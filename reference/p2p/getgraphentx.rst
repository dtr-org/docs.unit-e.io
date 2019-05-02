.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getgraphentx
------------

Contains a p2p::GrapheneTxRequest Sent in response to "GRAPHENEBLOCK" message

This message is part of the Graphene block propagation protocol as defined in
`UIP-26 <https://github.com/dtr-org/uips/blob/master/UIP-0026.md>`__.

Used by the receiver to request any missing transactions after graphene block
was successfully decoded.

+-------------------------+-------------------+----------+-----------------------------------+
| Name                    | Data Type         | Bytes    | Description                       |
+=========================+===================+==========+===================================+
| block_hash              | uint256_          | 32       | Hash of the block being requested |
+-------------------------+-------------------+----------+-----------------------------------+
| missing_tx_short_hashes | vector_\<uint64_> | *Varies* | Set of short tx hashes            |
+-------------------------+-------------------+----------+-----------------------------------+

.. _uint256: types/Integers.html
.. _uint64: types/Integers.html
.. _vector: types/vector.html
