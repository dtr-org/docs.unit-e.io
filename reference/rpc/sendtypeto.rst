.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

sendtypeto
----------

``sendtypeto "typein" "typeout" [{address: , amount: , narr: , subfee:},...] ("comment" "comment-to" test_fee coin_control)``

Send Unit-e to multiple outputs.

Argument #1 - typein
~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

Argument #2 - typeout
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

Argument #3 - outputs
~~~~~~~~~~~~~~~~~~~~~

**Type:** json, required

::

  [                  (Array of output objects)
    {
      "address": "<address>", (string, required) The Unit-e address to send to.
      "amount": x.xxx,        (numeric or string, required) The amount in UTE to send. eg 0.1
      "subfee": b,            (boolean, optional, default=false) The fee will be deducted from the amount being sent.
      "script": "<script>"    (string, optional) Hex encoded script, will override the address.
    }
    ,...
  ]

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

::

  {
    "changeaddress": "<address>", (string, optional) The Address for receiving change
    "inputs":                     (json, optional)
           [{"tx":, "n":},...],
    "replaceable": b,             (boolean, optional)  Allow this transaction to be replaced by a transaction
                                  with higher fees via BIP 125
    "conf_target": n,             (numeric, optional) Confirmation target (in blocks)
    "estimate_mode": "xxx",       (string, optional) The fee estimate mode, must be one of:
            "UNSET"
            "ECONOMICAL"
            "CONSERVATIVE"
    "fee_rate": n,                (numeric, optional, default not set: makes wallet determine the fee) Set a specific
                                  feerate (UTE per KB)
    "ignore_remote_staked": b     (boolean, optional, default=false) Exclude coins that are currently staked on other nodes.
  }

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

  unit-e-cli sendtypeto unit unit "[{\"address\":\"2NDoNG8nR57LDs9m2VKV4wzYVR9YBJ2L5Nd\",\"amount\":0.1}]"

