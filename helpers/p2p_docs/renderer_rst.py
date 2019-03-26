# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from pathlib import Path
from collections import OrderedDict
from collections import defaultdict
import re
import os

from doc_parser import DocParser
from doc_processor import DocProcessor


class RendererRST:
    """Renderer creating reStructuredText (RST) formatted output from doc data.

    The renderer reads doc data files from the doc_data directory and creates
    corresponding RST files with the output for processing through Sphinx. The
    data is parsed with the DocParser and pre-processed with the DocProcessor.

    The `render` method is the central entry point for generating the RST files.
    """
    class Error(Exception):
        pass

    def __init__(self):
        self.clear()

    def clear(self):
        self.message = ""
        self.data_types = defaultdict(list)
        self.link_targets = set()

    def render_copyright_header(self, sections):
        r"""Render a copyright header with attributions to the copyright holders
        defined with the \copyright command.
        """
        copyright_holders = None
        for section in sections:
            if section["type"] == "copyright":
                copyright_holders = section["args"]
        if copyright_holders:
            result = ""
            result += ".. "
            if "bitcoin" in copyright_holders:
                result += "Copyright (c) 2014-2018 Bitcoin.org\n"
            if "unit-e" in copyright_holders:
                if len(copyright_holders) > 1:
                    result += "   "
                result += "Copyright (c) 2019 The Unit-e developers\n"
            result += "   Distributed under the MIT software license, see the accompanying\n"
            result += "   file LICENSE or https://opensource.org/licenses/MIT.\n\n"
            return result
        else:
            return ""

    def render_link_targets(self):
        """Render RST link targets which are referenced by the type links in
        the format tables. The targets are defined at the end of the document.
        """
        if not self.link_targets:
            return ""
        result = "\n"
        for target in sorted(self.link_targets):
            result += ".. _" + target + ": "
            if not self.message.startswith("types/"):
                result += "types/"
            if re.match(r"u?int\d+", target):
                result += "Integers"
            else:
                result += target
            result += ".html\n"
        return result

    def render_source_footer(self, sections):
        """Render footer at the end of the document with a link to where the
        original data came from.
        """
        for section in sections:
            if section["type"] == "copyright" and "bitcoin" in section["args"]:
                return "\n.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/\n"
        return ""

    def resolve_link_target(self, target):
        """Resolve a generic link of the form 'scheme:path' into a concrete
        link which can be resolved in the context of the RST file.
        """
        match = re.match("(.*?):(.*)", target)
        if match:
            scheme = match.group(1)
            path = match.group(2)
            prefix = ""
            if scheme == "message":
                if self.message.startswith("types/"):
                    prefix = "../"
                link = path + ".html"
            elif scheme == "intro":
                if self.message.startswith("types/"):
                    prefix = "../"
                link = "intro.html#" + path
            elif scheme == "type":
                if not self.message.startswith("types/"):
                    prefix = "types/"
                link = path + ".html"
            elif scheme == "http" or scheme == "https":
                link = target
            else:
                raise Exception("Unknown link target scheme: '%s'" % scheme)
            return prefix + link
        else:
            return target

    def auto_link_type(self, text):
        """Automatically create links to the corresponding type page for data
        type entries, which for example occur in format tables. The method
        returns a marked up version of the given text. For the links to work
        the `render_link_targets` method has to be called to add the target
        definitions at the end of the file.
        """
        vector_match = re.match("vector<(.*)>", text)
        if vector_match:
            type_name = vector_match.group(1)
            self.link_targets.add("vector")
            self.link_targets.add(type_name)
            return r"vector_\<%s_>" % (type_name)
        int_match = re.match(r"^u?int\d*$", text)
        if int_match:
            self.link_targets.add(text)
            return "%s_" % text
        array_match = re.match(r"^(.*)\[(\d*)\]$", text)
        if array_match:
            data_type = array_match.group(1)
            size = array_match.group(2)
            self.link_targets.add(data_type)
            return r"%s_\[%s]" % (data_type, size)
        if text in ["CompactSize", "BlockHeader", "Transaction", "TxIn",
                    "TxOut", "Outpoint",
                    "OutputMapping", "UTXOSubset", "char", "string", "bool",
                    "PrefilledTransaction", "Address"]:
            self.link_targets.add(text)
            return "%s_" % text
        non_types = ["*Varies*", "*None*", "coinbasescript"]
        if text not in non_types:
            print("  Unrecognized type:", text)
        return text

    def process_links(self, text):
        """Turn generic links of the form '[text](target)' into the
        corresponding RST equivalent.
        """
        processed = ""
        start_text = 0
        for match in re.finditer(r'\[(.*?)\]\((.*?)\)', text):
            link_text = match.group(1)
            link_target = match.group(2)
            processed += text[start_text:match.start()]
            processed += "`%s <%s>`__" % (link_text,
                                          self.resolve_link_target(link_target))
            start_text = match.end()
        processed += text[start_text:]
        return processed

    def process_headers(self, text):
        """Turn markdown style headers of the form '#', '##', '###', etc. into
        the corresponding RST equivalent.
        """
        processed = ""
        lines = text.split("\n")
        for i, line in enumerate(lines):
            match = re.match("^(#+)(.*)", line)
            if match:
                header_markup = match.group(1)
                header_text = match.group(2).lstrip()
                processed += header_text + "\n"
                processed += "=-~^'"[len(header_markup) - 1] * \
                    (len(header_text)) + "\n"
            else:
                processed += line
                if i < len(lines) - 1 or line.endswith("\n"):
                    processed += "\n"
        return processed

    def process_text(self, text):
        """Call all the processing methods on the given text."""
        processors = [
            self.process_links,
            self.process_headers,
        ]
        processed = text
        for processor in processors:
            processed = processor(processed)
        return processed

    def render_doc_text(self, section):
        """Render text section."""
        return self.process_text(section["data"])

    def maximize_width(self, widths, row, element_name):
        width = len(self.process_text(row[element_name]))
        if width > widths[element_name]:
            widths[element_name] = width

    def table_line(self, widths, char='-'):
        result = ""
        for field in widths.keys():
            result += "+" + char * widths[field]
        return result + "+\n"

    def table_row(self, entries, widths):
        result = ""
        for field in widths.keys():
            field_text = self.process_text(entries[field])
            result += "| " + field_text + ' ' * \
                (widths[field] - len(field_text) - 1)
        return result + "|\n"

    def render_doc_table(self, section):
        """Render table section."""
        headers = section["args"]

        widths = OrderedDict()
        for field in headers:
            widths[field] = len(field)
        for row in section["data"]:
            for field in headers:
                if field == "Data Type":
                    self.data_types[row["Data Type"]].append(self.message)
                    row["Data Type"] = self.auto_link_type(row["Data Type"])
                self.maximize_width(widths, row, field)
        for field in headers:
            widths[field] += 2

        headers_dict = {}
        for field in headers:
            headers_dict[field] = field

        result = ""
        result += self.table_line(widths)
        result += self.table_row(headers_dict, widths)
        result += self.table_line(widths, "=")
        for row in section["data"]:
            result += self.table_row(row, widths)
            result += self.table_line(widths)

        return result

    def render_doc_example(self, section):
        """Render example."""
        result = ""
        if "intro" in section["args"]:
            result += 'The annotated hexdump below shows a `"' + self.message
            result += '" message <' + self.message
            result += ".html>`__. (The message header has been omitted.)\n\n"

        result += ".. highlight:: "
        if "c++" in section["args"]:
            result += "c++"
        else:
            result += "text"
        result += "\n\n::\n\n"
        for line in section["data"].rstrip().split("\n"):
            if line:
                result += "   " + line
            result += "\n"
        return result

    def render_doc_figure(self, section):
        """Render figure."""
        result = ".. figure:: " + section["args"][0] + "\n"
        result += "   :alt: " + section["args"][1] + "\n\n"
        result += "   " + section["args"][1] + "\n"
        return result

    def render_doc_nop(self, section):
        """Don't do anything."""
        return ""

    def render_doc_todo(self, section):
        """Render a note about a todo item."""
        return "**TODO: %s**\n" % section["args"]

    def render_doc(self, message, sections):
        """Return a rendered RST string from the given sections for the given
        message. The sections have to be in the structure as returned by the
        DocParser.
        """
        self.message = message
        self.link_targets = set()
        result = ""
        handlers = {
            "format": self.render_doc_table,
            "table": self.render_doc_table,
            "example": self.render_doc_example,
            "figure": self.render_doc_figure,
            "text": self.render_doc_text,
            "copyright": self.render_doc_nop,
            "todo": self.render_doc_todo,
        }
        for section in sections:
            if section["type"] in handlers:
                result += handlers[section["type"]](section)
            else:
                raise Exception("No handler for section type '%s'" %
                                section["type"])

        # Remove trailing empty lines
        while(result.endswith("\n\n")):
            result = result[:-1]

        return result

    def render_file(self, output_dir, name, message=None, title=True):
        """Create RST file in the given output directory for the message with
        the given name. Optionally takes a message object as returned by the
        CodeParser. This is rendered together with the information from the
        file in the `doc_data` directory which corresponds to the message with
        the given name.
        """
        filename = output_dir / (name + ".rst")
        with filename.open("w") as file:
            with (Path("doc_data") / (name + ".txt")).open() as data_file:
                doc_data = data_file.read()
            sections = DocParser().parse(doc_data)
            doc_processor = DocProcessor()
            doc_processor.message = name
            processed_sections = doc_processor.process(sections)
            file.write(self.render_copyright_header(processed_sections))
            if title:
                match = re.match("types/(.*)", name)
                if match:
                    title_str = match.group(1)
                else:
                    title_str = name
                file.write(title_str + "\n")
                file.write("-" * len(title_str) + "\n\n")
            if message:
                file.write(message["text"])
                if not doc_data.startswith("\n"):
                    file.write(" ")
                else:
                    file.write("\n")
            file.write(self.render_doc(name, processed_sections))
            file.write(self.render_link_targets())
            file.write(self.render_source_footer(processed_sections))

    def render_toc_header(self, title=None):
        result = "\n"
        if title:
            result += "\n%s\n" % title
            result += "-" * len(title) + "\n\n"
        result += ".. toctree::\n"
        result += "  :maxdepth: 1\n\n"
        return result

    def render(self, messages, show_data_types=False):
        """Render RST files from doc sources.

        The `messages` parameter takes a list of structures as returned by the
        CodeParser. If the `show_data_types` option is set a summary of the
        data types used in the processed data is put out.

        The renderer generates an index file with references to all P2P
        messages, a file for each message, and a file for each data type used
        in the commands. It also renders an `intro` file with general
        information about the P2P messages.
        """
        output_dir = Path("../../reference/p2p/")
        index_filename = output_dir / "index.rst"
        with index_filename.open("w") as index_file:
            index_file.write("P2P Network Protocol\n")
            index_file.write("=======================\n")
            index_file.write(self.render_toc_header())
            index_file.write("  intro\n")
            print("Rendering intro")
            self.render_file(output_dir, "intro", title=False)

            index_file.write(self.render_toc_header("Messages"))
            for key in sorted(messages.keys()):
                message = messages[key]
                name = message["name"]
                index_file.write("  " + name + "\n")
                print("Rendering message", name)
                self.render_file(output_dir, name, message=message)

            index_file.write(self.render_toc_header("Data Types"))

            for type_file in sorted(Path("doc_data/types/").glob("*.txt")):
                type_name = os.path.splitext(type_file.name)[0]
                index_file.write("  types/" + type_name + "\n")
                print("Rendering type", type_name)
                self.render_file(output_dir, "types/" + type_name)

            if show_data_types:
                print("\nData Types:\n")
                for data_type in sorted(self.data_types.keys()):
                    print("  " + data_type +
                          " (" + ", ".join(self.data_types[data_type]) + ")")
