.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

listbanned
----------

``listbanned``

List all banned IPs/Subnets.

Examples
~~~~~~~~

::

  unite-cli listbanned

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listbanned", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

