.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

notfound
--------

The notfound message is a reply to a getdata message which requested an object the receiving node does not have available for relay. (Nodes are not expected to relay historic transactions which are no longer in the memory pool or relay set. Nodes may also have pruned spent transactions from older blocks, making them unable to send those blocks.)

The format and maximum size limitations of the "notfound" message are identical to the `"inv" message <inv.html>`__; only the message header differs.

+-----------+----------------+----------+------------------------------------------------------------------+
| Name      | Data Type      | Bytes    | Description                                                      |
+===========+================+==========+==================================================================+
| inventory | vector_\<Inv_> | *Varies* | One or more inventory entries up to a maximum of 50,000 entries. |
+-----------+----------------+----------+------------------------------------------------------------------+

.. _Inv: types/Inv.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
