# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from doc_parser import DocParser
import pytest


def test_parse_format():
    doc_data = """one line
another line

\\startformat
name1
type1
description1

name2
type2
description2
\\endformat

\\startformat
name3
type3
description3
\\endformat

some more text
"""

    parsed = DocParser().parse(doc_data)

    assert len(parsed) == 5

    assert parsed[0]["type"] == "text"
    assert parsed[0]["data"] == "one line\nanother line\n\n"

    assert parsed[1]["type"] == "format"
    assert parsed[1]["data"] == [
        {
            "Name": "name1",
            "Data Type": "type1",
            "Description": "description1",
        },
        {
            "Name": "name2",
            "Data Type": "type2",
            "Description": "description2",
        },
    ]

    assert parsed[2]["type"] == "text"
    assert parsed[2]["data"] == "\n"

    assert parsed[3]["type"] == "format"
    assert parsed[3]["data"] == [
        {
            "Name": "name3",
            "Data Type": "type3",
            "Description": "description3",
        },
    ]

    assert parsed[4]["type"] == "text"
    assert parsed[4]["data"] == "\nsome more text\n"


def test_parse_error():
    doc_data = r"\startformat\n"

    with pytest.raises(DocParser.Error):
        DocParser().parse(doc_data)


def test_parse_table():
    doc_data = r"""\starttable One, Column Two, Three
row1 1
row1 2
row1 3

row2 1
row2 2
row2 3
\endtable
"""
    parsed = DocParser().parse(doc_data)

    assert parsed[0]["type"] == "table"
    assert parsed[0]["args"] == ["One", "Column Two", "Three"]
    assert parsed[0]["data"] == [
        {
            "One": "row1 1",
            "Column Two": "row1 2",
            "Three": "row1 3",
        },
        {
            "One": "row2 1",
            "Column Two": "row2 2",
            "Three": "row2 3",
        },
    ]


def test_parse_example():
    doc_data = r"""\startexample nointro
xyz
\endexample
"""
    parsed = DocParser().parse(doc_data)

    assert parsed[0]["type"] == "example"
    assert parsed[0]["args"] == ["nointro"]
    assert parsed[0]["data"] == "xyz\n"

    doc_data = r"""\startexample
xyz
\endexample
"""
    parsed = DocParser().parse(doc_data)

    assert parsed[0]["type"] == "example"
    assert parsed[0]["args"] == []
    assert parsed[0]["data"] == "xyz\n"


def test_parse_figure():
    doc_data = r"\figure /some/path, Some title"
    parsed = DocParser().parse(doc_data)
    assert parsed[0]["type"] == "figure"
    assert parsed[0]["args"] == ["/some/path", "Some title"]
    assert "data" not in parsed[0]


def test_parse_copyright():
    doc_data = r"\copyright bitcoin, unit-e"
    parsed = DocParser().parse(doc_data)
    assert parsed[0]["type"] == "copyright"
    assert parsed[0]["args"] == ["bitcoin", "unit-e"]
    assert "data" not in parsed[0]


def test_parse_todo():
    doc_data = r"\todo some thing"
    parsed = DocParser().parse(doc_data)
    assert parsed[0]["type"] == "todo"
    assert parsed[0]["args"] == "some thing"
    assert "data" not in parsed[0]


def test_parse_args():
    parser = DocParser()
    assert parser.parse_args("") == []
    assert parser.parse_args(" ") == []
    assert parser.parse_args("one") == ["one"]
    assert parser.parse_args("one,two") == ["one", "two"]
    assert parser.parse_args("one, two two") == ["one", "two two"]
    assert parser.parse_args(" one, two ") == ["one", "two"]
