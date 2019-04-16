.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getaddednodeinfo
----------------

``getaddednodeinfo ( "node" )``

Returns information about the given added node, or all added nodes
(note that onetry addnodes are not listed here)

Argument #1 - node
~~~~~~~~~~~~~~~~~~

**Type:** string, optional

If provided, return information about this specific node, otherwise all nodes are returned.

Result
~~~~~~

::

  [
    {
      "addednode" : "192.168.0.201",   (string) The node IP address or name (as provided to addnode)
      "connected" : true|false,          (boolean) If connected
      "addresses" : [                    (list of objects) Only when connected = true
         {
           "address" : "192.168.0.201:7182",  (string) The unite server IP and port we're connected to
           "connected" : "outbound"           (string) connection, inbound or outbound
         }
       ]
    }
    ,...
  ]

Examples
~~~~~~~~


.. highlight:: shell

::

  unit-e-cli getaddednodeinfo "192.168.0.201"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddednodeinfo", "params": ["192.168.0.201"] }' -H 'content-type: text/plain;' http://127.0.0.1:7181/

