.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

verifychain
-----------

``verifychain ( checklevel nblocks )``

Verifies blockchain database.

Argument #1 - checklevel
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, 0-4, default=3

How thorough the block verification is.

Argument #2 - nblocks
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=6, 0=all

The number of blocks to check.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true|false
     - boolean
     - Verified or not

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli verifychain

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "verifychain", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

