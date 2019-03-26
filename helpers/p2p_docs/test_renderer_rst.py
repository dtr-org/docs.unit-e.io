# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from renderer_rst import RendererRST
from doc_parser import DocParser
from doc_processor import DocProcessor


def test_render_doc_example1():
    with open("test_data/doc_data/example.txt") as doc_file:
        doc_data = DocProcessor().process(DocParser().parse(doc_file.read()))
        rendered = RendererRST().render_doc("example", doc_data)
    with open("test_data/expected/example.rst") as expected_file:
        assert rendered == expected_file.read()


def test_render_doc_example2():
    with open("test_data/doc_data/tx.txt") as doc_file:
        doc_data = DocProcessor().process(DocParser().parse(doc_file.read()))
        rendered = RendererRST().render_doc("example", doc_data)
    with open("test_data/expected/tx.rst") as expected_file:
        assert rendered == expected_file.read()


def test_render_doc_example3():
    renderer = RendererRST()
    with open("test_data/doc_data/types/vector.txt") as doc_file:
        doc_data = DocProcessor().process(DocParser().parse(doc_file.read()))
        rendered = renderer.render_doc("types/vector", doc_data)
    rendered += renderer.render_link_targets()
    with open("test_data/expected/types/vector.rst") as expected_file:
        assert rendered == expected_file.read()


def test_render_doc_table_format():
    section = {
        "type": "table",
        "args": ["Name", "Data Type", "Required/Optional", "Description"],
        "data": [{
            "Name": "version",
            "Data Type": "int32",
            "Required/Optional": "Required",
            "Description": "Highest protocol version",
        }]
    }
    expected = """+---------+-----------+-------------------+--------------------------+
| Name    | Data Type | Required/Optional | Description              |
+=========+===========+===================+==========================+
| version | int32_    | Required          | Highest protocol version |
+---------+-----------+-------------------+--------------------------+
"""
    rendered = RendererRST().render_doc_table(section)
    assert rendered == expected


def test_render_doc_table_table():
    section = {
        "type": "table",
        "args": ["Value", "Name", "Description"],
        "data": [{
            "Value": "0",
            "Name": "SOMENAME",
            "Description": "Explain",
        }]
    }
    expected = """+-------+----------+-------------+
| Value | Name     | Description |
+=======+==========+=============+
| 0     | SOMENAME | Explain     |
+-------+----------+-------------+
"""
    rendered = RendererRST().render_doc_table(section)
    assert rendered == expected


def test_render_doc_example():
    section = {
        "type": "example",
        "args": ["intro"],
        "data": "xyz",
    }
    expected = """The annotated hexdump below shows a `"abc" message <abc.html>`__. (The message header has been omitted.)

.. highlight:: text

::

   xyz
"""
    renderer = RendererRST()
    renderer.message = "abc"
    assert renderer.render_doc_example(section) == expected


def test_render_doc_example_nointro():
    section = {
        "type": "example",
        "args": [],
        "data": "xyz",
    }
    expected = """.. highlight:: text

::

   xyz
"""
    assert RendererRST().render_doc_example(section) == expected


def test_render_doc_example_cpp():
    section = {
        "type": "example",
        "args": ["c++", "nointro"],
        "data": "some(code) * 4",
    }
    expected = """.. highlight:: c++

::

   some(code) * 4
"""
    assert RendererRST().render_doc_example(section) == expected


def test_process_links():
    renderer = RendererRST()

    tests = [
        [
            "abc",
            "abc"
        ],
        [
            "[ab](cd)",
            "`ab <cd>`__"
        ],
        [
            "[ab](cd) [efg](hij)",
            "`ab <cd>`__ `efg <hij>`__"
        ],
        [
            "xxx [ab](cd) yyy [efg](hij) zzz",
            "xxx `ab <cd>`__ yyy `efg <hij>`__ zzz"
        ],
        [
            "xxx [ab](cd)\nyyy [efg](hij) zzz",
            "xxx `ab <cd>`__\nyyy `efg <hij>`__ zzz"
        ],
        [
            "[ab](cd) (ef)",
            "`ab <cd>`__ (ef)"
        ],
        [
            "(``abc[...]``)",
            "(``abc[...]``)",
        ],
        [
            "[...]",
            "[...]",
        ]
    ]

    for test in tests:
        assert renderer.process_links(test[0]) == test[1]


