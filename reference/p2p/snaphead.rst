.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

snaphead
--------

Contains the snapshot::SnapshotHeader message. Sent in response to a "getsnaphead" message.

This message is part of the snapshot mechanism as defined in `UIP-11 <https://github.com/dtr-org/uips/blob/master/UIP-0011.md>`__.

+--------------------+-----------+-------+---------------------------------------------------------------+
| Name               | Data Type | Bytes | Description                                                   |
+====================+===========+=======+===============================================================+
| snapshot hash      | uint256_  | 32    | Snapshot hash                                                 |
+--------------------+-----------+-------+---------------------------------------------------------------+
| block hash         | uint256_  | 32    | Hash of block at which the snapshot was created               |
+--------------------+-----------+-------+---------------------------------------------------------------+
| stake modifier     | uint256_  | 32    | Stake modifier of the block at which the snapshot was created |
+--------------------+-----------+-------+---------------------------------------------------------------+
| chain work         | uint256_  | 32    | Chain work                                                    |
+--------------------+-----------+-------+---------------------------------------------------------------+
| total utxo subsets | uint64_   | 8     | Total UTXO subsets in snapshot                                |
+--------------------+-----------+-------+---------------------------------------------------------------+

.. _uint256: types/Integers.html
.. _uint64: types/Integers.html
