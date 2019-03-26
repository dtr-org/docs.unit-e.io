.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

merkleblock
-----------

The merkleblock message is a reply to a getdata message which requested a block using the inventory type MSG_MERKLEBLOCK. It is only part of the reply: if any matching transactions are found, they will be sent separately as `"tx" messages <tx.html>`__.

If a filter has been previously set with the `"filterload" message <filterload.html>`__, the "merkleblock" message will contain the TXIDs of any transactions in the requested block that matched the filter, as well as any parts of the block’s merkle tree necessary to connect those transactions to the block header’s merkle root. The message also contains a complete copy of the block header to allow the client to hash it and confirm its proof of work.

+-------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name              | Data Type    | Bytes    | Description                                                                                                                                                                                                                                                   |
+===================+==============+==========+===============================================================================================================================================================================================================================================================+
| block header      | BlockHeader_ | 80       | The block header in the format described in the `block header section <types/BlockHeader.html>`__.                                                                                                                                                            |
+-------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| transaction count | uint32_      | 4        | The number of transactions in the block (including ones that don’t match the filter).                                                                                                                                                                         |
+-------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hash count        | CompactSize_ | *Varies* | The number of hashes in the following field.                                                                                                                                                                                                                  |
+-------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hashes            | uint256_\[]  | *Varies* | One or more hashes of both transactions and merkle nodes in internal byte order. Each hash is 32 bytes.                                                                                                                                                       |
+-------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| flag byte count   | CompactSize_ | *Varies* | The number of flag bytes in the following field.                                                                                                                                                                                                              |
+-------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| flags             | uint8_\[]    | *Varies* | A sequence of bits packed eight in a byte with the least significant bit first. May be padded to the nearest byte boundary but must not contain any more bits than that. Used to assign the hashes to particular nodes in the merkle tree as described below. |
+-------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The annotated hexdump below shows a "merkleblock" message which corresponds to the examples below. (The message header has been omitted.)

.. highlight:: text

::

   01000000 ........................... Block version: 1
   82bb869cf3a793432a66e826e05a6fc3
   7469f8efb7421dc88067010000000000 ... Hash of previous block's header
   7f16c5962e8bd963659c793ce370d95f
   093bc7e367117b3c30c1f8fdd0d97287 ... Merkle root
   76381b4d ........................... Time: 1293629558
   4c86041b ........................... nBits: 0x04864c * 256**(0x1b-3)
   554b8529 ........................... Nonce

   07000000 ........................... Transaction count: 7
   04 ................................. Hash count: 4

   3612262624047ee87660be1a707519a4
   43b1c1ce3d248cbfc6c15870f6c5daa2 ... Hash #1
   019f5b01d4195ecbc9398fbf3c3b1fa9
   bb3183301d7a1fb3bd174fcfa40a2b65 ... Hash #2
   41ed70551dd7e841883ab8f0b16bf041
   76b7d1480e4f0af9f3d4c3595768d068 ... Hash #3
   20d2a7bc994987302e5b1ac80fc425fe
   25f8b63169ea78e68fbaaefa59379bbf ... Hash #4

   01 ................................. Flag bytes: 1
   1d ................................. Flags: 1 0 1 1 1 0 0 0

Note: when fully decoded, the above "merkleblock" message provided the TXID for a single transaction that matched the filter. In the network traffic dump this output was taken from, the full transaction belonging to that TXID was sent immediately after the "merkleblock" message as a `"tx" message <tx.html>`__.

