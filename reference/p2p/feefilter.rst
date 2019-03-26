.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

feefilter
---------

The feefilter message tells the receiving peer not to inv us any txs which do not meet the specified min fee rate.

Mempool limiting provides protection against attacks and spam transactions that have low fee rates and are unlikely to be included in mined blocks. The "feefilter" messages allows a node to inform its peers that it will not accept transactions below a specified fee rate into its mempool, and therefore that the peers can skip relaying inv messages for transactions below that fee rate to that node.

+---------+-----------+-------+------------------------------------------------------------------------------------------------------+
| Name    | Data Type | Bytes | Description                                                                                          |
+=========+===========+=======+======================================================================================================+
| feerate | uint64_   | 8     | The fee rate (in satoshis per kilobyte) below which transactions should not be relayed to this peer. |
+---------+-----------+-------+------------------------------------------------------------------------------------------------------+

The receiving peer may choose to ignore the message and not filter transaction inv messages.

The fee filter is additive with bloom filters. If an SPV client loads a bloom filter and sends a feefilter message, transactions should only be relayed if they pass both filters.

Note however that feefilter has no effect on block propagation or responses to getdata messages. For example, if a node requests a merkleblock from its peer by sending a getdata message with inv type MSG_FILTERED_BLOCK and it has previously sent a feefilter to that peer, the peer should respond with a merkleblock containing *all* the transactions matching the bloom filter, even if they are below the feefilter fee rate.

inv messages generated from a mempool message are subject to a fee filter if it exists.

The annotated hexdump below shows a `"feefilter" message <feefilter.html>`__. (The message header has been omitted.)

.. highlight:: text

::

   7cbd000000000000 ... satoshis per kilobyte: 48,508

.. _uint64: types/Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
