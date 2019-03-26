.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

filteradd
---------

The filteradd message tells the receiving peer to add a single element to a previously-set bloom filter, such as a new public key.

Part of the connection bloom filtering mechanism as described in `BIP-37 <https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki>`__.

The element is sent directly to the receiving peer; the peer then uses the parameters set in the `"filterload" message <filterload.html>`__ to add the element to the bloom filter.

Because the element is sent directly to the receiving peer, there is no obfuscation of the element and none of the plausible-deniability privacy provided by the bloom filter. Clients that want to maintain greater privacy should recalculate the bloom filter themselves and send a new `"filterload" message <filterload.html>`__ with the recalculated bloom filter.

+---------+------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name    | Data Type        | Bytes    | Description                                                                                                                                                                                                                                                                                                                        |
+=========+==================+==========+====================================================================================================================================================================================================================================================================================================================================+
| element | vector_\<uint8_> | *Varies* | The element to add to the current filter. Maximum of 520 bytes, which is the maximum size of an element which can be pushed onto the stack in a pubkey or signature script. Elements must be sent in the byte order they would use when appearing in a raw transaction; for example, hashes should be sent in internal byte order. |
+---------+------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note: a "filteradd" message will not be accepted unless a filter was previously set with the `"filterload" message <filterload.html>`__.

The annotated hexdump below shows a "filteradd" message adding a TXID. (The message header has been omitted.) This TXID appears in the same block used for the example hexdump in the `"merkleblock" message <merkleblock.html>`__; if that `"merkleblock" message <merkleblock.html>`__ is re-sent after sending this "filteradd" message, six hashes are returned instead of four.

.. highlight:: text

::

   20 ................................. Element bytes: 32
   fdacf9b3eb077412e7a968d2e4f11b9a
   9dee312d666187ed77ee7d26af16cb0b ... Element (A TXID)

.. _uint8: types/Integers.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
