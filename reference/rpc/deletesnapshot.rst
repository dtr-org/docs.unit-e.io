.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

deletesnapshot
--------------

``deletesnapshot (<snapshothash>)``

Deletes snapshot from disk.

Argument #1 - snapshothash
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** hex, required

hash of the snapshot to delete

Examples
~~~~~~~~

::

  unite-cli deletesnapshot 34aa7d3aabd5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "deletesnapshot", "params": [34aa7d3aabd5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

