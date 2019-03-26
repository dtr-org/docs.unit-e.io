.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

reject
------

The reject message informs the receiving node that one of its previous messages has been rejected.

+------------+-----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name       | Data Type | Bytes    | Description                                                                                                                                                                                                                                    |
+============+===========+==========+================================================================================================================================================================================================================================================+
| message    | string_   | *Varies* | The type of message rejected as ASCII text *without null padding*. For example: “tx”, “block”, or “version”.                                                                                                                                   |
+------------+-----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| code       | char_     | 1        | The reject message code. See the table below.                                                                                                                                                                                                  |
+------------+-----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reason     | string_   | *Varies* | The reason for the rejection in ASCII text. This should not be displayed to the user; it is only for debugging purposes. May be an empty string.                                                                                               |
+------------+-----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| extra data | uint256_  | 32       | Optional additional data provided with the rejection. For example, most rejections of `"tx" messages <tx.html>`__ or `"block" messages <block.html>`__ include the hash of the rejected transaction or block header. See the code table below. |
+------------+-----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following table lists message reject codes. Codes are tied to the type of message they reply to; for example there is a 0x10 reject code for transactions and a 0x10 reject code for blocks.

+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Code | In Reply To                          | Extra Bytes | Extra Type | Description                                                                                                                                                                                                    |
+======+======================================+=============+============+================================================================================================================================================================================================================+
| 0x01 | *any message*                        | 0           | N/A        | Message could not be decoded. Be careful of "reject" message feedback loops where two peers each don’t understand each other’s "reject" messages and so keep sending them back and forth forever.              |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x10 | `"block" message <block.html>`__     | 32          | uint256    | Block is invalid for some reason (invalid proof-of-work, invalid signature, etc). Extra data may include the rejected block’s header hash.                                                                     |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x10 | `"tx" message <tx.html>`__           | 32          | uint256    | Transaction is invalid for some reason (invalid signature, output value greater than input, etc.). Extra data may include the rejected transaction’s TXID.                                                     |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x11 | `"block" message <block.html>`__     | 32          | uint256    | The block uses a version that is no longer supported. Extra data may include the rejected block’s header hash.                                                                                                 |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x11 | `"version" message <version.html>`__ | 0           | N/A        | Connecting node is using a protocol version that the rejecting node considers obsolete and unsupported.                                                                                                        |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x12 | `"tx" message <tx.html>`__           | 32          | uint256    | Duplicate input spend (double spend): the rejected transaction spends the same input as a previously-received transaction. Extra data may include the rejected transaction’s TXID.                             |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x12 | `"version" message <version.html>`__ | 0           | N/A        | More than one `"version" message <version.html>`__ received in this connection.                                                                                                                                |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x40 | `"tx" message <tx.html>`__           | 32          | uint256    | The transaction will not be mined or relayed because the rejecting node considers it non-standard—a transaction type or version unknown by the server. Extra data may include the rejected transaction’s TXID. |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x41 | `"tx" message <tx.html>`__           | 32          | uint256    | One or more output amounts are below the dust threshold. Extra data may include the rejected transaction’s TXID.                                                                                               |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x42 | `"tx" message <tx.html>`__           | 32          | uint256    | The transaction did not have a large enough fee or priority to be relayed or mined. Extra data may include the rejected transaction’s TXID.                                                                    |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x43 | `"block" message <block.html>`__     | 32          | uint256    | The block belongs to a block chain which is not the same block chain as provided by a compiled-in checkpoint. Extra data may include the rejected block’s header hash.                                         |
+------+--------------------------------------+-------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The annotated hexdump below shows a `"reject" message <reject.html>`__. (The message header has been omitted.)

.. highlight:: text

::

   02 ................................. Number of bytes in message: 2
   7478 ............................... Type of message rejected: tx
   12 ................................. Reject code: 0x12 (duplicate)
   15 ................................. Number of bytes in reason: 21
   6261642d74786e732d696e707574732d
   7370656e74 ......................... Reason: bad-txns-inputs-spent
   394715fcab51093be7bfca5a31005972
   947baf86a31017939575fb2354222821 ... TXID

.. _char: types/char.html
.. _string: types/string.html
.. _uint256: types/Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
