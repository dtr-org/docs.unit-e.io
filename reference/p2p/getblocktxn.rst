.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getblocktxn
-----------

Contains a BlockTransactionsRequest Peer should respond with "blocktxn" message.

Part of the compact blocks mechanism as described in `BIP-152 <https://github.com/bitcoin/bips/blob/master/bip-0152.mediawiki>`__.

The "getblocktxn" message is defined as a message containing a serialized `"BlockTransactionsRequest" message <BlockTransactionsRequest.html>`__. Upon receipt of a properly-formatted "getblocktxn" message, nodes which recently provided the sender of such a message a `"cmpctblock" message <cmpctblock.html>`__ for the block hash identified in this message must respond with either an appropriate `"blocktxn" message <blocktxn.html>`__, or a full block message.

A `"blocktxn" message <blocktxn.html>`__ response must contain exactly and only each transaction which is present in the appropriate block at the index specified in the "getblocktxn" message indexes list, in the order requested.

The structure of "BlockTransactionsRequest" is defined below.

+----------------+-----------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name           | Data Type       | Bytes    | Description                                                                                                                                                                                                                                                                                                                                                 |
+================+=================+==========+=============================================================================================================================================================================================================================================================================================================================================================+
| block hash     | uint256_        | 32       | The blockhash of the block which the transactions being requested are in.                                                                                                                                                                                                                                                                                   |
+----------------+-----------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| indexes length | CompactSize_    | *Varies* | The number of transactions being requested.                                                                                                                                                                                                                                                                                                                 |
+----------------+-----------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| indexes        | CompactSize_\[] | *Varies* | List of compactSize containing the indexes of the transactions being requested in the block, differently encoded as in the `PrefilledTransactions <types/PrefilledTransaction.html>`__. **In version 2 of compact blocks, the wtxid should be used instead of the txid** (see `BIP-141 <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>`__) |
+----------------+-----------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _CompactSize: types/CompactSize.html
.. _uint256: types/Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
