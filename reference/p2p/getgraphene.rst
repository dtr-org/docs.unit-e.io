.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getgraphene
-----------

Contains a p2p::GrapheneBlockRequest Sent in response "headers" message

This message is part of the Graphene block propagation protocol as defined in
`UIP-26 <https://github.com/dtr-org/uips/blob/master/UIP-0026.md>`__.

+-------------------------+-----------+-------+---------------------------------------------+
| Name                    | Data Type | Bytes | Description                                 |
+=========================+===========+=======+=============================================+
| requested block hash    | uint256_  | 32    | Hash of the block being requested           |
+-------------------------+-----------+-------+---------------------------------------------+
| requester mempool count | uint64_   | 8     | Number of transactions in receiver's txpool |
+-------------------------+-----------+-------+---------------------------------------------+

.. _uint256: types/Integers.html
.. _uint64: types/Integers.html
