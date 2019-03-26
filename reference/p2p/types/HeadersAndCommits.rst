HeadersAndCommits
-----------------

List of block headers and their corresponding finalizer commit transactions.

+--------------+------------------------+----------+----------------------------------------------------------+
| Name         | Data Type              | Bytes    | Description                                              |
+==============+========================+==========+==========================================================+
| block header | BlockHeader_           | 80       | Header of block to which the commit transactions belong  |
+--------------+------------------------+----------+----------------------------------------------------------+
| commits      | vector_\<Transaction_> | *Varies* | Finalizer commit transactions for the given block header |
+--------------+------------------------+----------+----------------------------------------------------------+

.. _BlockHeader: BlockHeader.html
.. _Transaction: Transaction.html
.. _vector: vector.html
