import subprocess
import sys
import os.path
import os
import tempfile

import click


from hfs2018.utils import download_ipfs, IPFS_BIN_LOCATION, run_ipfs_daemon, add_to_ipfs


@click.group()
def main():
    pass

@main.command("init")
def init():
    if not os.path.exists(IPFS_BIN_LOCATION):
        click.echo("You don't have IPFS. Don't worry I'll download it for you...")
        download_ipfs()

    if os.path.exists(os.path.join(os.environ.get("HOME"), ".ipfs")):
        click.echo("IPFS has already been inititated. Skipping that...")
    else:
        click.echo("Initiating IPFS")
        exit_code = subprocess.call([IPFS_BIN_LOCATION, "init"])
        if exit_code == 0:
            click.echo("Successfully initiated IPFS")
        else:
            click.echo("Failed to initiate IPFS")
            sys.exit(1)



@main.command("add")
def add():
    if not os.path.exists(IPFS_BIN_LOCATION):
        click.echo("Please run hfs2018 init first..")
        sys.exit(1)

    ipfs_daemon_process = run_ipfs_daemon()
    fh = click.edit()
    add_to_ipfs(fh)
    ipfs_daemon_process.terminate()


@main.command("run")
def run():
    click.echo("Run")

@main.command("publish")
def publish():
    click.echo("Publish")


if __name__ == '__main__':
    main()