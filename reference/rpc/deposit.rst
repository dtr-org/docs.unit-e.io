.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

deposit
-------

``deposit``

Creates a new deposit of the given amount, if accepted it will make the current node a validator.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** required

the destination for the deposit.

Argument #2 - amount
~~~~~~~~~~~~~~~~~~~~

**Type:** required

the amount deposit.

Examples
~~~~~~~~

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "deposit", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX" 150000000000] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

