A vector is a variable-length array of elements of a certain type. It consists of a field indicating the number of elements followed by the elements itself. The size of the vector varies depending on the number and size of the elements.

Many messages use vectors of other data types in their payload. See the `"example" message <../example.html>`__.

+---------+--------------+----------+-----------------------------------------------------------------------+
| Name    | Data Type    | Bytes    | Description                                                           |
+=========+==============+==========+=======================================================================+
| count   | CompactSize_ | *Varies* | The number of elements contained in the vector.                       |
+---------+--------------+----------+-----------------------------------------------------------------------+
| element | *Varies*     | *Varies* | The data of exactly as many elements as indicated by the count field. |
+---------+--------------+----------+-----------------------------------------------------------------------+

An example of a vector of `addresses <address.html>`__:

.. highlight:: text

::

   fde803 ............................. Address count: 1000

   d91f4854 ........................... [Epoch time][unix epoch time]: 1414012889
   0100000000000000 ................... Service bits: 01 ([network][network] node)
   00000000000000000000ffffc0000233 ... IP Address: ::ffff:192.0.2.51
   208d ............................... Port: 8333

   [...] .............................. (999 more addresses omitted)

.. _CompactSize: CompactSize.html
