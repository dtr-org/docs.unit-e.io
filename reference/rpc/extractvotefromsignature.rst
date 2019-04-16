.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

extractvotefromsignature
------------------------

``extractvotefromsignature``

Returns JSON representation of decoded vote

Argument #1 - signature
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string

.

Result
~~~~~~

::

  {
    "validator_address": xxxx   (string) the validator address
    "target_hash": xxxx
        (string) the target hash  "source_epoch": xxxx       (numeric) the source epoch
    "target_epoch": xxxx       (numeric) the target epoch
  }

