.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

pong
----

The pong message replies to a ping message, proving to the pinging node that the ponging node is still alive. unit-e will, by default, disconnect from any clients which have not responded to a `"ping" message <ping.html>`__ within 20 minutes.

To allow nodes to keep track of latency, the "pong" message sends back the same nonce received in the `"ping" message <ping.html>`__ it is replying to.

The format of the "pong" message is identical to the `"ping" message <ping.html>`__; only the message header differs.

+-------+-----------+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name  | Data Type | Bytes | Description                                                                                                                                                                                                                                                                              |
+=======+===========+=======+==========================================================================================================================================================================================================================================================================================+
| nonce | uint64_   | 8     | Random nonce assigned to this `"ping" message <ping.html>`__. The responding "pong" message will include this nonce to identify the `"ping" message <ping.html>`__ to which it is replying. See `BIP-31 <https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki>`__ for details. |
+-------+-----------+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uint64: types/Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
