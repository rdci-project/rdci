# About

This project is an entry in the hackathon Hack for Sweden 2018.

RDCI is a proof-of-concept demonstrating how public information can be placed on IPFS in order to make it resilient in a time 
of crisis.

The Internet is currently centralized and can be compromised in different ways by various entities. IPFS is however decentralized. You can think about it like bitcoin or git applied to the whole Internet.

The demo can be reached through IPFS via the hash `QmcL7KRwGCPsABq4YhJA7XeGHuXuUQxjcTUg7Wk3QWWAKe`. This is a single DNS-like name which can be altered to point to different content by site administrators.


Please take a look at the trailer: https://youtu.be/pYnihoYzVU4

You can reach the site via regular HTTP (proxy) by visiting:

[https://gateway.ipfs.io/ipns/QmcL7KRwGCPsABq4YhJA7XeGHuXuUQxjcTUg7Wk3QWWAKe](https://gateway.ipfs.io/ipns/QmcL7KRwGCPsABq4YhJA7XeGHuXuUQxjcTUg7Wk3QWWAKe)

or equivalently at https://goo.gl/8r4D8A

# Details

RDCI provides a CLI that facilities working with IPFS for people that are not familiar with it. Users can create a new IPFS site, preview it and publish it via a single user interface. The tool can add files to IPFS, and publish pages to IPNS (the "DNS" of IPFS).

The site can then be accessed via HTTP (as a proxy) or accessed directly on IPFS via that hash.

In the demo we've uploaded data from the Swedish police. We also have a map for Sweden which will contain information about shelters. Take a look at ... for details about that.

Note that any static data can be hosted on IPFS.

We've got some more info on https://devpost.com/software/resilient-distributed-crisis-information.

# About IPFS

From Wikipedia:

> InterPlanetary File System (IPFS) is a protocol and network designed to create a content-addressable, peer-to-peer method of storing and sharing hypermedia in a distributed file system. IPFS was initially designed by Juan Benet, and is now an open-source project developed with help from the community.

# Caveats

* IPFS is still in the incubation state. This means that usability is not what you might be used to and pulling and pushing data can be slower than you're used to.
* This is an entry in a hackathon and it still needs a lot of TLC.
