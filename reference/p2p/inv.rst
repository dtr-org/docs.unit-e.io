.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

inv
---

The inv message (inventory message) transmits one or more inventories of objects known to the transmitting peer. It can be sent unsolicited to announce new transactions or blocks, or it can be sent in reply to a `"getblocks" message <getblocks.html>`__ or `"mempool" message <mempool.html>`__.

The receiving peer can compare the inventories from an "inv" message against the inventories it has already seen, and then use a follow-up message to request unseen objects.

+-----------+----------------+----------+------------------------------------------------------------------+
| Name      | Data Type      | Bytes    | Description                                                      |
+===========+================+==========+==================================================================+
| inventory | vector_\<Inv_> | *Varies* | One or more inventory entries up to a maximum of 50,000 entries. |
+-----------+----------------+----------+------------------------------------------------------------------+

The following annotated hexdump shows an "inv" message with two inventory entries. (The message header has been omitted.)

.. highlight:: text

::

   02 ................................. Count: 2

   01000000 ........................... Type: MSG_TX
   de55ffd709ac1f5dc509a0925d0b1fc4
   42ca034f224732e429081da1b621f55a ... Hash (TXID)

   01000000 ........................... Type: MSG_TX
   91d36d997037e08018262978766f24b8
   a055aaf1d872e94ae85e9817b2c68dc7 ... Hash (TXID)

.. _Inv: types/Inv.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