Parsing A MerkleBlock Message
'''''''''''''''''''''''''''''

As seen in the annotated hexdump above, the "merkleblock" message provides three special data types: a transaction count, a list of hashes, and a list of one-bit flags.

You can use the transaction count to construct an empty merkle tree. We’ll call each entry in the tree a node; on the bottom are TXID nodes—the hashes for these nodes are TXIDs; the remaining nodes (including the merkle root) are non-TXID nodes—they may actually have the same hash as a TXID, but we treat them differently.

.. figure:: /img/dev/animated-en-merkleblock-parsing.gif
   :alt: Example Of Parsing A MerkleBlock Message

   Example Of Parsing A MerkleBlock Message

Keep the hashes and flags in the order they appear in the "merkleblock" message. When we say “next flag” or “next hash”, we mean the next flag or hash on the list, even if it’s the first one we’ve used so far.

Start with the merkle root node and the first flag. The table below describes how to evaluate a flag based on whether the node being processed is a TXID node or a non-TXID node. Once you apply a flag to a node, never apply another flag to that same node or reuse that same flag again.

+-------+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Flag  | TXID Node                                                                                | Non-TXID Node                                                                                                                                                                                                    |
+=======+==========================================================================================+==================================================================================================================================================================================================================+
| **0** | Use the next hash as this node’s TXID, but this transaction didn’t match the filter.     | Use the next hash as this node’s hash. Don’t process any descendant nodes.                                                                                                                                       |
+-------+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **1** | Use the next hash as this node’s TXID, and mark this transaction as matching the filter. | The hash needs to be computed. Process the left child node to get its hash; process the right child node to get its hash; then concatenate the two hashes as 64 raw bytes and hash them to get this node’s hash. |
+-------+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Any time you begin processing a node for the first time, evaluate the next flag. Never use a flag at any other time.

When processing a child node, you may need to process its children (the grandchildren of the original node) or further-descended nodes before returning to the parent node. This is expected—keep processing depth first until you reach a TXID node or a non-TXID node with a flag of 0.

After you process a TXID node or a non-TXID node with a flag of 0, stop processing flags and begin to ascend the tree. As you ascend, compute the hash of any nodes for which you now have both child hashes or for which you now have the sole child hash. See the `merkle tree section <intro.html#merkle-trees>`__ for hashing instructions. If you reach a node where only the left hash is known, descend into its right child (if present) and further descendants as necessary.

However, if you find a node whose left and right children both have the same hash, fail. This is related to `CVE-2012-2459 <http://cve.mitre.org/cgi-bin/cvename.cgi?name=2012-2459>`__.

Continue descending and ascending until you have enough information to obtain the hash of the merkle root node. If you run out of flags or hashes before that condition is reached, fail. Then perform the following checks (order doesn’t matter):

-  Fail if there are unused hashes in the hashes list.

-  Fail if there are unused flag bits—except for the minimum number of bits necessary to pad up to the next full byte.

-  Fail if the hash of the merkle root node is not identical to the merkle root in the block header.

-  Fail if the block header is invalid. Remember to ensure that the hash of the header is less than or equal to the target threshold encoded by the nBits header field. Your program should also, of course, attempt to ensure the header belongs to the best block chain and that the user knows how many confirmations this block has.

For a detailed example of parsing a "merkleblock" message, please see the corresponding merkle block examples section.

Creating A MerkleBlock Message
''''''''''''''''''''''''''''''

It’s easier to understand how to create a "merkleblock" message after you understand how to parse an already-created message, so we recommend you read the parsing section above first.

Create a complete merkle tree with TXIDs on the bottom row and all the other hashes calculated up to the merkle root on the top row. For each transaction that matches the filter, track its TXID node and all of its ancestor nodes.

.. figure:: /img/dev/animated-en-merkleblock-creation.gif
   :alt: Example Of Creating A MerkleBlock Message

   Example Of Creating A MerkleBlock Message

Start processing the tree with the merkle root node. The table below describes how to process both TXID nodes and non-TXID nodes based on whether the node is a match, a match ancestor, or neither a match nor a match ancestor.

+--------------------------------------+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Condition                            | TXID Node                                                              | Non-TXID Node                                                                                                                                                                |
+======================================+========================================================================+==============================================================================================================================================================================+
| **Neither Match Nor Match Ancestor** | Append a 0 to the flag list; append this node’s TXID to the hash list. | Append a 0 to the flag list; append this node’s hash to the hash list. Do not descend into its child nodes.                                                                  |
+--------------------------------------+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Match Or Match Ancestor**          | Append a 1 to the flag list; append this node’s TXID to the hash list. | Append a 1 to the flag list; process the left child node. Then, if the node has a right child, process the right child. Do not append a hash to the hash list for this node. |
+--------------------------------------+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Any time you begin processing a node for the first time, a flag should be appended to the flag list. Never put a flag on the list at any other time, except when processing is complete to pad out the flag list to a byte boundary.

When processing a child node, you may need to process its children (the grandchildren of the original node) or further-descended nodes before returning to the parent node. This is expected—keep processing depth first until you reach a TXID node or a node which is neither a TXID nor a match ancestor.

After you process a TXID node or a node which is neither a TXID nor a match ancestor, stop processing and begin to ascend the tree until you find a node with a right child you haven’t processed yet. Descend into that right child and process it.

After you fully process the merkle root node according to the instructions in the table above, processing is complete. Pad your flag list to a byte boundary and construct the "merkleblock" message using the template near the beginning of this subsection.

.. _BlockHeader: types/BlockHeader.html
.. _CompactSize: types/CompactSize.html
.. _uint256: types/Integers.html
.. _uint32: types/Integers.html
.. _uint8: types/Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
