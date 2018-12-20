.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

combinerawtransaction
---------------------

``combinerawtransaction ["hexstring",...]``

Combine multiple partially signed transactions into one transaction.

The combined transaction may be another partially signed transaction or a
fully signed transaction.

Argument #1 - txs
~~~~~~~~~~~~~~~~~

**Type:** string

A json array of hex strings of partially signed transactions

::

    [
      "hexstring"     (string) A transaction hash
      ,...
    ]

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - hex
     - string
     - The hex-encoded raw transaction with signature(s)

Examples
~~~~~~~~

::

  unite-cli combinerawtransaction ["myhex1", "myhex2", "myhex3"]

