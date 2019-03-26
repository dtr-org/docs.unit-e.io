.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

blocktxn
--------

Contains a BlockTransactions. Sent in response to a "getblocktxn" message.

Part of the compact blocks mechanism as described in `BIP-152 <https://github.com/bitcoin/bips/blob/master/bip-0152.mediawiki>`__.

Upon receipt of a properly-formatted requested "blocktxn" message, nodes should attempt to reconstruct the full block by taking the prefilledtxn transactions from the original `"cmpctblock" message <cmpctblock.html>`__ and placing them in the marked positions, then for each short transaction ID from the original `"cmpctblock" message <cmpctblock.html>`__, in order, find the corresponding transaction either from the "blocktxn" message or from other sources and place it in the first available position in the block then once the block has been reconstructed, it shall be processed as normal, keeping in mind that short transaction IDs are expected to occasionally collide, and that nodes must not be penalized for such collisions, wherever they appear.

+--------------+------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Name         | Data Type              | Bytes    | Description                                                                                                                                 |
+==============+========================+==========+=============================================================================================================================================+
| block hash   | uint256_               | 32       | The blockhash of the block which the transactions being provided are in.                                                                    |
+--------------+------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------+
| transactions | vector_\<Transaction_> | *Varies* | Vector of transactions, for an example hexdump of the raw transaction format, see the `raw transaction section <types/Transaction.html>`__. |
+--------------+------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------+

.. _Transaction: types/Transaction.html
.. _uint256: types/Integers.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
