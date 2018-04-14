import subprocess
import sys
import os.path
import os
import tempfile

import click
from mkdocs.commands.serve import serve

from hfs2018.utils import (download_ipfs, IPFS_BIN_LOCATION, run_ipfs_daemon,
                           add_to_ipfs, cd, Printer)
from hfs2018.site import setup_site


@click.group()
def main():
    pass


@main.command()
@click.argument('output_dir', type=click.Path(exists=False))
@click.argument('name', required=False)
def init(output_dir, name=None):
    Printer.start(f"Setting up new site: {output_dir}")
    if not os.path.exists(IPFS_BIN_LOCATION):
        Printer.warn("You don't have IPFS. Don't worry I'll download it for you...")
        download_ipfs()

    if os.path.exists(os.path.join(os.environ.get("HOME"), ".ipfs")):
        Printer.info("IPFS has already been inititated. Skipping that...")
    else:
        Printer.info("Initiating IPFS")
        exit_code = subprocess.call([IPFS_BIN_LOCATION, "init"])
        if exit_code == 0:
            Printer.success("Successfully initiated IPFS")
        else:
            Printer.error("Failed to initiate IPFS")
            sys.exit(1)
    
    Printer.ready('New site setup successfully!')
    setup_site(output_dir, name=name)
    Printer.info('To preview your site, run:')
    Printer.info(f"hfs2018 run {output_dir}")


@main.command()
@click.pass_context
def add(context):
    if not os.path.exists(IPFS_BIN_LOCATION):
        Printer.error("Please run hfs2018 init first..")
        context.abort()

    ipfs_daemon_process = run_ipfs_daemon()
    fh = click.edit()
    add_to_ipfs(fh)
    ipfs_daemon_process.terminate()


@main.command()
@click.argument('directory', type=click.Path(exists=True))
def run(directory):
    """Start the development server to preview output."""
    with cd(directory):
        serve()


@main.command()
def publish():
    Printer.start("Publish")


if __name__ == '__main__':
    main()