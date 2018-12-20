.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

signmessagewithprivkey
----------------------

``signmessagewithprivkey "privkey" "message"``

Sign a message with the private key of an address

Argument #1 - privkey
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The private key to sign the message with.

Argument #2 - message
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The message to create a signature of.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - signature
     - string
     - The signature of the message encoded in base 64

Examples
~~~~~~~~

Create the signature::

  unite-cli signmessagewithprivkey "privkey" "my message"

Verify the signature::

  unite-cli verifymessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX" "signature" "my message"

As json rpc::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "signmessagewithprivkey", "params": ["privkey", "my message"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

