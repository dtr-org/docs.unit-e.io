.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getbestblockhash
----------------

``getbestblockhash``

Returns the hash of the best (tip) block in the longest blockchain.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - hex
     - string
     - the block hash hex encoded

Examples
~~~~~~~~

::

  unite-cli getbestblockhash

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getbestblockhash", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

