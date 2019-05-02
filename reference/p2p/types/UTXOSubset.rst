.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

UTXOSubset
----------


+---------+--------------------------+----------+-------------------------------------------------+
| Name    | Data Type                | Bytes    | Description                                     |
+=========+==========================+==========+=================================================+
| tx id   | uint256_                 | 32       | Transaction hash                                |
+---------+--------------------------+----------+-------------------------------------------------+
| height  | uint32_                  | 4        | Block height where the transaction was included |
+---------+--------------------------+----------+-------------------------------------------------+
| type    | uint8_                   | 1        | Type of the transaction                         |
+---------+--------------------------+----------+-------------------------------------------------+
| outputs | vector_\<OutputMapping_> | *Varies* | Map of outputs this transaction contains        |
+---------+--------------------------+----------+-------------------------------------------------+

.. _OutputMapping: OutputMapping.html
.. _uint256: Integers.html
.. _uint32: Integers.html
.. _uint8: Integers.html
.. _vector: vector.html
