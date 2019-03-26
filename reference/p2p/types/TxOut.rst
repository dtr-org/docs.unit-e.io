.. Copyright (c) 2014-2018 Bitcoin.org
   Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

TxOut
-----


A Transaction Output

Each output spends a certain number of satoshis, placing them under control of anyone who can satisfy the provided pubkey script.

+-----------+-----------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name      | Data Type | Bytes    | Description                                                                                                                                                                                                                                                     |
+===========+===========+==========+=================================================================================================================================================================================================================================================================+
| value     | int64_    | 8        | Number of satoshis to spend. May be zero; the sum of all outputs may not exceed the sum of satoshis previously spent to the outpoints provided in the input section. (Exception: coinbase transactions spend the block subsidy and collected transaction fees.) |
+-----------+-----------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pk_script | string_   | *Varies* | Pubkey script. Defines the conditions which must be satisfied to spend this output. Maximum length is 10,000 bytes.                                                                                                                                             |
+-----------+-----------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _int64: Integers.html
.. _string: string.html

.. Content originally imported from https://github.com/bitcoin-dot-org/bitcoin.org/blob/master/_data/devdocs/en/references/
