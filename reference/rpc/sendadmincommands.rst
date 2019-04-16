.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

sendadmincommands
-----------------

``sendadmincommands``

Sends admin commands in a single transaction.

Argument #1 - prevouts
~~~~~~~~~~~~~~~~~~~~~~

**Type:** required

input UTXOs. [(tx_hash, out_n)ъ.

Argument #2 - fee
~~~~~~~~~~~~~~~~~

**Type:** required

fee you want to pay for this transaction.

Argument #3 - commands
~~~~~~~~~~~~~~~~~~~~~~

**Type:** required

list of commands to send:
       {'cmd': 'END_PERMISSIONING'}
       {'cmd': 'ADD_TO_WHITELIST', 'payload': <keys>}
       {'cmd': 'REMOVE_FROM_WHITELIST', 'payload': <keys>}
       {'cmd': 'RESET_ADMINS', 'payload': <keys>}

Argument #4 - destination
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** optional

where to send change if any.

Examples
~~~~~~~~


.. highlight:: shell

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendadmincommands", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

