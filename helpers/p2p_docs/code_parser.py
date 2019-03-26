# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from pathlib import Path
import re


class CodeParser:
    """Parser for p2p messsage information from the C++ source code."""
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir) / "src"

    def parse(self):
        """Parse the C++ source code and return a dictionary of the messages
        found there. Each message is represented by a dictionary containing its
        'name', a 'text' description, and possibly 'since' and 'since_note'
        notes with information about its history.
        """
        messages = {}
        with (self.source_dir / "protocol.h").open() as header_file:
            parsing = False
            text = ""
            since = None
            since_note = ""
            for line in header_file:
                if parsing:
                    match = re.match(r'extern const char \*(.*);', line)
                    if match:
                        symbol = match.group(1)
                        message = {"text": text}
                        if since:
                            message["since"] = since
                        if since_note:
                            message["since_note"] = since_note
                        messages[symbol] = message
                        text = ""
                        since = None
                        since_note = ""
                    elif line.startswith("}"):
                        break
                    else:
                        if line.startswith(" * @since "):
                            since = line[10:].rstrip(".\n")
                        elif line.startswith(" *   "):
                            if since_note:
                                since_note += " "
                            since_note += line[5:].rstrip()
                        elif line.startswith(" * @see"):
                            pass
                        elif line.startswith(" * "):
                            if text:
                                text += " "
                            text += line[3:].rstrip()
                elif line.startswith("namespace NetMsgType"):
                    parsing = True

        with (self.source_dir / "protocol.cpp").open() as impl_file:
            parsing = False
            for line in impl_file:
                if parsing:
                    match = re.match(r'const char \*(.*)="(.*)";', line)
                    if match:
                        symbol = match.group(1)
                        name = match.group(2)
                        messages[symbol]["name"] = name
                    elif line.startswith("}"):
                        break
                elif line.startswith("namespace NetMsgType"):
                    parsing = True

        return messages
