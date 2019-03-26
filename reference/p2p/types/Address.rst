.. Copyright (c) 2014-2018 Bitcoin.org
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

Address
-------

Network IP address of a peer.

+------------+------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name       | Data Type  | Bytes | Description                                                                                                                                                                                                                                                                      |
+============+============+=======+==================================================================================================================================================================================================================================================================================+
| services   | uint64_    | 8     | The services the node advertised in its `"version" message <../version.html>`__.                                                                                                                                                                                                 |
+------------+------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IP address | char_\[16] | 16    | IPv6 address in **big endian byte order**. IPv4 addresses can be provided as `IPv4-mapped IPv6 addresses <http://en.wikipedia.org/wiki/IPv6#IPv4-mapped_IPv6_addresses>`__                                                                                                       |
+------------+------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| port       | uint8_\[2] | 2     | Port number in **big endian byte order**. Note that Bitcoin Core will only connect to nodes with non-standard port numbers as a last resort for finding peers. This is to prevent anyone from trying to use the network to disrupt non-Unit-e  services that run on other ports. |
+------------+------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. highlight:: text

::

   0100000000000000 ................... Service bits: 01 ([network][network] node)
   00000000000000000000ffffc0000233 ... IP Address: ::ffff:192.0.2.51
   208d ............................... Port: 8333

.. _char: char.html
.. _uint64: Integers.html
.. _uint8: Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
