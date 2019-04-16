.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getrawchangeaddress
-------------------

``getrawchangeaddress ( "address_type" )``

Returns a new Unit-e address, for receiving change.

This is for use with raw transactions, NOT normal use.

Argument #1 - address_type
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

The address type to use. Options are "legacy", "p2sh-segwit", and "bech32". Default is set by -changetype.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - address
     - string
     - The address

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli getrawchangeaddress

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawchangeaddress", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

