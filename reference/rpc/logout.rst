.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

logout
------

``logout``

Creates a logout request, if accepted it will start the logout process for the validator.

Examples
~~~~~~~~


.. highlight:: shell

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "logout", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

