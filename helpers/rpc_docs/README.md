This directory contains a small tool to generate the RPC docs from the help
output of a running unit-e daemon. This makes it super-easy to update
documentation to the actual state of the implementation.

To run it you need to export the directory where you have your unit-e checkout
as UNIT_E_PATH environment variable. The tool currently assumes that you have
compiled binaries in the `src` directory in this path and that you have `united
-regtest` running.

The tool has unit tests. Run them by running `pytest`.

It requires jinja2 as templating framework to generate the RST files from the
data gathered from the daemon.
