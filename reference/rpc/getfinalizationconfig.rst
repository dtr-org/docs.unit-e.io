.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getfinalizationconfig
---------------------

``getfinalizationconfig``

Returns an object containing the esperanza protocol configuration.

Result
~~~~~~

::

  {
    "epochLength": xxxxxxx        (numeric) size of the epoch expressed in blocks
    "minDepositSize": xxxxxxx        (numeric) minimum deposit size allowed to become validator
    "dynastyLogoutDelay": xxxxxxx        (numeric) minimum delay in dynasties before a logout can be performed
    "withdrawalEpochDelay": xxxxxxx        (numeric) minimum delay in epochs before a withdrawal can take place
    "bountyFractionDenominator": xxxxxxx        (numeric) the bounty reward for reporting a slashable behaviour is defined by 1/x
    "slashFractionMultiplier": xxxxxxx        (numeric) multiplier for slashing the deposit of a misbehaving validator
    "baseInterestFactor": xxxxxxx        (numeric) base interest factor
    "basePenaltyFactor": xxxxxxx        (numeric) base penalty factor
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getfinalizationconfig", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

