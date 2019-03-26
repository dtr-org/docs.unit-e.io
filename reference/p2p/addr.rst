.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

addr
----

The addr (IP address) message relays connection information for peers on the network. Each peer which wants to accept incoming connections creates an "addr" message providing its connection information and then sends that message to its peers unsolicited. Some of its peers send that information to their peers (also unsolicited), some of which further distribute it, allowing decentralized peer discovery for any program already on the network.

An "addr" message may also be sent in response to a `"getaddr" message <getaddr.html>`__.

+--------------+----------------------------+----------+-------------------------------------------------------------+
| Name         | Data Type                  | Bytes    | Description                                                 |
+==============+============================+==========+=============================================================+
| IP addresses | vector_\<AddressWithTime_> | *Varies* | IP address entries. The maximum number of entries is 1,000. |
+--------------+----------------------------+----------+-------------------------------------------------------------+

The following annotated hexdump shows part of an "addr" message. (The message header has been omitted and the actual IP address has been replaced with a `RFC5737 <http://tools.ietf.org/html/rfc5737>`__ reserved IP address.)

.. highlight:: text

::

   01 ................................. Address count: 1

   d91f4854 ........................... [Epoch time][unix epoch time]: 1414012889
   0100000000000000 ................... Service bits: 01 ([network][network] node)
   00000000000000000000ffffc0000233 ... IP Address: ::ffff:192.0.2.51
   208d ............................... Port: 8333

.. _AddressWithTime: types/AddressWithTime.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
