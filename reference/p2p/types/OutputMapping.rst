.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

OutputMapping
-------------


+-------+-----------+----------+---------------+
| Name  | Data Type | Bytes    | Description   |
+=======+===========+==========+===============+
| index | uint32_   | 4        | Output index  |
+-------+-----------+----------+---------------+
| txout | TxOut_    | *Varies* | Actual output |
+-------+-----------+----------+---------------+

.. _TxOut: TxOut.html
.. _uint32: Integers.html
