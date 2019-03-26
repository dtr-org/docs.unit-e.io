.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getdata
-------

The getdata message requests one or more data objects from another node. The objects are requested by an inventory, which the requesting node typically received previously by way of an `"inv" message <inv.html>`__.

The response to a "getdata" message can be a `"tx" message <tx.html>`__, `"block" message <block.html>`__, `"merkleblock" message <merkleblock.html>`__, `"cmpctblock" message <cmpctblock.html>`__, or `"notfound" message <notfound.html>`__.

This message cannot be used to request arbitrary data, such as historic transactions no longer in the memory pool or relay set. Full nodes may not even be able to provide older blocks if they’ve pruned old transactions from their block database. For this reason, the "getdata" message should usually only be used to request data from a node which previously advertised it had that data by sending an `"inv" message <inv.html>`__.

The format and maximum size limitations of the "getdata" message are identical to the `"inv" message <inv.html>`__; only the message header differs.

+-----------+----------------+----------+------------------------------------------------------------------+
| Name      | Data Type      | Bytes    | Description                                                      |
+===========+================+==========+==================================================================+
| inventory | vector_\<Inv_> | *Varies* | One or more inventory entries up to a maximum of 50,000 entries. |
+-----------+----------------+----------+------------------------------------------------------------------+

.. _Inv: types/Inv.html
.. _vector: types/vector.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
