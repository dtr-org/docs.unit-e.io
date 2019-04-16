.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

setaccount
----------

``setaccount "address" "account"``

DEPRECATED. Sets the account associated with the given address.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The Unit-e address to be associated with an account.

Argument #2 - account
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The account to assign the address to.

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli setaccount "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX" "tabby"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setaccount", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX", "tabby"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

