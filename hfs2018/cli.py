import shutil
import subprocess
import sys
import os.path
import os

import click

from hfs2018.utils import download_ipfs


@click.group()
def main():
    pass

@main.command("init")
def init():
    if not shutil.which("ipfs"):
        print("IPFS is not on path. Please add it...")
        download_ipfs()

    if os.path.exists(os.path.join(os.environ.get("HOME"), ".ipfs")):
        print("IPFS has already been inititated. Skipping that...")
    else:
        print("Initiating IPFS")
        exit_code = subprocess.call(["ipfs", "init"])
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