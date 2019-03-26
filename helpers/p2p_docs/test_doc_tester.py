import sys
import io
from pathlib import Path

from doc_tester import DocTester
from doc_parser import DocParser


def test_object():
    tester = DocTester("test_data")
    result = tester.test_object("inv", "1234 ..\n")
    assert result == "inv: PASS: msg_inv"


def test_extract_example():
    parser = DocParser()
    with Path("doc_data/feefilter.txt").open() as file:
        doc_data = parser.parse(file.read())

    tester = DocTester("test_data")

    example = tester.extract_example(doc_data)
    assert example == "7cbd000000000000 ... satoshis per kilobyte: 48,508\n"


def test_example_to_hex():
    tester = DocTester("test_data")

    tests = [
        [
            "7cbd000000000000 ... satoshis per kilobyte: 48,508",
            "7cbd000000000000",
        ],
        [
            "  abcd",
            "abcd",
        ],
        [
            "| | 48 .................................... Push 72 bytes as data",
            "48",
        ]
    ]

    for test in tests:
        assert tester.example_to_hex(test[0]) == test[1]
