.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

verifymessage
-------------

``verifymessage "address" "signature" "message"``

Verify a signed message

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The Unit-e address to use for the signature.

Argument #2 - signature
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The signature provided by the signer in base 64 encoding (see signmessage).

Argument #3 - message
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The message that was signed.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true|false
     - boolean
     - If the signature is verified or not.

Examples
~~~~~~~~


.. highlight:: shell

Unlock the wallet for 30 seconds::

  unit-e-cli walletpassphrase "mypassphrase" 30

Create the signature::

  unit-e-cli signmessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX" "my message"

Verify the signature::

  unit-e-cli verifymessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX" "signature" "my message"

As json rpc::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "verifymessage", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX", "signature", "my message"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

