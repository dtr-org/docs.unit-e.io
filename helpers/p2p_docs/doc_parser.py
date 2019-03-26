# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import re


class DocParser:
    """Parser for the documentation data in the `doc_data` directory.

    The documentation is stored in a simple text-based format with a few control
    commands to mark up special sections such as a definition of the format of
    a P2P message or an example.

    The parsed data is returned as an array of dictionaries, each representing
    a section of a piece of documentation. The data is meant for further
    processing and rendering in a format which can be used for displaying the
    documentation to users, such as RST.
    """
    class Error(Exception):
        """Error class thrown on a parsing error."""
        pass

    def __init__(self):
        pass

    def parse_args(self, arg_str):
        args = arg_str.split(",")
        result = []
        for arg in args:
            stripped_arg = arg.lstrip().rstrip()
            if stripped_arg:
                result.append(stripped_arg)
        return result

    def parse_single_line_command(self, command, line, parse_args=True):
        self.end_text_section()
        if parse_args:
            args = self.parse_args(line[len(command)+1:])
        else:
            args = line[len(command)+1:].lstrip()
        self.append_section(command, args=args)

    def append_section(self, section_type, args=None, data=None):
        section = {
            "type": section_type
        }
        if args is not None:
            section["args"] = args
        if data is not None:
            section["data"] = data
        self.sections.append(section)

    def end_text_section(self):
        if self.text is not None:
            self.append_section("text", data=self.text)
        self.text = ""

    def parse(self, input):
        """Parse documentation data string given as `input` parameter and
        return an array of dictionaries containing the sections of the document.
        """
        self.sections = []
        self.text = None
        current_section = None
        table_rows = []
        args = []
        for line in input.rstrip().split("\n"):
            command_match = re.match(
                r'\\start(table|format|example)(.*)', line)
            if command_match:
                self.end_text_section()
                command = command_match.group(1)
                current_section = command
                if command == "format":
                    args = ["Name", "Data Type", "Description"]
                    row = {}
                    column_to_parse = 0
                elif command == "table":
                    args = self.parse_args(command_match.group(2))
                    row = {}
                    column_to_parse = 0
                elif command == "example":
                    args = self.parse_args(command_match.group(2))
                else:
                    raise self.Error("Unknown command: '%s'" % line)
            elif current_section == "format" or current_section == "table":
                if line.startswith("\\end" + current_section):
                    self.append_section(
                        current_section, args=args, data=table_rows)
                    table_rows = []
                    current_section = None
                else:
                    if not line:
                        continue
                    row[args[column_to_parse]] = line
                    column_to_parse += 1
                    if column_to_parse == len(args):
                        table_rows.append(row)
                        row = {}
                        column_to_parse = 0
            elif current_section == "example":
                if line.startswith("\\endexample"):
                    self.append_section("example", args=args, data=self.text)
                    self.text = ""
                    current_section = None
                else:
                    self.text += line + "\n"
            elif line.startswith("\\figure"):
                self.parse_single_line_command("figure", line)
            elif line.startswith("\\copyright"):
                self.parse_single_line_command("copyright", line)
            elif line.startswith("\\todo"):
                self.parse_single_line_command("todo", line, parse_args=False)
            else:
                if self.text is None:
                    self.text = ""
                self.text += line + "\n"
        if current_section:
            raise self.Error("Missing \\end" + current_section)
        if self.text:
            self.append_section("text", data=self.text)
        return self.sections
