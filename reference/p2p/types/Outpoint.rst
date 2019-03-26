.. Copyright (c) 2014-2018 Bitcoin.org
   Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

Outpoint
--------


Outpoint: The Specific Part Of A Specific Output
''''''''''''''''''''''''''''''''''''''''''''''''

Because a single transaction can include multiple outputs, the outpoint structure includes both a TXID and an output index number to refer to specific output.

+-------+-----------+-------+-------------------------------------------------------------------------------------------------------------------+
| Name  | Data Type | Bytes | Description                                                                                                       |
+=======+===========+=======+===================================================================================================================+
| hash  | uint256_  | 32    | The TXID of the transaction holding the output to spend. The TXID is a hash provided here in internal byte order. |
+-------+-----------+-------+-------------------------------------------------------------------------------------------------------------------+
| index | uint32_   | 4     | The output index number of the specific output to spend from the transaction. The first output is 0x00000000.     |
+-------+-----------+-------+-------------------------------------------------------------------------------------------------------------------+

.. _uint256: Integers.html
.. _uint32: Integers.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
