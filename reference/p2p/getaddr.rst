.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getaddr
-------

The getaddr message requests an addr message from the receiving node, preferably one with lots of IP addresses of other receiving nodes. The transmitting node can use those IP addresses to quickly update its database of available nodes rather than waiting for unsolicited `"addr" messages <addr.html>`__ to arrive over time.

There is no payload in a "getaddr" message. See the `message header section <intro.html#message-header>`__ for an example of a message without a payload.

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
