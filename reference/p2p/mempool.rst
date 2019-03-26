.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

mempool
-------

The mempool message requests the TXIDs of transactions that the receiving node has verified as valid but which have not yet appeared in a block. That is, transactions which are in the receiving node’s memory pool. The response to the "mempool" message is one or more `"inv" messages <inv.html>`__ containing the TXIDs in the usual inventory format.

Sending the "mempool" message is mostly useful when a program first connects to the network. Full nodes can use it to quickly gather most or all of the unconfirmed transactions available on the network; this is especially useful for miners trying to gather transactions for their transaction fees. SPV clients can set a filter before sending a ``mempool`` to only receive transactions that match that filter; this allows a recently-started client to get most or all unconfirmed transactions related to its wallet.

An `"inv" message <inv.html>`__ is limited to 50,000 inventories. The node sends as many `"inv" messages <inv.html>`__ as needed to reference its complete memory pool.

The ``inv`` response to the "mempool" message is, at best, one node’s view of the network, not a complete list of unconfirmed transactions on the network. Here are some additional reasons the list might not be complete:

-  The "mempool" message is not currently fully compatible with the `"filterload" message <filterload.html>`__’s ``BLOOM_UPDATE_ALL`` and ``BLOOM_UPDATE_P2PUBKEY_ONLY`` flags. Mempool transactions are not sorted like in-block transactions, so a transaction (tx2) spending an output can appear before the transaction (tx1) containing that output, which means the automatic filter update mechanism won’t operate until the second-appearing transaction (tx1) is seen—missing the first-appearing transaction (tx2). It has been proposed in `Bitcoin Core issue #2381 <https://github.com/bitcoin/bitcoin/issues/2381>`__ that the transactions should be sorted before being processed by the filter.

There is no payload in a "mempool" message. See the `message header section <intro.html#message-header>`__ for an example of a message without a payload.

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
