.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

walletpassphrase
----------------

``walletpassphrase "passphrase" timeout [staking_only]``

Stores the wallet decryption key in memory for 'timeout' seconds.

This is needed prior to performing transactions related to private keys such as sending unites

Argument #1 - passphrase
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The wallet passphrase

Argument #2 - timeout
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

The time to keep the decryption key in seconds; capped at 100000000 (~3 years).

Argument #3 - staking_only
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=false

Unlock the wallet for staking, but not for other operations. Set <timeout> to 0
       to keep it unlocked indefinitely.

Examples
~~~~~~~~

Unlock the wallet for 60 seconds::

  unite-cli walletpassphrase "my pass phrase" 60

Lock the wallet again (before 60 seconds)::

  unite-cli walletlock

As json rpc call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "walletpassphrase", "params": ["my pass phrase", 60] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

