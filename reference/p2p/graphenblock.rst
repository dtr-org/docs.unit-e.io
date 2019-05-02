.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

graphenblock
------------

Contains a p2p::GrapheneBlock Sent in response to "GETGRAPHENE" message

This message is part of the Graphene block propagation protocol as defined in
`UIP-26 <https://github.com/dtr-org/uips/blob/master/UIP-0026.md>`__.

+------------------------+------------------------+----------+----------------------------------------------------------------+
| Name                   | Data Type              | Bytes    | Description                                                    |
+========================+========================+==========+================================================================+
| header                 | BlockHeader_           | 140      | Block header                                                   |
+------------------------+------------------------+----------+----------------------------------------------------------------+
| nonce                  | uint64_                | 8        | Nonce used for computing short tx hashes                       |
+------------------------+------------------------+----------+----------------------------------------------------------------+
| bloom filter           | BloomFilter_           | *Varies* | Bloom filter                                                   |
+------------------------+------------------------+----------+----------------------------------------------------------------+
| IBLT                   | GrapheneIblt_          | *Varies* | Invertible bloom lookup table                                  |
+------------------------+------------------------+----------+----------------------------------------------------------------+
| prefilled transactions | vector_\<Transaction_> | *Varies* | Transactions the sender expect the receiver to not be aware of |
+------------------------+------------------------+----------+----------------------------------------------------------------+

.. _BlockHeader: types/BlockHeader.html
.. _BloomFilter: types/BloomFilter.html
.. _GrapheneIblt: types/GrapheneIblt.html
.. _Transaction: types/Transaction.html
.. _uint64: types/Integers.html
.. _vector: types/vector.html
