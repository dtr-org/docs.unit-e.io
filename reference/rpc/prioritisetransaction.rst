.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

prioritisetransaction
---------------------

``prioritisetransaction <txid> <dummy value> <fee delta>``

Accepts the transaction into mined blocks at a higher (or lower) priority

Argument #1 - txid
~~~~~~~~~~~~~~~~~~

**Type:** string, required

The transaction id.

Argument #2 - dummy
~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

API-Compatibility for previous API. Must be zero or null.
       DEPRECATED. For forward compatibility use named arguments and omit this parameter.

Argument #3 - fee_delta
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

The fee value (in satoshis) to add (or subtract, if negative).
       The fee is not actually paid, only the algorithm for selecting transactions into a block
       considers the transaction as it would have paid a higher (or lower) fee.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true
     - boolean
     - Returns true

Examples
~~~~~~~~

::

  unite-cli prioritisetransaction "txid" 0.0 10000

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "prioritisetransaction", "params": ["txid", 0.0, 10000] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

