.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getaccount
----------

``getaccount "address"``

DEPRECATED. Returns the account associated with the given address.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The unite address for account lookup.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - accountname
     - string
     - the account address

Examples
~~~~~~~~

::

  unite-cli getaccount "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaccount", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

