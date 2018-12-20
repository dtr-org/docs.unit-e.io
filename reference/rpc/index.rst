.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

RPC API Reference
=================

This is the reference for the RPC API calls of Unit-e. Use `unite-cli` to run
the commands.

Blockchain
----------

.. toctree::
  :maxdepth: 1

  getbestblockhash
  getblock
  getblockchaininfo
  getblockcount
  getblockhash
  getblockheader
  getchaintips
  getchaintxstats
  getdifficulty
  getmempoolancestors
  getmempooldescendants
  getmempoolentry
  getmempoolinfo
  getrawmempool
  gettxout
  gettxoutproof
  gettxoutsetinfo
  preciousblock
  pruneblockchain
  savemempool
  verifychain
  verifytxoutproof

Control
-------

.. toctree::
  :maxdepth: 1

  getmemoryinfo
  help
  logging
  stop
  uptime

Finalization
------------

.. toctree::
  :maxdepth: 1

  getfinalizationconfig
  getfinalizationstate

Generating
----------

.. toctree::
  :maxdepth: 1

  generate
  generatetoaddress

Mining
------

.. toctree::
  :maxdepth: 1

  prioritisetransaction

Mnemonic
--------

.. toctree::
  :maxdepth: 1

  mnemonic

Network
-------

.. toctree::
  :maxdepth: 1

  addnode
  clearbanned
  disconnectnode
  getaddednodeinfo
  getconnectioncount
  getnettotals
  getnetworkinfo
  getpeerinfo
  listbanned
  ping
  setban
  setnetworkactive

Rawtransactions
---------------

.. toctree::
  :maxdepth: 1

  combinerawtransaction
  createrawtransaction
  decoderawtransaction
  decodescript
  fundrawtransaction
  getrawtransaction
  sendrawtransaction
  signrawtransaction

Snapshot
--------

.. toctree::
  :maxdepth: 1

  calcsnapshothash
  createsnapshot
  deletesnapshot
  getblocksnapshot
  gettipsnapshot
  listsnapshots

Util
----

.. toctree::
  :maxdepth: 1

  createmultisig
  estimatefee
  estimatesmartfee
  signmessagewithprivkey
  validateaddress
  verifymessage

Wallet
------

.. toctree::
  :maxdepth: 1

  abandontransaction
  abortrescan
  addmultisigaddress
  addressbookinfo
  backupwallet
  bumpfee
  deposit
  dumpprivkey
  dumpwallet
  encryptwallet
  filteraddresses
  filtertransactions
  getaccount
  getaccountaddress
  getaddressesbyaccount
  getbalance
  getnewaddress
  getrawchangeaddress
  getreceivedbyaccount
  getreceivedbyaddress
  gettransaction
  getunconfirmedbalance
  getvalidatorinfo
  getwalletinfo
  importaddress
  importmasterkey
  importmulti
  importprivkey
  importprunedfunds
  importpubkey
  importwallet
  keypoolrefill
  listaccounts
  listaddressgroupings
  listlockunspent
  listreceivedbyaccount
  listreceivedbyaddress
  listsinceblock
  listtransactions
  listunspent
  listwallets
  lockunspent
  logout
  manageaddressbook
  move
  removeprunedfunds
  rescanblockchain
  sendadmincommands
  sendfrom
  sendmany
  sendtoaddress
  sendtypeto
  setaccount
  settxfee
  signmessage
  walletlock
  walletpassphrase
  walletpassphrasechange
  withdraw

