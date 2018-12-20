.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getaddressesbyaccount
---------------------

``getaddressesbyaccount "account"``

DEPRECATED. Returns the list of addresses for the given account.

Argument #1 - account
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The account name.

Result
~~~~~~

::

  [                     (json array of string)
    "address"         (string) a unite address associated with the given account
    ,...
  ]

Examples
~~~~~~~~

::

  unite-cli getaddressesbyaccount "tabby"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressesbyaccount", "params": ["tabby"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

