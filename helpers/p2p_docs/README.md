This directory contains the scripts and data to generate the reference
documentation for all the P2P messages Unit-e uses.

The data is taken from the unit-e sources and the information in the directory
`doc_data`. At the moment most of the information is not in the C++ sources.
This might change in the future im order to maintain the documentation closer to
the code which implements the documented messages.

The documentation is maintained in reStructuredText (RST) format. To generate
the part with the P2P messages reference, call

    ./p2p_docs_helper generate <path to a checkout of unit-e>

This will generate the RST data. You need to manually check it into git and push
it to master through a pull request to get it live on https://docs.unit-e.io.

To change the documentation, edit the files in the [`doc_data`](doc_data)
directory.

The script comes with unit tests which can be run with `pytest`.

The rendered data which is maintained in git doubles as a kind of integration
test. With `git diff` you can see the effect of your changes and by committing
the changes you create a new baseline to which you can compare future runs.
