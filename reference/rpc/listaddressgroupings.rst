.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

listaddressgroupings
--------------------

``listaddressgroupings``

Lists groups of addresses which have had their common ownership
made public by common use as inputs or as the resulting change
in past transactions

Result
~~~~~~

::

  [
    [
      [
        "address",            (string) The unite address
        amount,                 (numeric) The amount in UTE
        "account"             (string, optional) DEPRECATED. The account
      ]
      ,...
    ]
    ,...
  ]

Examples
~~~~~~~~

::

  unite-cli listaddressgroupings

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listaddressgroupings", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

