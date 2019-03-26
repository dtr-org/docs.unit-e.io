.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

filterclear
-----------

The filterclear message tells the receiving peer to remove a previously-set bloom filter.

Part of the connection bloom filtering mechanism as described in `BIP-37 <https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki>`__.

This also undoes the effect of setting the relay field in the `"version" message <version.html>`__ to 0, allowing unfiltered access to `"inv" messages <inv.html>`__ announcing new transactions.

unit-e does not require a "filterclear" message before a replacement filter is loaded with a `"filterload" message <filterload.html>`__. It also doesn’t require a `"filterload" message <filterload.html>`__ before a "filterclear" message.

There is no payload in a "filterclear" message. See the `message header section <intro.html#message-header>`__ for an example of a message without a payload.

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
