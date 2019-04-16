.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

keypoolrefill
-------------

``keypoolrefill ( newsize )``

Fills the keypool.

Arguments
1. newsize     (numeric, optional, default=100) The new keypool size

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli keypoolrefill

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "keypoolrefill", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

