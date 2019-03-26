.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

string
------

Variable length string type. This type consists of a length field and a sequence of characters with the actual data.

A string can be empty. Then it only consists of a zero length field and no data.

+------------+--------------+----------+---------------------------------------------------------------------------------+
| Name       | Data Type    | Bytes    | Description                                                                     |
+============+==============+==========+=================================================================================+
| length     | CompactSize_ | *Varies* | Number of characters in string                                                  |
+------------+--------------+----------+---------------------------------------------------------------------------------+
| characters | char_\[]     | *Varies* | Exactly as many `char <char.html>`__ elements as specified by the length field. |
+------------+--------------+----------+---------------------------------------------------------------------------------+

.. highlight:: text

::

   00 ................................. Bytes in string: 0 (empty string)
   0f ................................. Bytes in string: 15
   2f5361746f7368693a302e392e332f ..... String: /Satoshi:0.9.3/

.. _CompactSize: CompactSize.html
.. _char: char.html
