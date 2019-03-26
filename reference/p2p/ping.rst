.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

ping
----

The ping message is sent periodically to help confirm that the receiving peer is still connected. If a TCP/IP error is encountered when sending the "ping" message (such as a connection timeout), the transmitting node can assume that the receiving node is disconnected. The response to a "ping" message is the `"pong" message <pong.html>`__.

The message includes a single field, the nonce.

+-------+-----------+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name  | Data Type | Bytes | Description                                                                                                                                                                                                                                                              |
+=======+===========+=======+==========================================================================================================================================================================================================================================================================+
| nonce | uint64_   | 8     | Random nonce assigned to this "ping" message. The responding `"pong" message <pong.html>`__ will include this nonce to identify the "ping" message to which it is replying. See `BIP-31 <https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki>`__ for details. |
+-------+-----------+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The annotated hexdump below shows a `"ping" message <ping.html>`__. (The message header has been omitted.)

.. highlight:: text

::

   0094102111e2af4d ... Nonce

.. _uint64: types/Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
