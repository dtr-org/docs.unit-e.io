.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

generate
--------

``generate nblocks ( maxtries )``

Mine up to nblocks blocks immediately (before the RPC call returns) to an address in the wallet.

Note: this function can only be used on the regtest network.

Argument #1 - nblocks
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

How many blocks are generated immediately.

Argument #2 - maxtries
~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

How many iterations to try (default = 1000000).

Result
~~~~~~

::

  [ blockhashes ]     (array) hashes of blocks generated
  
  Examples:
  
  Generate 11 blocks
  > unit-e-cli generate 11

