
import tarfile

import requests

IPFS_URL="https://dist.ipfs.io/go-ipfs/v0.4.14/go-ipfs_v0.4.14_darwin-amd64.tar.gz"
LOCAL_FILE="go-ipfs.tar.gz"
IPFS_BIN_LOCATION = "go-ipfs/ipfs"

def download_ipfs():
    r = requests.get(IPFS_URL, stream=True)
    with open(LOCAL_FILE, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    tar = tarfile.open(LOCAL_FILE)
    tar.extractall()
    tar.close()

    return IPFS_BIN_LOCATION