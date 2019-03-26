.. Copyright (c) 2014-2018 Bitcoin.org
   Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

PrefilledTransaction
--------------------


+-------+--------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name  | Data Type    | Bytes    | Description                                                                                                                                                                                                                              |
+=======+==============+==========+==========================================================================================================================================================================================================================================+
| index | CompactSize_ | *Varies* | The index into the block at which this transaction is located. Differentially encoded, i.e. the resulting index is calculated as effective_index = previous_index + index + 1. If it's the first index in the list it is taken as it is. |
+-------+--------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tx    | Transaction_ | *Varies* | The transaction which is in the block at the effective index.                                                                                                                                                                            |
+-------+--------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _CompactSize: CompactSize.html
.. _Transaction: Transaction.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
