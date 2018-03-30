#!/bin/bash

mkdir -p ./tmp
cd ./tmp
wget -nc https://dist.ipfs.io/go-ipfs/v0.4.14/go-ipfs_v0.4.14_darwin-amd64.tar.gz 
tar -xzvf go-ipfs_v0.4.14_darwin-amd64.tar.gz
cd go-ipfs
./install.sh
ipfs init

