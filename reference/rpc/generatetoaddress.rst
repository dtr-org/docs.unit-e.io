.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

generatetoaddress
-----------------

``generatetoaddress nblocks address (maxtries)``

Mine blocks immediately to a specified address (before the RPC call returns)

Argument #1 - nblocks
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

How many blocks are generated immediately.

Argument #2 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The address to send the newly generated unite to.

Argument #3 - maxtries
~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

How many iterations to try (default = 1000000).

Result
~~~~~~

::

  [ blockhashes ]     (array) hashes of blocks generated
  
  Examples:
  
  Generate 11 blocks to myaddress
  > unite-cli generatetoaddress 11 "myaddress"

