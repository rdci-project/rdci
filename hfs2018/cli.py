import shutil
import subprocess
import sys
import os.path
import os

import click

from hfs2018.utils import download_ipfs, IPFS_BIN_LOCATION


@click.group()
def main():
    pass

@main.command("init")
def init():
    if not os.path.exists(IPFS_BIN_LOCATION):
        print("You don't have IPFS. Don't worry I'll download it for you...")
        download_ipfs()

    if os.path.exists(os.path.join(os.environ.get("HOME"), ".ipfs")):
        print("IPFS has already been inititated. Skipping that...")
    else:
        print("Initiating IPFS")
        exit_code = subprocess.call([IPFS_BIN_LOCATION, "init"])
        if exit_code == 0:
            print("Successfully initiated IPFS")
        else:
            print("Failed to initiate IPFS")
            sys.exit(1)



@main.command("add")
def add():
    print("Add")

@main.command("run")
def run():
    print("Run")

@main.command("publish")
def publish():
    print("Publish")


if __name__ == '__main__':
    main()