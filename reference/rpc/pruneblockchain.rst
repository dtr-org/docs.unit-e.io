.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

pruneblockchain
---------------

``pruneblockchain``


Argument #1 - height
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

The block height to prune up to. May be set to a discrete height, or a unix timestamp
       to prune blocks whose block time is at least 2 hours older than the provided timestamp.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - n
     - numeric
     - Height of the last block pruned.

Examples
~~~~~~~~

::

  unite-cli pruneblockchain 1000

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "pruneblockchain", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

