#!/usr/bin/env python3
# Copyright (c) 2018 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import subprocess
import re
import os
import sys

from collections import defaultdict
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from help_parser import HelpParser

unit_e_path = os.environ.get("UNIT_E_PATH")
if not unit_e_path:
    sys.exit("UNIT_E_PATH is not set. Exiting.")

unite_cli = Path(unit_e_path) / "src/unite-cli"
base_dir = (Path(os.path.dirname(__file__)) / "../..").resolve()
output_dir = base_dir / "reference/rpc"
template_dir = base_dir / "helpers/rpc_docs/templates"


def cli(cmd):
    result = subprocess.run([unite_cli, "-regtest"] +
                            cmd, stdout=subprocess.PIPE)
    return result.stdout.rstrip().decode("utf-8")


def write_command_page(command):
    command_output = cli(["help", command])
    command_file = command + ".rst"
    with open(output_dir / command_file, "w") as file:
        file.write(command_output)


def titleunderline(value):
    return '-' * len(value)


def split_command(value):
    return value.split()[0]


def table(rows, title=None):
    output = '.. list-table::'
    if title:
        output += ' ' + title
    output += '\n   :header-rows: 1\n\n'
    output += '   * - Name\n     - Type\n     - Description\n'
    for row in rows:
        output += '   * - ' + row["name"] + '\n'
        output += '     - ' + row["type"] + '\n'
        if row["description"]:
            description = row["description"]
        else:
            description = "object"
        output += '     - ' + description + '\n'
    return output


def process_command_help(input):
    help_data = HelpParser().parse_help(input)
    output = '``' + help_data["command"] + '``\n\n'
    output += help_data['description'] + '\n'
    if help_data['arguments']:
        number = 1
        for argument in help_data['arguments']:
            title = 'Argument #' + str(number) + ' - ' + argument['name']
            output += title + '\n'
            output += '~' * len(title) + '\n\n'
            output += '**Type:** ' + argument['type'] + '\n\n'
            if argument['description']:
                output += argument['description'] + '\n\n'
            if 'literal_description' in argument:
                output += '::\n\n' + argument['literal_description'] + '\n'
            number += 1
    if help_data['results']:
        for result in help_data['results']:
            if result and 'format' in result:
                if result['format'] == 'table':
                    full_title = "Result"
                    if 'title_extension' in result:
                        full_title += result['title_extension']
                    output += full_title + '\n'
                    output += '~' * len(full_title) + '\n\n'
                    output += table([result]) + '\n'
                elif result['format'] == 'literal':
                    result_title = 'Result'
                    if 'title_extension' in result:
                        result_title += result['title_extension']
                    output += result_title + '\n' + '~' * \
                        len(result_title) + '\n\n::\n\n' + \
                        result['text'] + '\n'
    if help_data["examples"]:
        output += 'Examples\n~~~~~~~~\n\n'
        text = ''
        for example_line in help_data['examples']:
            if example_line.startswith('> '):
                output += text + '::\n\n'
                output += '  ' + example_line[2:].rstrip() + '\n\n'
                text = ''
            else:
                text += example_line
    return output


def render_cmd_page(env, command):
    print("Command: " + command)

    command_template = env.get_template("command.rst")
    command_output = cli(["help", command])
    command_file = command + ".rst"
    with open(output_dir / command_file, "w") as file:
        file.write(command_template.render(
                title=command,
                content=process_command_help(command_output)))


def render_pages(env):
    help_output = cli(["help"])
    all_commands = defaultdict(list)
    group = ""
    for line in help_output.splitlines():
        pattern = re.compile("== (.*) ==")
        match = pattern.match(line)
        if match:
            group = match.group(1)
        else:
            if len(line) > 0:
                all_commands[group].append(line.rstrip())

    template = env.get_template("index.rst")
    with open(output_dir / "index.rst", "w") as file:
        file.write(template.render(all_commands=all_commands))

    for group in all_commands:
        for full_command in all_commands[group]:
            command = full_command.split()[0]
            render_cmd_page(env, command)


def main():
    env = Environment(loader=FileSystemLoader(
        str(template_dir)), trim_blocks=True)
    env.filters['titleunderline'] = titleunderline
    env.filters['splitcommand'] = split_command

    if len(sys.argv) == 2:
        render_cmd_page(env, sys.argv[1])
    else:
        render_pages(env)


if __name__ == '__main__':
    main()
