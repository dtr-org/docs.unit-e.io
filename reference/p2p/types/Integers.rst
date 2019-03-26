.. Copyright (c) 2019 The Unit-e developers
   Distributed under the MIT software license, see the accompanying
   file LICENSE or https://opensource.org/licenses/MIT.

Integers
--------

There are signed and unsigned integer types of different sizes. All integers use little-endian byte order.

uint256 is used to represent a SHA256 hash, e.g. a block header hash. It's not really an integer as it is not used for arithmetic operations. When being compared it is treated as a little-endian byte ordered number. This is also referred to as internal byte order.

+---------+-------+--------+
| Type    | Bytes | Signed |
+=========+=======+========+
| int32   | 4     | Yes    |
+---------+-------+--------+
| int64   | 8     | Yes    |
+---------+-------+--------+
| uint8   | 1     | No     |
+---------+-------+--------+
| uint16  | 2     | No     |
+---------+-------+--------+
| uint32  | 4     | No     |
+---------+-------+--------+
| uint64  | 8     | No     |
+---------+-------+--------+
| uint256 | 32    | No     |
+---------+-------+--------+

Examples:

.. highlight:: text

::

   01 ......... uint8 (0x01, 1)
   ff080000 ... uint32 (0x8ff, 2303)
   feffffff ... int32 (0xfffffffe, -2)

Example for a block header hash:

.. highlight:: text

::

   6fe28c0ab6f1b372c1a6a246ae63f74f
   931e8365e15a089c68d6190000000000 ... uint256 (0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)
