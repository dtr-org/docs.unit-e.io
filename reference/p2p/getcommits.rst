.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

getcommits
----------

Contains a getcommits request as described in UIP-21. Peer should respond with the "commits" message.

Part of the mechanism to transfer finalizer commits as described in `UIP-21 <https://github.com/dtr-org/uips/blob/master/UIP-0021.md>`__.

When a peer receives a "getcommits" message it scans the main chain starting from the first hash given in the ``start`` field. It searches the chain for subsequent checkpoints given in the ``start`` field. It replies with headers and commits for blocks folllowing the most recent checkpoint until it reaches the block given in the ``stop`` field, the next finalization point or the tip of the chain.

+-------+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name  | Data Type          | Bytes    | Description                                                                                                                                                          |
+=======+====================+==========+======================================================================================================================================================================+
| start | vector_\<uint256_> | *Varies* | Vector of block hashes, ascending order.                                                                                                                             |
+-------+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stop  | uint256_           | 32       | Hash of block when to stop sending headers and commits. If this is 0x0 commits are sent until the next finalization point or the tip of the chain have been reached. |
+-------+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uint256: types/Integers.html
.. _vector: types/vector.html
