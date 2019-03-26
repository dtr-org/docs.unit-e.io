# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from doc_processor import DocProcessor


def test_process():
    doc_data = [
        {
            "type": "table",
            "args": ["Data Type", "Text"],
            "data": [
                {
                    "Data Type": "int32",
                    "Text": '"addr" message'
                },
            ]
        },
        {
            "type": "text",
            "data": 'Text with "some" message and UIP-1.',
        }
    ]

    processed = DocProcessor().process(doc_data)
    expected = [
        {
            "type": "table",
            "args": ["Data Type", "Bytes", "Text"],
            "data": [
                {
                    "Data Type": "int32",
                    "Bytes": "4",
                    "Text": '["addr" message](message:addr)'
                },
            ]
        },
        {
            "type": "text",
            "data": 'Text with ["some" message](message:some) and [UIP-1](https://github.com/dtr-org/uips/blob/master/UIP-0001.md).'
        }
    ]
    assert processed == expected


def test_auto_link_messages():
    processor = DocProcessor()
    processor.message = "self"

    tests = [
        [
            "x",
            "x",
        ],
        [
            '“abc” message',
            '["abc" message](message:abc)',
        ],
        [
            '"abc" message',
            '["abc" message](message:abc)',
        ],
        [
            '“abc” message\n“def” message',
            '["abc" message](message:abc)\n["def" message](message:def)',
        ],
        [
            '"self" message',
            '"self" message',
        ],
        [
            '“xyz” messages',
            '["xyz" messages](message:xyz)',
        ],
        [
            '["MSG"](/en/de) x "abc" message.',
            '["MSG"](/en/de) x ["abc" message](message:abc).',
        ],
        [
            '“xyz” message\'s',
            '["xyz" message](message:xyz)\'s',
        ],
    ]

    for test in tests:
        assert processor.auto_link_messages(test[0]) == test[1]


def test_auto_link_xips():
    processor = DocProcessor()
    processor.message = "self"

    uip12_link = '[UIP-12](https://github.com/dtr-org/uips/blob/master/UIP-0012.md)'
    uip8_link = '[UIP-8](https://github.com/dtr-org/uips/blob/master/UIP-0008.md)'

    bip37_link = "[BIP-37](https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki)"
    bip130_link = "[BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)"

    tests = [
        [
            "x",
            "x",
        ],
        [
            'UIP12',
            uip12_link,
        ],
        [
            'UIP-12',
            uip12_link,
        ],
        [
            'UIP 12',
            uip12_link,
        ],
        [
            'UIP-12,a',
            uip12_link + ',a',
        ],
        [
            'a UIP-8 b UIP-12 c',
            'a ' + uip8_link + ' b ' + uip12_link + ' c',
        ],
        [
            'BIP37',
            bip37_link,
        ],
        [
            'BIP-130',
            bip130_link,
        ],
        [
            'UIP-12, BIP-37.',
            uip12_link + ', ' + bip37_link + '.'
        ]
    ]

    for test in tests:
        assert processor.auto_link_xips(test[0]) == test[1]


def test_add_bytes_to_table():
    section = {
        "type": "table",
        "args": ["Data Type"],
        "data": [
            {
                "Data Type": "int32",
            },
            {
                "Data Type": "char",
            },
            {
                "Data Type": "CompactSize",
            }
        ]
    }
    DocProcessor().add_bytes_to_table(section)
    expected_section = {
        "type": "table",
        "args": ["Data Type"],
        "data": [
            {
                "Data Type": "int32",
                "Bytes": "4",
            },
            {
                "Data Type": "char",
                "Bytes": "1",
            },
            {
                "Data Type": "CompactSize",
                "Bytes": "*Varies*",
            }
        ]
    }
    assert section == expected_section


def test_size_for_type():
    tests = {
        "uint8": "1",
        "int32": "4",
        "uint8[]": "*Varies*",
    }
    for test in tests:
        assert DocProcessor().size_for_type(test) == tests[test]
