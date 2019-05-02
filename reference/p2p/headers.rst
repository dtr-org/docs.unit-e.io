.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

headers
-------

The headers message sends one or more block headers to a node which previously requested certain headers with a getheaders message. A headers message can be empty.

+---------+------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name    | Data Type              | Bytes    | Description                                                                                                                                                                                                                                                                                    |
+=========+========================+==========+================================================================================================================================================================================================================================================================================================+
| headers | vector_\<BlockHeader_> | *Varies* | Block headers: each 140-byte block header is in the format described in the `block headers section <types/BlockHeader.html>`__. Number of block headers up to a maximum of 2,000. Note: headers-first sync assumes the sending node will send the maximum number of headers whenever possible. |
+---------+------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The annotated hexdump below shows a `"headers" message <headers.html>`__. (The message header has been omitted.)

.. highlight:: text

::

   01 ................................. Header count: 1

   02000000 ........................... Block version: 2
   b6ff0b1b1680a2862a30ca44d346d9e8
   910d334beb48ca0c0000000000000000 ... Hash of previous block's header
   9d10aa52ee949386ca9385695f04ede2
   70dda20810decd12bc9b048aaab31471 ... Merkle root
   084c799cd551dd1d8d5c5f9a5d593b2e
   931f5e36122ee5c793c1d08a19839cc0 ... Witness Merkle root
   95d4c628d3aa681f4f0895281921b339
   4f61d7781e9861fba5ecb403311832f4 ... Finalizer commits Merkle root
   24d95a54 ........................... [Unix time][unix epoch time]: 1415239972
   30c31b18 ........................... Target (bits)

.. _BlockHeader: types/BlockHeader.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
