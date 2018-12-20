.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

abortrescan
-----------

``abortrescan``

Stops current wallet rescan triggered by an RPC call, e.g. by an importprivkey call.

Examples
~~~~~~~~

Import a private key::

  unite-cli importprivkey "mykey"

Abort the running wallet rescan::

  unite-cli abortrescan

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "abortrescan", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

