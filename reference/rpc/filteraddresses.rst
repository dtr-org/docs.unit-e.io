.. Copyright (c) 2018-2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

filteraddresses
---------------

``filteraddresses ( offset count sort_code "search" match_owned )``

List addresses.

Argument #1 - "offset":
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

number of addresses to skip

Argument #2 - "count":
~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

number of addresses to be displayed

Argument #3 - "sort_code":
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

0 sort by label ascending,
       1 sort by label descending, default 0

Argument #4 - "search":
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

a query to search labels

Argument #5 - "match_owned":
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

0 off, 1 owned, 2 non-owned,
       default 0

