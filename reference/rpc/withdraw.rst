.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

withdraw
--------

``withdraw``

Withdraw all funds form the validator's deposit and makes them available for the given address.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** required

the destination for the withdrawn funds.

Examples
~~~~~~~~

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "withdraw", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

