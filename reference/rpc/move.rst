.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

move
----

``move "fromaccount" "toaccount" amount ( minconf "comment" )``

DEPRECATED. Move a specified amount from one account in your wallet to another.

Argument #1 - fromaccount
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The name of the account to move funds from. May be the default account using "".

Argument #2 - toaccount
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The name of the account to move funds to. May be the default account using "".

Argument #3 - amount
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric

Quantity of UTE to move between accounts.

Argument #4 - (dummy)
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

Ignored. Remains for backward compatibility.

Argument #5 - comment
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

An optional comment, stored in the wallet only.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true|false
     - boolean
     - true if successful.

Examples
~~~~~~~~

Move 0.01 UTE from the default account to the account named tabby::

  unite-cli move "" "tabby" 0.01

Move 0.01 UTE timotei to akiko with a comment and funds have 6 confirmations::

  unite-cli move "timotei" "akiko" 0.01 6 "happy birthday!"

As a json rpc call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "move", "params": ["timotei", "akiko", 0.01, 6, "happy birthday!"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

