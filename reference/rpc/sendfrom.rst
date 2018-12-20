.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

sendfrom
--------

``sendfrom "fromaccount" "toaddress" amount ( minconf "comment" "comment_to" )``

DEPRECATED (use sendtoaddress). Sent an amount from an account to a unite address.

Argument #1 - fromaccount
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The name of the account to send funds from. May be the default account using "".
       Specifying an account does not influence coin selection, but it does associate the newly created
       transaction with the account, so the account's balance computation and transaction history can reflect
       the spend.

Argument #2 - toaddress
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The unite address to send funds to.

Argument #3 - amount
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric or string, required

The amount in UTE (transaction fee is added on top).

Argument #4 - minconf
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=1

Only use funds with at least this many confirmations.

Argument #5 - comment
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

A comment used to store what the transaction is for. 
       This is not part of the transaction, just kept in your wallet.

Argument #6 - comment_to
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

An optional comment to store the name of the person or organization 
       to which you're sending the transaction. This is not part of the transaction, 
       it is just kept in your wallet.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - txid
     - string
     - The transaction id.

Examples
~~~~~~~~

Send 0.01 UTE from the default account to the address, must have at least 1 confirmation::

  unite-cli sendfrom "" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.01

Send 0.01 from the tabby account to the given address, funds must have at least 6 confirmations::

  unite-cli sendfrom "tabby" "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.01 6 "donation" "seans outpost"

As a json rpc call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["tabby", "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.01, 6, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

