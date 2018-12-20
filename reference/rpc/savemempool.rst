.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

savemempool
-----------

``savemempool``

Dumps the mempool to disk.

Examples
~~~~~~~~

::

  unite-cli savemempool

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "savemempool", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

