.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

calcsnapshothash
----------------

``calcsnapshothash``

Returns snapshot hash and its data after arithmetic calculations

Argument #1 - inputs
~~~~~~~~~~~~~~~~~~~~

**Type:** hex, required

serialized UTXOs to subtract.

Argument #2 - outputs
~~~~~~~~~~~~~~~~~~~~~

**Type:** hex, required

serialized UTXOs to add.

Argument #3 - stakeModifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** hex, required

stake modifier of the current block

Argument #4 - snapshotData
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** hex, optional

initial snapshot data.

Examples
~~~~~~~~

::

  unite-cli calcsnapshothash 010000000000000000000000000000000000000000000000000000000000000000ffffffff0000000000ffffffffffffffff00 010000000000000000000000000000000000000000000000000000000000000000ffffffff0000000000ffffffffffffffff00 aa00000000000000000000000000000000000000000000000000000000000000 60000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "calcsnapshothash", "params": [010000000000000000000000000000000000000000000000000000000000000000ffffffff0000000000ffffffffffffffff00 010000000000000000000000000000000000000000000000000000000000000000ffffffff0000000000ffffffffffffffff00 aa00000000000000000000000000000000000000000000000000000000000000 60000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

