.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

listwallets
-----------

``listwallets``

Returns a list of currently loaded wallets.

For full information on the wallet, use "getwalletinfo"

Result
~~~~~~

::

  [                         (json array of strings)
    "walletname"            (string) the wallet name
     ...
  ]

Examples
~~~~~~~~

::

  unite-cli listwallets

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listwallets", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

