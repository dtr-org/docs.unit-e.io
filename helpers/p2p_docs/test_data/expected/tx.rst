It is sent in the raw transaction format. It can be sent in a variety of situations;

-  **Transaction Response:** unit-e and `Unit-eJ <http://unitej.github.io>`__ will send it in response to a `"getdata" message <getdata.html>`__ that requests the transaction with an inventory type of `"MSG_TX" </en/developer-reference#term-msg_tx>`__.

-  **MerkleBlock Response:** unit-e will send it in response to a `"getdata" message <getdata.html>`__ that requests a merkle block with an inventory type of ``MSG_MERKLEBLOCK``. (This is in addition to sending a `"merkleblock" message <merkleblock.html>`__.) Each `"tx" message <tx.html>`__ in this case provides a matched transaction from that block.

-  **Unsolicited:** `Unit-eJ <http://unitej.github.io>`__ will send a `"tx" message <tx.html>`__ unsolicited for transactions it originates.

For an example hexdump of the raw transaction format, see the `raw transaction section </en/developer-reference#raw-transaction-format>`__.

Control Messages
~~~~~~~~~~~~~~~~

The following `network </en/developer-guide#term-network>`__ messages all help control the connection between two peers or allow them to advise each other about the rest of the `network </en/developer-guide#term-network>`__.

.. figure:: /img/dev/en-p2p-control-messages.svg
   :alt: Overview Of P2P Protocol Control And Advisory Messages

   Overview Of P2P Protocol Control And Advisory Messages

Note that almost none of the control messages are authenticated in any way, meaning they can contain incorrect or intentionally harmful information. In addition, this section does not yet cover P2P protocol operation over the `Tor network <https://en.wikipedia.org/wiki/Tor_%28anonymity_network%29>`__; if you would like to contribute information about Tor, please `open an issue <https://github.com/unite-dot-org/unite.org/issues>`__.
