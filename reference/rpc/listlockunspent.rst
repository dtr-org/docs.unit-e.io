.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

listlockunspent
---------------

``listlockunspent``

Returns list of temporarily unspendable outputs.

See the lockunspent call to lock and unlock transactions for spending.

Result
~~~~~~

::

  [
    {
      "txid" : "transactionid",     (string) The transaction id locked
      "vout" : n                      (numeric) The vout value
    }
    ,...
  ]

Examples
~~~~~~~~

List the unspent transactions::

  unite-cli listunspent

Lock an unspent transaction::

  unite-cli lockunspent false "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

List the locked transactions::

  unite-cli listlockunspent

Unlock the transaction again::

  unite-cli lockunspent true "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

As a json rpc call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listlockunspent", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

