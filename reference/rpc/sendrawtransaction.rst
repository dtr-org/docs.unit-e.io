.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

sendrawtransaction
------------------

``sendrawtransaction "hexstring" ( allowhighfees )``

Submits raw transaction (serialized, hex-encoded) to local node and network.

Also see createrawtransaction and signrawtransaction calls.

Argument #1 - hexstring
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The hex string of the raw transaction)

Argument #2 - allowhighfees
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=false

Allow high fees

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - hex
     - string
     - The transaction hash in hex

Examples
~~~~~~~~

Create a transaction::

  unite-cli createrawtransaction "[{\"txid\" : \"mytxid\",\"vout\":0}]" "{\"myaddress\":0.01}"

Sign the transaction, and get back the hex::

  unite-cli signrawtransaction "myhex"

Send the transaction (signed hex)::

  unite-cli sendrawtransaction "signedhex"

As a json rpc call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendrawtransaction", "params": ["signedhex"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

