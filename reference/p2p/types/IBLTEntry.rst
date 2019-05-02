.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

IBLTEntry
---------


+-----------+--------------+----------+-------------------------------------------------+
| Name      | Data Type    | Bytes    | Description                                     |
+===========+==============+==========+=================================================+
| count     | CompactSize_ | *Varies* | How many times key hash resolved to this bucket |
+-----------+--------------+----------+-------------------------------------------------+
| key sum   | uint64_      | 8        | Xor of all keys for this bucket                 |
+-----------+--------------+----------+-------------------------------------------------+
| key check | uint32_      | 4        | Xor of all key checksums                        |
+-----------+--------------+----------+-------------------------------------------------+

.. _CompactSize: CompactSize.html
.. _uint32: Integers.html
.. _uint64: Integers.html
