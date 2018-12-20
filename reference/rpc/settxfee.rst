.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

settxfee
--------

``settxfee amount``

Set the transaction fee per kB. Overwrites the paytxfee parameter.

Argument #1 - amount
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric or string, required

The transaction fee in UTE/kB

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true|false
     - boolean
     - Returns true if successful

Examples
~~~~~~~~

::

  unite-cli settxfee 0.00001

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "settxfee", "params": [0.00001] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

