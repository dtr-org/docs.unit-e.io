.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getblockheader
--------------

``getblockheader "hash" ( verbose )``

If verbose is false, returns a string that is serialized, hex-encoded data for blockheader 'hash'.

If verbose is true, returns an Object with information about blockheader <hash>.

Argument #1 - hash
~~~~~~~~~~~~~~~~~~

**Type:** string, required

The block hash

Argument #2 - verbose
~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

true for a json object, false for the hex encoded data

Result (for verbose = true)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {
    "hash" : "hash",     (string) the block hash (same as provided)
    "confirmations" : n,   (numeric) The number of confirmations, or -1 if the block is not on the main chain
    "height" : n,          (numeric) The block height or index
    "version" : n,         (numeric) The block version
    "versionHex" : "00000000", (string) The block version formatted in hexadecimal
    "merkleroot" : "xxxx", (string) The merkle root
    "witnessmerkleroot" : "xxxx", (string) The witness merkle root
    "finalizercommitsmerkleroot" : "xxxx", (string) The finalizer commits merkle root
    "time" : ttt,          (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
    "mediantime" : ttt,    (numeric) The median block time in seconds since epoch (Jan 1 1970 GMT)
    "bits" : "1d00ffff", (string) The bits
    "difficulty" : x.xxx,  (numeric) The difficulty
    "chainwork" : "0000...1f3"     (string) Expected number of hashes required to produce the current chain (in hex)
    "nTx" : n,             (numeric) The number of transactions in the block.
    "previousblockhash" : "hash",  (string) The hash of the previous block
    "nextblockhash" : "hash",      (string) The hash of the next block
  }

Result (for verbose=false)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - data
     - string
     - A string that is serialized, hex-encoded data for block 'hash'.

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli getblockheader "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockheader", "params": ["00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

