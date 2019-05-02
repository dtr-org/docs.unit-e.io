.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

graphenetx
----------

Contains a p2p::GrapheneTx Sent in response to "GETGRAPHENETX" message

This message is part of the Graphene block propagation protocol as defined in
`UIP-26 <https://github.com/dtr-org/uips/blob/master/UIP-0026.md>`__.

+------------+------------------------+----------+-----------------------------------+
| Name       | Data Type              | Bytes    | Description                       |
+============+========================+==========+===================================+
| block_hash | uint256_               | 32       | Hash of the block being requested |
+------------+------------------------+----------+-----------------------------------+
| txs        | vector_\<Transaction_> | *Varies* | List of full transactions         |
+------------+------------------------+----------+-----------------------------------+

.. _Transaction: types/Transaction.html
.. _uint256: types/Integers.html
.. _vector: types/vector.html
