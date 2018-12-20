.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

walletpassphrasechange
----------------------

``walletpassphrasechange "oldpassphrase" "newpassphrase"``

Changes the wallet passphrase from 'oldpassphrase' to 'newpassphrase'.

Argument #1 - oldpassphrase
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string

The current passphrase

Argument #2 - newpassphrase
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string

The new passphrase

Examples
~~~~~~~~

::

  unite-cli walletpassphrasechange "old one" "new one"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "walletpassphrasechange", "params": ["old one", "new one"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

