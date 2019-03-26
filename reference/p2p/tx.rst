.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

tx
--

The tx message transmits a single transaction. It is sent in the raw transaction format. It can be sent in a variety of situations;

-  **Transaction Response:** unit-e will send it in response to a `"getdata" message <getdata.html>`__ that requests the transaction with an inventory type of "MSG_TX".

-  **MerkleBlock Response:** unit-e will send it in response to a `"getdata" message <getdata.html>`__ that requests a merkle block with an inventory type of ``MSG_MERKLEBLOCK``. (This is in addition to sending a `"merkleblock" message <merkleblock.html>`__.) Each "tx" message in this case provides a matched transaction from that block.

+------+--------------+----------+-------------+
| Name | Data Type    | Bytes    | Description |
+======+==============+==========+=============+
| tx   | Transaction_ | *Varies* | Transaction |
+------+--------------+----------+-------------+

For an example hexdump of the raw transaction format, see the `raw transaction section <types/Transaction.html>`__.

.. _Transaction: types/Transaction.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
