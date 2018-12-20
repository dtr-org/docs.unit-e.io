.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

createsnapshot
--------------

``createsnapshot (<maxutxosubsets>)``

Creates the snapshot of the UTXO subsets on the disk.

Argument #1 - maxutxosubsets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

Maximum UTXO subsets to dump into the file

Examples
~~~~~~~~

::

  unite-cli createsnapshot 10

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createsnapshot", "params": [10] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

