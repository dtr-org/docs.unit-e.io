.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

dumpprivkey
-----------

``dumpprivkey "address"``

Reveals the private key corresponding to 'address'.

Then the importprivkey can be used with this output

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The unite address for the private key

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - key
     - string
     - The private key

Examples
~~~~~~~~

::

  unite-cli dumpprivkey "myaddress"

::

  unite-cli importprivkey "mykey"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "dumpprivkey", "params": ["myaddress"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

