Each peer which wants to accept incoming connections creates an `"addr" message <addr.html>`__ providing its connection information and then sends that message to its peers unsolicited. Some of its peers send that information to their peers (also unsolicited), some of which further distribute it, allowing decentralized peer discovery for any program already on the `network </en/developer-guide#term-network>`__.

An `"addr" message <addr.html>`__ may also be sent in response to a `"getaddr" message <getaddr.html>`__.

**TODO: example for a todo entry**

+--------------+--------------------+----------+-------------------------------------------------------------+
| Name         | Data Type          | Bytes    | Description                                                 |
+==============+====================+==========+=============================================================+
| IP addresses | vector_\<Address_> | *Varies* | IP address entries. The maximum number of entries is 1,000. |
+--------------+--------------------+----------+-------------------------------------------------------------+

Each encapsulated `network </en/developer-guide#term-network>`__ IP address currently uses the following structure:

+------------+------------+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name       | Data Type  | Bytes | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+============+============+=======+===================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| time       | uint32_    | 4     | *Added in*\ `protocol version 31402 </en/developer-reference#protocol-versions>`__\ *.* A time in `Unix epoch time <https://en.wikipedia.org/wiki/Unix_time>`__ format. Nodes advertising their own IP address set this to the current time. Nodes advertising IP addresses they’ve connected to set this to the last time they connected to that node. Other nodes just relaying the IP address should not change the time. Nodes can use the time field to avoid relaying old `"addr" messages <addr.html>`__. Malicious nodes may change times or even set them in the future. |
+------------+------------+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| services   | uint64_    | 8     | The services the node advertised in its `"version" message <version.html>`__.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+------------+------------+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IP address | char_\[16] | 16    | IPv6 address in **big endian byte order**. IPv4 addresses can be provided as `IPv4-mapped IPv6 addresses <http://en.wikipedia.org/wiki/IPv6#IPv4-mapped_IPv6_addresses>`__                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------+------------+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| port       | uint16_    | 2     | Port number in **big endian byte order**. Note that Bitcoin Core will only connect to nodes with non-standard port numbers as a last resort for finding peers. This is to prevent anyone from trying to use the `network </en/developer-guide#term-network>`__ to disrupt non-Unit-e  services that run on other ports.                                                                                                                                                                                                                                                           |
+------------+------------+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. figure:: /img/dev/en-bloom-update.svg
   :alt: Automatically Updating Bloom Filters

   Automatically Updating Bloom Filters

The following annotated hexdump shows part of an `"addr" message <addr.html>`__. (The message header has been omitted and the actual IP address has been replaced with a `RFC5737 <http://tools.ietf.org/html/rfc5737>`__ reserved IP address.)

.. highlight:: text

::

   fde803 ............................. Address count: 1000

   d91f4854 ........................... [Epoch time][unix epoch time]: 1414012889
   0100000000000000 ................... Service bits: 01 ([network][network] node)
   00000000000000000000ffffc0000233 ... IP Address: ::ffff:192.0.2.51
   208d ............................... Port: 8333

   [...] .............................. (999 more addresses omitted)
