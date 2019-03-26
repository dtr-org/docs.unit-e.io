.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getblocks
---------

The getblocks message requests an inv message that provides block header hashes starting from a particular point in the block chain. It allows a peer which has been disconnected or started for the first time to get the data it needs to request the blocks it hasn’t seen.

Peers which have been disconnected may have stale blocks in their locally-stored block chain, so the "getblocks" message allows the requesting peer to provide the receiving peer with multiple header hashes at various heights on their local chain. This allows the receiving peer to find, within that list, the last header hash they had in common and reply with all subsequent header hashes.

Note: the receiving peer itself may respond with an `"inv" message <inv.html>`__ containing header hashes of stale blocks. It is up to the requesting peer to poll all of its peers to find the best block chain.

If the receiving peer does not find a common header hash within the list, it will assume the last common block was the genesis block (block zero), so it will reply with in `"inv" message <inv.html>`__ containing header hashes starting with block one (the first block after the genesis block).

The `"getheaders" message <getheaders.html>`__ is nearly identical to the "getblocks" message, with one minor difference: the ``inv`` reply to the "getblocks" message will include no more than 500 block header hashes; the ``headers`` reply to the `"getheaders" message <getheaders.html>`__ will include as many as 2,000 block headers.

+---------------------+--------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                | Data Type    | Bytes    | Description                                                                                                                                                                                                                                                                                                                                                                      |
+=====================+==============+==========+==================================================================================================================================================================================================================================================================================================================================================================================+
| version             | uint32_      | 4        | The protocol version number; the same as sent in the `"version" message <version.html>`__.                                                                                                                                                                                                                                                                                       |
+---------------------+--------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hash count          | CompactSize_ | *Varies* | The number of header hashes provided not including the stop hash. There is no limit except that the byte size of the entire message must be below the `"MAX_SIZE" <https://github.com/bitcoin/bitcoin/blob/60abd463ac2eaa8bc1d616d8c07880dc53d97211/src/serialize.h#L23>`__ limit; typically from 1 to 200 hashes are sent.                                                      |
+---------------------+--------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| block header hashes | uint256_\[]  | *Varies* | One or more block header hashes (32 bytes each) in internal byte order. Hashes should be provided in reverse order of block height, so highest-height hashes are listed first and lowest-height hashes are listed last.                                                                                                                                                          |
+---------------------+--------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stop hash           | char_\[32]   | 32       | The header hash of the last header hash being requested; set to all zeroes to request an `"inv" message <inv.html>`__ with all subsequent header hashes (a maximum of 500 will be sent as a reply to this message; if you need more than 500, you will need to send another "getblocks" message with a higher-height header hash as the first entry in block header hash field). |
+---------------------+--------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The annotated hexdump below shows a `"getblocks" message <getblocks.html>`__. (The message header has been omitted.)

.. highlight:: text

::

   71110100 ........................... Protocol version: 70001
   02 ................................. Hash count: 2

   d39f608a7775b537729884d4e6633bb2
   105e55a16a14d31b0000000000000000 ... Hash #1

   5c3e6403d40837110a2e8afb602b1c01
   714bda7ce23bea0a0000000000000000 ... Hash #2

   00000000000000000000000000000000
   00000000000000000000000000000000 ... Stop hash

.. _CompactSize: types/CompactSize.html
.. _char: types/char.html
.. _uint256: types/Integers.html
.. _uint32: types/Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
