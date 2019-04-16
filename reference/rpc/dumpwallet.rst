.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

dumpwallet
----------

``dumpwallet "filename"``

Dumps all wallet keys in a human-readable format to a server-side file. This does not allow overwriting existing files.

Imported scripts are included in the dumpfile, but corresponding BIP173 addresses, etc. may not be added automatically by importwallet.

Note that if your wallet contains keys which are not derived from your HD seed (e.g. imported keys), these are not covered by
only backing up the seed itself, and must be backed up too (e.g. ensure you back up the whole dumpfile).

Argument #1 - filename
~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The filename with path (either absolute or relative to unit-e)

Result
~~~~~~

::

  {                           (json object)
    "filename" : {        (string) The filename with full absolute path
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli dumpwallet "test"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "dumpwallet", "params": ["test"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

