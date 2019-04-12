.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

.. _testnet:

Testnet
=======

Unit-e is under active development. It's built gradually and not done yet. The
first step is the testnet phase where we run a network for testing purposes, to
iron out bugs, and to experiment with some parameters, for example for the
economics. More features and components will be added and released over time.

If you build and run the unit-e client as described in the `unit-e README`_ it
will automatically connect to the testnet.

You can use the RPC interface to interact with the client. The most convenient
way is to use the ``unit-e-cli`` on the machine where you are running
``unit-e``. See the command line help you get with ``unit-e-cli -h`` for more
detailed instructions and the :ref:`rpc` for details on the RPC commands.

The peer-to-peer network protocol is documented in the :ref:`p2p`. The best
reference for how everything works together currently is the `source code`_.

If you find any issues please `report them on GitHub`_.

.. _unit-e README: https://github.com/dtr-org/unit-e/blob/master/README.md#running-from-source
.. _source code: https://github.com/dtr-org/unit-e
.. _report them on GitHub: https://github.com/dtr-org/unit-e/issues
