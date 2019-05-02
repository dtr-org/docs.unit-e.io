.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

BloomFilter
-----------


+------------+------------------+----------+--------------------------------------------------------------+
| Name       | Data Type        | Bytes    | Description                                                  |
+============+==================+==========+==============================================================+
| data       | vector_\<uint8_> | *Varies* | Filter data                                                  |
+------------+------------------+----------+--------------------------------------------------------------+
| hash_funcs | uint32_          | 4        | Number of hash functions                                     |
+------------+------------------+----------+--------------------------------------------------------------+
| tweak      | uint32_          | 4        | Constant added to the seed value passed to the hash function |
+------------+------------------+----------+--------------------------------------------------------------+
| flags      | uint8_           | 1        | Flags                                                        |
+------------+------------------+----------+--------------------------------------------------------------+

.. _uint32: Integers.html
.. _uint8: Integers.html
.. _vector: vector.html
