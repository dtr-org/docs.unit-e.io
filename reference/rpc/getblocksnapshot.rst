.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getblocksnapshot
----------------

``getblocksnapshot (<blockhash>)``

Returns the snapshot hash of the block.

Argument #1 - blockhash
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** hex, optional

block hash to lookup. If missing, the top is used. 

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli getblocksnapshot 0000000000d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblocksnapshot", "params": [0000000000d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

