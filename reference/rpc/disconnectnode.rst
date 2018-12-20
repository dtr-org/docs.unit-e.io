.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

disconnectnode
--------------

``disconnectnode "[address]" [nodeid]``

Immediately disconnects from the specified peer node.

Strictly one out of 'address' and 'nodeid' can be provided to identify the node.

To disconnect by nodeid, either set 'address' to the empty string, or call using the named 'nodeid' argument only.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

The IP address/port of the node

Argument #2 - nodeid
~~~~~~~~~~~~~~~~~~~~

**Type:** number, optional

The node ID (see getpeerinfo for node IDs)

Examples
~~~~~~~~

::

  unite-cli disconnectnode "192.168.0.6:7182"

::

  unite-cli disconnectnode "" 1

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "disconnectnode", "params": ["192.168.0.6:7182"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "disconnectnode", "params": ["", 1] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

