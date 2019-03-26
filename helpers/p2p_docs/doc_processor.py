# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import re


class DocProcessor:
    """Processor for parsed documentation data to prepare data for rendering.
    The DocProcessor covers the part of processing which is independent of the
    concrete rendering format.

    It handles adding links to references to P2P messages and adding field size
    data for tables containing data types.
    """
    def __init__(self):
        self.message = None

    def auto_link_xips(self, text):
        processed = ""
        start_text = 0
        for match in re.finditer(r'([UB]IP)-? ?(\d+)', text):
            xip_type = match.group(1)
            xip_number = match.group(2)
            processed += text[start_text:match.start()]
            start_text = match.end()
            if xip_type == "BIP":
                processed += "[BIP-{0}](https://github.com/bitcoin/bips/blob/master/bip-{0:04}.mediawiki)".format(int(xip_number))
            elif xip_type == "UIP":
                processed += "[UIP-{0}](https://github.com/dtr-org/uips/blob/master/UIP-{0:04}.md)".format(int(xip_number))
            else:
                raise Exception("Unknown XIP type: '%s'" % xip_type)
        processed += text[start_text:]
        return processed

    def auto_link_messages(self, text):
        processed = ""
        start_text = 0
        for match in re.finditer(r'[“"](.*?)[”"]', text):
            message = match.group(1)
            processed += text[start_text:match.start()]
            start_text = match.end() + 1 + len("message")
            if message != self.message and text[match.end() + 1:start_text] == "message":
                processed += '["%s" message' % message
                if start_text < len(text) and text[start_text] == "s":
                    processed += "s"
                    start_text += 1
                processed += "](message:%s)" % message
            else:
                start_text = match.start()
        processed += text[start_text:]
        return processed

    def process_text(self, method):
        for section in self.doc_data:
            if section["type"] == "text":
                section["data"] = method(section["data"])
            elif section["type"] == "format" or section["type"] == "table":
                for row in section["data"]:
                    for field in row:
                        row[field] = method(row[field])

    def size_for_type(self, data_type):
        if data_type == "char" or data_type == "bool":
            return "1"
        if data_type in ["CompactSize", "*Varies*", "string", "TxOut",
                         "Transaction", "coinbasescript", "*None*"] or data_type.startswith("vector<"):
            return "*Varies*"
        int_match = re.match(r"^u?int(\d+)$", data_type)
        if int_match:
            return str(int(int(int_match.group(1)) / 8))
        array_match = re.match(r"^(.*)\[(.*)\]$", data_type)
        if array_match:
            size = array_match.group(2)
            if not size:
                return "*Varies*"
            else:
                return size
        if data_type == "BlockHeader":
            return "80"
        if data_type == "Address":
            return "26"
        if data_type == "Outpoint":
            return "36"
        raise Exception("Unable to calculate size for type '%s'" % data_type)

    def add_bytes_to_table(self, section):
        for row in section["data"]:
            row["Bytes"] = self.size_for_type(row["Data Type"])

    def add_type_sizes(self):
        for section in self.doc_data:
            if section["type"] == "format" or section["type"] == "table":
                headers = section["args"]
                if "Data Type" in headers:
                    headers.insert(headers.index("Data Type") + 1, "Bytes")
                    self.add_bytes_to_table(section)

    def process(self, doc_data):
        """Process the doc data given in the `doc_data` parameter. The data has
        to be in the format returned by the DocParser. Returns the processed
        data in the same data structure.
        """
        self.doc_data = doc_data
        self.process_text(self.auto_link_messages)
        self.process_text(self.auto_link_xips)
        self.add_type_sizes()
        return self.doc_data
