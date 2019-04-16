.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getfinalizationstate
--------------------

``getfinalizationstate``

Returns an object containing finalization information.

Result
~~~~~~

::

  {
    "currentDynasty": xxxxxxx          (numeric) currentDynasty
    "currentEpoch": xxxxxxx            (numeric) currentEpoch
    "lastJustifiedEpoch": xxxxxxx      (numeric) lastJustifiedEpoch
    "lastFinalizedEpoch": xxxxxxx      (numeric) lastFinalizedEpoch
    "validators": xxxxxxx              (numeric) current number of active validators
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli getfinalizationstate

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getfinalizationstate", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

