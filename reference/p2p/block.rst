.. Copyright (c) 2014-2018 Bitcoin.org
   Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

block
-----

The block message transmits a single serialized block.

+--------------+------------------------+----------+--------------------+
| Name         | Data Type              | Bytes    | Description        |
+==============+========================+==========+====================+
| block header | BlockHeader_           | 80       | Block header       |
+--------------+------------------------+----------+--------------------+
| transactions | vector_\<Transaction_> | *Varies* | Block transactions |
+--------------+------------------------+----------+--------------------+

The "block" message can be sent for two different reasons:

1. **GetData Response:** Nodes will always send it in response to a `"getdata" message <getdata.html>`__ that requests the block with an inventory type of "MSG_BLOCK" (provided the node has that block available for relay).

2. **Unsolicited:** Some proposers will send unsolicited "block" messages broadcasting their newly-mined blocks to all of their peers.

.. _BlockHeader: types/BlockHeader.html
.. _Transaction: types/Transaction.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
