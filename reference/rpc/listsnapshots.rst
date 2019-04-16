.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

listsnapshots
-------------

``listsnapshots``

Lists all snapshots.

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli listsnapshots

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listsnapshots", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

