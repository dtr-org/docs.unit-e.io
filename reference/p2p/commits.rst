.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

commits
-------

Contains commits message as described in UIP-21. Sent in respose to a "getcommits" message.

Part of the mechanism to transfer finalizer commits as described in `UIP-21 <https://github.com/dtr-org/uips/blob/master/UIP-0021.md>`__.

+--------------------+------------------------------+----------+------------------------------------------------------------------------------------------------------+
| Name               | Data Type                    | Bytes    | Description                                                                                          |
+====================+==============================+==========+======================================================================================================+
| status             | uint8_                       | 1        | Status of reply, 0: finalization or "stop" reached, 1: tip reached, 2: message length limit exceeded |
+--------------------+------------------------------+----------+------------------------------------------------------------------------------------------------------+
| header and commits | vector_\<HeadersAndCommits_> | *Varies* | List of headers and commits                                                                          |
+--------------------+------------------------------+----------+------------------------------------------------------------------------------------------------------+

.. _HeadersAndCommits: types/HeadersAndCommits.html
.. _uint8: types/Integers.html
.. _vector: types/vector.html
