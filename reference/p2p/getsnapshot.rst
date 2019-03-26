.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getsnapshot
-----------

Contains the snapshot::GetSnapshot message. Peer should respond with the "snapshot" message.

This message is part of the snapshot mechanism as defined in `UIP-11 <https://github.com/dtr-org/uips/blob/master/UIP-0011.md>`__.

+-------------------+-----------+-------+--------------------------------------------+
| Name              | Data Type | Bytes | Description                                |
+===================+===========+=======+============================================+
| snapshot hash     | uint256_  | 32    | Hash of requested snapshot                 |
+-------------------+-----------+-------+--------------------------------------------+
| utxo subset index | uint64_   | 8     | Index of first UTXO subset in the snapshot |
+-------------------+-----------+-------+--------------------------------------------+
| utxo subset count | uint16_   | 2     | Number of UTXO subsets to return           |
+-------------------+-----------+-------+--------------------------------------------+

.. _uint16: types/Integers.html
.. _uint256: types/Integers.html
.. _uint64: types/Integers.html
