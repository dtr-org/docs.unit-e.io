.. Copyright (c) 2018 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

mnemonic
--------

``mnemonic new|decode|addchecksum|dumpwords|listlanguages``

mnemonic new [password]
    Generate a new mnemonic seed for setting a master
    key for the hierarchical deterministic wallet.

mnemonic info <mnemonic> [password]
    Shows various kinds of information about a mnemonic seed:

    "language": the language detected from the words,
    "bip39_seed": the seed decoded and converted to hex,
    "bip32_root": the private key derived from this seed,
    "entropy": the entropy contained in this seed.

mnemonic listlanguages
    Print list of supported languages.

