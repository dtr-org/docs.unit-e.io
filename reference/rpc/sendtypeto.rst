.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

sendtypeto
----------

``sendtypeto "typein" "typeout" [{address: , amount: , narr: , subfee:},...] ("comment" "comment-to" test_fee coin_control)``

Send UnitE to multiple outputs.

Argument #1 - typein
~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

Argument #2 - typeout
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

Argument #3 - outputs
~~~~~~~~~~~~~~~~~~~~~

**Type:** json, required

Array of output objects
       3.1 "address"    (string, required) The UnitE address to send to.
       3.2 "amount"     (numeric or string, required) The amount in UTE to send. eg 0.1
       3.x "subfee"     (boolean, optional, default=false) The fee will be deducted from the amount being sent.
       3.x "script"     (string, optional) Hex encoded script, will override the address.

Argument #4 - comment
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

A comment used to store what the transaction is for. 
       This is not part of the transaction, just kept in your wallet.

Argument #5 - comment_to
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

A comment to store the name of the person or organization 
       to which you're sending the transaction. This is not part of the 
       transaction, just kept in your wallet.

Argument #6 - test_fee
~~~~~~~~~~~~~~~~~~~~~~

**Type:** bool, optional, default=false

Only return the fee it would cost to send, txn is discarded.

Argument #7 - coin_control
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** json, optional

Coincontrol object.
       7.1 "changeaddress"  (string, optional) The Address for receiving change
       7.2 "inputs"         (json, optional) 
       [{"tx":, "n":},...],
       7.3 "replaceable"    (boolean, optional)  Allow this transaction to be replaced by a transaction
       with higher fees via BIP 125
       7.4 "conf_target"    (numeric, optional) Confirmation target (in blocks)
       7.5 "estimate_mode"  (string, optional) The fee estimate mode, must be one of:
       "UNSET"
       "ECONOMICAL"
       "CONSERVATIVE"
       7.6 "fee_rate"        (numeric, optional, default not set: makes wallet determine the fee) Set a specific 
       feerate (UTE per KB)

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

::

  unite-cli sendtypeto unit unit "[{\"address\":\"2NDoNG8nR57LDs9m2VKV4wzYVR9YBJ2L5Nd\",\"amount\":0.1}]"

