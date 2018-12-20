.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

clearbanned
-----------

``clearbanned``

Clear all banned IPs.

Examples
~~~~~~~~

::

  unite-cli clearbanned

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "clearbanned", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

