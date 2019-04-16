.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

createvotetransaction
---------------------

``createvotetransaction``

Returns raw transaction data

Argument #1 - prev_tx
~~~~~~~~~~~~~~~~~~~~~

**Type:** string

previous transaction hash

Result raw transaction
~~~~~~~~~~~~~~~~~~~~~~

::

  > unit-e-cli createvotetransaction {"validator_address": xxxx, "target_hash": xxxx, "source_epoch": xxxx, "target_epoch": xxxx} txid

