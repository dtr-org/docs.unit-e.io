namespace NetMsgType {

/**
 * The version message provides information about the transmitting node to the
 * receiving node at the beginning of a connection.
 * @see https://unite.org/en/developer-reference#version
 */
extern const char *VERSION;
/**
 * The merkleblock message is a reply to a getdata message which requested a
 * block using the inventory type MSG_MERKLEBLOCK.
 * @since protocol version 70001 as described by BIP37.
 * @see https://unite.org/en/developer-reference#merkleblock
 */
extern const char *MERKLEBLOCK;
/**
 * The filterload message tells the receiving peer to filter all relayed
 * transactions and requested merkle blocks through the provided filter.
 * @since protocol version 70001 as described by BIP37.
 *   Only available with service bit NODE_BLOOM since protocol version
 *   70011 as described by BIP111.
 * @see https://unite.org/en/developer-reference#filterload
 */
extern const char *FILTERLOAD;
/**
 * Contains the snapshot::GetSnapshotHeader message.
 * Peer should respond with the "snaphead" message.
 */
extern const char *GETSNAPSHOTHEADER;
};

/* Get a vector of all valid message types (see above) */
const std::vector<std::string> &getAllNetMessageTypes();
