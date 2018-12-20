.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getvalidatorinfo
----------------

``getvalidatorinfo``

Returns an object containing validator-related information.

Result
~~~~~~

::

  {
    "enabled": true|false,    (boolean) if staking is enabled or not on this wallet.
    "validator_status":       (string) the current status of the validator.
  }

Examples
~~~~~~~~

::

  unite-cli getvalidatorinfo

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getvalidatorinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

