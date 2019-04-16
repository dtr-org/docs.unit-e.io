.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getchaintips
------------

``getchaintips``

Return information about all known tips in the block tree, including the main chain as well as orphaned branches.

Result
~~~~~~

::

  [
    {
      "height": xxxx,         (numeric) height of the chain tip
      "hash": "xxxx",         (string) block hash of the tip
      "branchlen": 0          (numeric) zero for main chain
      "status": "active"      (string) "active" for the main chain
    },
    {
      "height": xxxx,
      "hash": "xxxx",
      "branchlen": 1          (numeric) length of branch connecting the tip to the main chain
      "status": "xxxx"        (string) status of the chain (active, valid-fork, valid-headers, headers-only, invalid)
    }
  ]

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli getchaintips

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getchaintips", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