def test_process_headers():
    renderer = RendererRST()

    tests = [
        [
            "## abc",
            "abc\n---\n",
        ],
        [
            "### de",
            "de\n~~\n",
        ],
        [
            "#### f",
            "f\n^\n",
        ],
        [
            "##### gh ij",
            "gh ij\n'''''\n",
        ],
        [
            "a b\nc ##\nd # e",
            "a b\nc ##\nd # e",
        ],
    ]

    for test in tests:
        assert renderer.process_headers(test[0]) == test[1]


def test_process_text_example1():
    source = """## Some title

Some text with a [link](http://example.com#section) to somewhere.

### Section 1

Text with [more](a/b) nice [links](/c/dd) to more nice places.

#### Subsection 1.1

More text
"""
    expected = """Some title
----------

Some text with a `link <http://example.com#section>`__ to somewhere.

Section 1
~~~~~~~~~

Text with `more <a/b>`__ nice `links </c/dd>`__ to more nice places.

Subsection 1.1
^^^^^^^^^^^^^^

More text
"""
    assert RendererRST().process_text(source) == expected


def test_resolve_link_target():
    renderer = RendererRST()

    tests = [
        [
            "message:abc",
            "abc.html",
        ],
        [
            "intro:message-header",
            "intro.html#message-header",
        ],
        [
            "type:sometype",
            "types/sometype.html",
        ],
    ]

    for test in tests:
        assert renderer.resolve_link_target(test[0]) == test[1]

    renderer.message = "types/one"
    assert renderer.resolve_link_target("type:two") == "two.html"


def test_render_copyright_header_none():
    sections = []
    assert RendererRST().render_copyright_header(sections) == ""


def test_render_copyright_header_one():
    sections = [{"type": "copyright", "args": ["bitcoin"]}]
    expected = """.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

"""
    assert RendererRST().render_copyright_header(sections) == expected


def test_render_copyright_header_two():
    sections = [{"type": "copyright", "args": ["bitcoin", "unit-e"]}]
    expected = """.. Copyright (c) 2014-2018 Bitcoin.org
   Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

"""
    assert RendererRST().render_copyright_header(sections) == expected


def test_auto_link_type():
    renderer = RendererRST()

    tests = [
        [
            "vector<Address>",
            r"vector_\<Address_>",
            {"vector", "Address"},
        ],
        [
            "uint32",
            "uint32_",
            {"uint32"},
        ],
        [
            "uint64",
            "uint64_",
            {"uint64"},
        ],
        [
            "CompactSize",
            "CompactSize_",
            {"CompactSize"},
        ],
        [
            "char[32]",
            r"char_\[32]",
            {"char"},
        ],
        [
            "uint256[]",
            r"uint256_\[]",
            {"uint256"},
        ],
        [
            "uint8[2]",
            r"uint8_\[2]",
            {"uint8"},
        ]
    ]

    for test in tests:
        renderer.clear()
        assert renderer.auto_link_type(test[0]) == test[1]
        assert renderer.link_targets == test[2]


def test_render_link_targets():
    renderer = RendererRST()

    tests = [
        [
            {},
            "",
        ],
        [
            {"CompactSize"},
            "\n.. _CompactSize: types/CompactSize.html\n",
        ],
        [
            {"int8"},
            "\n.. _int8: types/Integers.html\n",
        ],
        [
            {"uint64"},
            "\n.. _uint64: types/Integers.html\n",
        ],
        [
            {"uint64", "uint256"},
            "\n.. _uint256: types/Integers.html\n.. _uint64: types/Integers.html\n",
        ],
    ]

    for test in tests:
        renderer.link_targets = test[0]
        assert renderer.render_link_targets() == test[1]
