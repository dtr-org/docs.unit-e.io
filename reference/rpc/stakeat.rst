.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

stakeat
-------

``stakeat recipient test_fee coin_control``

Delegate staking to the provided recipient. The funds will still be spendable
by the current node.

Argument #1 - recipient
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** json, required

1.1 "address"    (string, required) The Unit-e address to send to.
       1.2 "amount"     (numeric or string, required) The amount in UTE to send, e.g. 0.1
       1.3 "subfee"     (boolean, optional, default=false) Deduct the fee from the amount being sent.

Argument #2 - test_fee
~~~~~~~~~~~~~~~~~~~~~~

**Type:** bool, optional, default=false

Only return the fee it would cost to send, txn is discarded.

Argument #3 - coin_control
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** json, optional

Coincontrol object.
       3.1 "changeaddress"  (string, optional) The Address for receiving change
       3.2 "inputs"         (json, optional) 
       [{"tx":, "n":},...],
       3.3 "replaceable"    (boolean, optional)  Allow this transaction to be replaced by a transaction
       with higher fees via BIP 125
       3.4 "conf_target"    (numeric, optional) Confirmation target (in blocks)
       3.5 "estimate_mode"  (string, optional) The fee estimate mode, must be one of:
       "UNSET"
       "ECONOMICAL"
       "CONSERVATIVE"
       3.6 "fee_rate"        (numeric, optional, default not set: makes wallet determine the fee) Set a specific 
       feerate (UTE per KB)
       7.7 "ignore_remote_staked" (boolean, opional, default=false) Exclude coins that are currently staked on other nodes.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - txid
     - string
     - The transaction id.

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli stakeat "{\"address\":\"2NDoNG8nR57LDs9m2VKV4wzYVR9YBJ2L5Nd\",\"amount\":0.1}"

