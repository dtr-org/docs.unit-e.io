.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

importmasterkey
---------------

``importmasterkey``

Import a master key from a BIP39 seed, with an optional passphrase.

Argument #1 - seed
~~~~~~~~~~~~~~~~~~

**Type:** string, required

a list of words to create the master key from

Argument #2 - passphrase
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

an optional passphrase to protect the key

Argument #3 - rescan
~~~~~~~~~~~~~~~~~~~~

**Type:** bool, optional

an optional flag whether to rescan the blockchain

Examples
~~~~~~~~

::

  unite-cli importmasterkey "next debate force grief bleak want truck prepare theme lecture wear century rich grace someone"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "importmasterkey", "params": ["next debate force grief bleak want truck prepare theme lecture wear century rich grace someone"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

