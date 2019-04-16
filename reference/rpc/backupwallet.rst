.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

backupwallet
------------

``backupwallet "destination"``

Safely copies current wallet file to destination, which can be a directory or a path with filename.

Argument #1 - destination
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string

The destination directory or file

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli backupwallet "backup.dat"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "backupwallet", "params": ["backup.dat"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

