.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

gettipsnapshot
--------------

``gettipsnapshot``

Returns the snapshot hash of the tip

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli gettipsnapshot

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettipsnapshot", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

