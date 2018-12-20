.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getreceivedbyaccount
--------------------

``getreceivedbyaccount "account" ( minconf )``

DEPRECATED. Returns the total amount received by addresses with <account> in transactions with at least [minconf] confirmations.

Argument #1 - account
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The selected account, may be the default account using "".

Argument #2 - minconf
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=1

Only include transactions confirmed at least this many times.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - amount
     - numeric
     - The total amount in UTE received for this account.

Examples
~~~~~~~~

Amount received by the default account with at least 1 confirmation::

  unite-cli getreceivedbyaccount ""

Amount received at the tabby account including unconfirmed amounts with zero confirmations::

  unite-cli getreceivedbyaccount "tabby" 0

The amount with at least 6 confirmations::

  unite-cli getreceivedbyaccount "tabby" 6

As a json rpc call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getreceivedbyaccount", "params": ["tabby", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

