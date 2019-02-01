# Copyright (c) 2018 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from rpc_docs import process_command_help
from help_parser import HelpParser
from pathlib import Path
import os

test_data_dir = Path(os.path.dirname(__file__)) / "test_data"


def test_process_command_help():
    for cmd in ['getbestblockhash', 'calcsnapshothash', 'getblockchaininfo',
                'listsnapshots', 'getblock', 'getbalance', 'bumpfee',
                'getchaintips', 'getmempoolancestors', 'preciousblock',
                'importmulti', 'listunspent', 'examplecommand2', 'estimatefee']:
        with open(test_data_dir / cmd) as file:
            input = file.read()
        with open(test_data_dir / (cmd + ".expected")) as file:
            expected_output = file.read()
        assert process_command_help(input) == expected_output


def test_parse_help():
    with open(test_data_dir / "examplecommand") as file:
        input = file.read()
    result = HelpParser().parse_help(input)
    assert result["command"] == 'examplecommand "arg" "object" ( "optional-arg" )'
    assert result["description"] == "Returns the hash of the best (tip) block in the longest blockchain.\n"
    assert len(result["arguments"]) == 8
    assert result["arguments"][0] == {
        'name': 'arg', 'type': 'string, required',
        'description': 'An argument.'}
    assert result["arguments"][1] == {
        'name': 'otherarg', 'type': 'string, required',
        'description': 'Line one\n       line two'}
    assert result["arguments"][2] == {
        'name': 'object',
        'type': 'array, required',
        'description': 'Some data',
        'literal_description': '  [     (array of json objects)\n'
        '    {\n'
        '      "key": "value", (type) desc\n'
        '    }\n'
        '  ,...\n'
        '  ]\n',
    }
    assert result["arguments"][3] == {
        'name': 'optional-arg', 'type': 'string, optional',
        'description': 'An optional argument.'}
    assert result["arguments"][4] == {
        'name': 'options',
        'type': 'json, optional',
        'description': '',
        'literal_description': '  {\n'
        '     "rescan": <false>, (xx) yy\n'
        '  }\n',
    }
    assert result["arguments"][5] == {
        'name': 'commands',
        'type': 'required',
        'description': 'list of commands to send:\n'
        "       {'cmd': 'END_PERMISSIONING'}\n"
        "       {'cmd': 'ADD_TO_WHITELIST', 'payload': <keys>}",
    }
    assert result["arguments"][6] == {
        'name': 'inputs',
        'type': 'array',
        'description': 'A json array',
        'literal_description': '     [\n'
        '       {\n'
        '         "txid":"id",    (s) id\n'
        '                             [vout_index,...]\n'
        '       }\n'
        '       ,...\n'
        '     ]\n',
    }
    assert result["arguments"][7] == {
        'name': 'outputs',
        'type': 'object',
        'description': 'a json object',
        'literal_description': '    {\n'
        '      "address": x.xxx,    (ns) a\n'
        '      "data": "hex"      (s) data\n'
        '      ,...\n'
        '    }\n',
    }
    assert result["results"] == [{'format': 'table', 'title_extension': '',
                                  'name': "hex", "type": "string",
                                  "description": "the block hash hex encoded"}]
    assert result["examples"] == ["> unite-cli examplecommand foo",
                                  "> curl --user myusername --data-binary someargs"]


def test_parse_help_result_with_quotes():
    assert HelpParser().parse_help_result('"hex"      (string) the block hash hex encoded') == {
        'format': 'table', 'name': 'hex', 'type': 'string', 'description': 'the block hash hex encoded'}


def test_parse_help_result_without_quotes():
    assert HelpParser().parse_help_result('hex      (string) the block hash hex encoded') == {
        'format': 'table', 'name': 'hex', 'type': 'string', 'description': 'the block hash hex encoded'}

def test_parse_help_argument_with_quotes():
    assert HelpParser().parse_help_argument('1. "inputs" (hex, required) serialized UTXOs to subtract.') == {
        'name': 'inputs', 'type': 'hex, required', 'description': 'serialized UTXOs to subtract.'}


def test_parse_help_argument_without_quotes():
    assert HelpParser().parse_help_argument('1. inputs (hex, required) serialized UTXOs to subtract.') == {
        'name': 'inputs', 'type': 'hex, required', 'description': 'serialized UTXOs to subtract.'}


def test_parse_help_arguments_without_description():
    assert HelpParser().parse_help_argument('2. options               (object, optional)') == {
        'name': 'options', 'type': 'object, optional', 'description': ''}


def test_check_and_set_json_level():
    parser = HelpParser()

    def check(line, expected_json_level):
        parser.check_opening_json(line)
        assert parser.json_level == expected_json_level

    check(' x', 0)
    check(' {', 1)
    check(' [', 2)
    check(' []', 2)
    check(' {}', 2)
    check(' {},', 2)
    check(' [],', 2)
