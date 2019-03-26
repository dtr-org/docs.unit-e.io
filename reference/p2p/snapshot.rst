.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

snapshot
--------

Contains the snapshot::Snapshot object Sent in response to a "getsnapshot" message.

This message is part of the snapshot mechanism as defined in `UIP-11 <https://github.com/dtr-org/uips/blob/master/UIP-0011.md>`__.

+-------------------+-----------------------+----------+--------------------------------------------+
| Name              | Data Type             | Bytes    | Description                                |
+===================+=======================+==========+============================================+
| snapshot hash     | uint256_              | 32       | Snapshot hash                              |
+-------------------+-----------------------+----------+--------------------------------------------+
| utxo subset index | uint64_               | 8        | index of first UTXO subset in the snapshot |
+-------------------+-----------------------+----------+--------------------------------------------+
| utxo subsets      | vector_\<UTXOSubset_> | *Varies* | UTXO subsets and their outputs             |
+-------------------+-----------------------+----------+--------------------------------------------+

.. highlight:: text

::

   d9cd8155764c3543f10fad8a480d7431
   37466f8d55213c8eaefcd12f06d43a80 ... Snapshot hash
   1122334455667788 ................... UTXO subset index

   01 ................................. Size of UTXO list

   d2387e70b5a084f4efdcd732bb2710ec
   28d48db38ecd38510ccab8877e4b7bd7 ... Hash of transaction
   07000000 ........................... Block height where transaction was included, 0x7 (7)
   00 ................................. False, no coinbase transaction

   01 ................................. Size of output list

   02000000 ........................... Output index
   2a00000000000000 ................... Value, 0x2a (42)

   03 ................................. Size of script
   123456 ............................. Script (dummy data)

.. _UTXOSubset: types/UTXOSubset.html
.. _uint256: types/Integers.html
.. _uint64: types/Integers.html
.. _vector: types/vector.html
