.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

filtertransactions
------------------

``filtertransactions ( options )``

List transactions.

Argument #1 - options
~~~~~~~~~~~~~~~~~~~~~

**Type:** json, optional

: A configuration object for the query
       All keys are optional. Default values are:
       Expected values are as follows:
       count:             number of transactions to be displayed
       (integer >= 0, use 0 for unlimited)
       skip:              number of transactions to skip
       (integer >= 0)
       include_watchonly: whether to include watchOnly transactions
       (bool string)
       search:            a query to search addresses and amounts
       character DOT '.' is not searched for:
       search "123" will find 1.23 and 12.3
       (query string)
       category:          select only one category of transactions to return
       (string from list)
       all, send, orphan, immature, coinbase, 
       receive, orphaned_stake, stake, internal_transfer
       sort:              sort transactions by criteria
       (string from list)
       time          most recent first
       address       alphabetical
       category      alphabetical
       amount        biggest first
       confirmations most confirmations first
       txid          alphabetical
       from:              unix timestamp or string "yyyy-mm-ddThh:mm:ss"
       to:                unix timestamp or string "yyyy-mm-ddThh:mm:ss"
       collate:           display number of records and sum of amount fields

::

    {
        "count":             10,
        "skip":              0,
        "include_watchonly": false,
        "search":            ''
        "category":          'all',
        "sort":              'time'
        "from":              '0'
        "to":                '9999'
        "collate":           false
    }

Examples
~~~~~~~~


.. highlight:: shell

