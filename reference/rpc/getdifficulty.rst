.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getdifficulty
-------------

``getdifficulty``

Returns the proof-of-work difficulty as a multiple of the minimum difficulty.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - n.nnn
     - numeric
     - the proof-of-work difficulty as a multiple of the minimum difficulty.

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli getdifficulty

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getdifficulty", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

