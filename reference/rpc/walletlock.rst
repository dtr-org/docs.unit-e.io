.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

walletlock
----------

``walletlock``

Removes the wallet encryption key from memory, locking the wallet.

After calling this method, you will need to call walletpassphrase again
before being able to call any methods which require the wallet to be unlocked.

Examples
~~~~~~~~

Set the passphrase for 2 minutes to perform a transaction::

  unite-cli walletpassphrase "my pass phrase" 120

Perform a send (requires passphrase set)::

  unite-cli sendtoaddress "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 1.0

Clear the passphrase since we are done before 2 minutes is up::

  unite-cli walletlock

As json rpc call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "walletlock", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

