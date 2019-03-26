.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

cmpctblock
----------

Contains a CBlockHeaderAndShortTxIDs object - providing a header and list of "short txids".

Part of the compact blocks mechanism as described in `BIP-152 <https://github.com/bitcoin/bips/blob/master/bip-0152.mediawiki>`__.

**Version 1 compact blocks are pre-segwit (txids), version 2 compact blocks are post-segwit (wtxids)**

The "cmpctblock" message is a reply to a `"getdata" message <getdata.html>`__ which requested a block using the inventory type "MSG_CMPCT_BLOCK". If the requested block was recently announced and is close to the tip of the best chain of the receiver and after having sent the requesting peer a `"sendcmpct" message <sendcmpct.html>`__, nodes respond with a "cmpctblock" message containing data for the block.

**If the requested block is too old, the node responds with a full non-compact block**

Upon receipt of a "cmpctblock" message, after sending a `"sendcmpct" message <sendcmpct.html>`__, nodes should calculate the short transaction ID for each unconfirmed transaction they have available (ie in their mempool) and compare each to each short transaction ID in the "cmpctblock" message. After finding already-available transactions, nodes which do not have all transactions available to reconstruct the full block should request the missing transactions using a `"getblocktxn" message <getblocktxn.html>`__.

A node must not send a "cmpctblock" message unless they are able to respond to a `"getblocktxn" message <getblocktxn.html>`__ which requests every transaction in the block. A node must not send a "cmpctblock" message without having validated that the header properly commits to each transaction in the block, and properly builds on top of the existing, fully-validated chain with a valid proof-of-work either as a part of the current most-work valid chain, or building directly on top of it. A node may send a "cmpctblock" message before validating that each transaction in the block validly spends existing UTXO set entries.

The "cmpctblock" message is used to relay a block header, the short transactions IDs used for matching already-available transactions, and a select few transactions which we expect a peer may be missing. It contains a vector of `"PrefilledTransaction" <types/PrefilledTransaction.html>`__.

+-----------------+---------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name            | Data Type                       | Bytes    | Description                                                                                                                                                                                                                                                                                                                                                                                   |
+=================+=================================+==========+===============================================================================================================================================================================================================================================================================================================================================================================================+
| block header    | BlockHeader_                    | 80       | The header of the block being provided.                                                                                                                                                                                                                                                                                                                                                       |
+-----------------+---------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nonce           | uint64_                         | 8        | A nonce for use in short transaction ID calculations.                                                                                                                                                                                                                                                                                                                                         |
+-----------------+---------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| shortids length | CompactSize_                    | *Varies* | The number of short transaction IDs in the following field.                                                                                                                                                                                                                                                                                                                                   |
+-----------------+---------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| shortids        | uint8_\[]                       | *Varies* | The short transaction IDs calculated from the transactions which were not provided explicitly in prefilledtxn. Vector of 6-byte integers in the spec, padded with two null-bytes so it can be read as an 8-byte integer. **In version 2 of compact blocks, shortids should use the wtxid instead of txid** (see `BIP-141 <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>`__) |
+-----------------+---------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| prefilled txn   | vector_\<PrefilledTransaction_> | *Varies* | Used to provide the coinbase transaction and a select few which we expect a peer may be missing. Vector of `"PrefilledTransaction" <types/PrefilledTransaction.html>`__ structures.                                                                                                                                                                                                           |
+-----------------+---------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Any undefined behavior in this spec may cause failure to transfer block to, peer disconnection by, or self-destruction by the receiving node. A node receiving non-minimally-encoded CompactSize encodings should make a best-effort to eat the sender’s cat.

As high-bandwidth mode permits relaying of "cmpctblock" messages prior to full validation (requiring only that the block header is valid before relay), nodes SHOULD NOT ban a peer for announcing a new block with a "cmpctblock" message that is invalid, but has a valid header.

**Version 2 compact blocks notes**

Transactions inside "cmpctblock" messages (both those used as direct announcement and those in response to getdata) and in `"blocktxn" messages <blocktxn.html>`__ should include witness data, using the same format as responses to getdata "MSG_WITNESS_TX", specified in `BIP-144 <https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki>`__.

Upon receipt of a `"getdata" message <getdata.html>`__ containing a request for a "MSG_CMPCT_BLOCK" object for which a "cmpctblock" message is not sent in response, the block message containing the requested block in non-compact form MUST be encoded with witnesses (as is sent in reply to a "MSG_WITNESS_BLOCK") if the protocol version used to encode the "cmpctblock" message would have been 2, and encoded without witnesses (as is sent in response to a "MSG_BLOCK") if the protocol version used to encode the "cmpctblock" message would have been 1.

**Short Transaction ID calculation**

Short transaction IDs are used to represent a transaction without sending a full 256-bit hash. They are calculated as follows,

-  A single-SHA256 hashing the block header with the nonce appended (in little-endian)
-  Running SipHash-2-4 with the input being the transaction ID (**wtxid in version 2 of compact blocks**) and the keys (k0/k1) set to the first two little-endian 64-bit integers from the above hash, respectively.
-  Dropping the 2 most significant bytes from the SipHash output to make it 6 bytes.
-  Two null-bytes appended so it can be read as an 8-byte integer.

.. _BlockHeader: types/BlockHeader.html
.. _CompactSize: types/CompactSize.html
.. _PrefilledTransaction: types/PrefilledTransaction.html
.. _uint64: types/Integers.html
.. _uint8: types/Integers.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
