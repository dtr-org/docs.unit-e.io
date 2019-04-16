.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

uptime
------

``uptime``

Returns the total uptime of the server.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ttt
     - numeric
     - The number of seconds that the server has been running

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli uptime

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "uptime", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

