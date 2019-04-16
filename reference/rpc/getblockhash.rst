.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getblockhash
------------

``getblockhash height``

Returns hash of block in best-block-chain at height provided.

Argument #1 - height
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

The height index

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - hash
     - string
     - The block hash

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli getblockhash 1000

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockhash", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

