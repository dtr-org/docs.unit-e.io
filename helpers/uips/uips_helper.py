#!/usr/bin/env python3
# Copyright (c) 2018-2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
#
# This is an adation of hUIPon.py
# (https://github.com/dtr-org/uips/blob/master/adrs/hUIPon.py)

import os
import re
import sys

"""A simple script that generates a RST file for all the UIPs"""


class UIPsHelper:

    def __init__(self):
        pass

    def generate(self, uips_dir):
        toc_filename = os.path.abspath(__file__ + "/../../../reference/uips.rst")
        lines =[]
        with open(toc_filename, "r") as toc_file:
            found_table = False
            for line in toc_file:
                if line.startswith('*'):
                    if not found_table:
                        lines += self.generate_table(uips_dir)
                        found_table = True
                else:
                    lines.append(line.rstrip())
        with open(toc_filename, "w") as toc_file:
            for l in lines:
                toc_file.write(l + "\n")

    def generate_table(self, uips_dir):
        lines = []

        uips = self.list_uips(uips_dir)

        for uip in uips:
            num = "`" + uip[:-3] + " <https://github.com/dtr-org/uips/blob/master/" + uip + ">`_"
            with open(uips_dir + "/" + uip, "r") as file:
                title = ""
                status = ""
                created = ""
                complete = False
                for i in range(1, 10):
                    next_line = file.readline()

                    if not title and re.match("^# UIP-[0-9]*[: ].*$", next_line):
                        title = re.search("^# UIP-[0-9]*[: ](.*)$", next_line).group(1).strip()

                    if not status and re.match("^Status:.*$", next_line):
                        status = re.search("^Status:(.*)$", next_line).group(1).strip()

                    if not created and re.match("^Created:.*$", next_line):
                        created = re.search("^Created:(.*)$", next_line).group(1).strip()
                        complete = True
                        break

                if not complete:
                    raise Exception("Cannot parse file: " + uip)

            new_entry = "* " + num + " - " + title
            lines.append(new_entry)

        return lines


    def list_uips(self, uips_dir):
        uips = []

        for filename in os.listdir(uips_dir):
            if re.match(r"^UIP-[0-9]{4}\.md", filename) and filename != "UIP-0000.md":
                uips.append(filename)

        uips.sort(key=lambda a: int(re.search(r"^UIP-([0-9]{4})\.md", a).group(1)))
        return uips


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: uips_helper.py <directory with checkout of uips repo>")

    UIPsHelper().generate(sys.argv[1])
