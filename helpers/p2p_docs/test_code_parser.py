# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from code_parser import CodeParser


def test_parse_code():
    parser = CodeParser("test_data/unit-e")
    messages = parser.parse()
    assert len(messages) == 4

    msg = messages["VERSION"]
    assert msg["name"] == "version"
    assert msg["text"] == ("The version message provides information about the transmitting node to the "
                           + "receiving node at the beginning of a connection.")
    assert "since" not in msg

    msg = messages["MERKLEBLOCK"]
    assert msg["name"] == "merkleblock"
    assert msg["text"] == ("The merkleblock message is a reply to a getdata message which requested a "
                           + "block using the inventory type MSG_MERKLEBLOCK.")
    assert msg["since"] == "protocol version 70001 as described by BIP37"

    msg = messages["FILTERLOAD"]
    assert msg["name"] == "filterload"
    assert msg["text"] == ("The filterload message tells the receiving peer to filter all relayed "
                           + "transactions and requested merkle blocks through the provided filter.")
    assert msg["since"] == "protocol version 70001 as described by BIP37"
    assert msg["since_note"] == ("Only available with service bit NODE_BLOOM since protocol version "
                                 + "70011 as described by BIP111.")

    msg = messages["GETSNAPSHOTHEADER"]
    assert msg["name"] == "getsnaphead"
    assert msg["text"] == ('Contains the snapshot::GetSnapshotHeader message. '
                           + 'Peer should respond with the "snaphead" message.')
    assert "since" not in msg
    assert "since_note" not in msg
