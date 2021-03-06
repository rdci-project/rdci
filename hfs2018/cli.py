import subprocess
import sys
import os.path
import os
import tempfile
import shutil

import click
from mkdocs.commands.serve import serve
from mkdocs.commands.build import build
from mkdocs.config import load_config

from hfs2018.utils import (download_ipfs, IPFS_BIN_LOCATION, ipfs_daemon,
                           add_to_ipfs, cd, Printer, update_ipns_record)
from hfs2018.site import setup_site, add_content

DEFAULT_SITE_DIR = './content'
IPFS_BIN = shutil.which('ipfs') or IPFS_BIN_LOCATION


@click.group()
def main():
    pass


@main.command()
@click.argument('name')
def init(name):
    Printer.start(f"Setting up new site: {DEFAULT_SITE_DIR}")
    if not os.path.exists(IPFS_BIN):
        Printer.warn("You don't have IPFS. Don't worry I'll download it for you...")
        download_ipfs()

    if os.path.exists(os.path.join(os.environ.get("HOME"), ".ipfs")):
        Printer.info("IPFS has already been inititated. Skipping that...")
    else:
        Printer.info("Initiating IPFS")
        exit_code = subprocess.call([IPFS_BIN, "init"])
        if exit_code == 0:
            Printer.success("Successfully initiated IPFS")
        else:
            Printer.error("Failed to initiate IPFS")
            sys.exit(1)
    
    Printer.ready('New site setup successfully!')
    setup_site(DEFAULT_SITE_DIR, name=name)
    Printer.info('To preview your site, run:')
    Printer.info('hfs2018 run')


@main.command()
@click.pass_context
@click.option('--skip_update_ipns', default=False, is_flag=True)
def publish(context, skip_update_ipns):
    Printer.start("Publishing your site to IPFS...")
    with cd(DEFAULT_SITE_DIR):
        Printer.info("Building site...")
        build(load_config(config_file='./mkdocs.yml'))

    if not os.path.exists(IPFS_BIN):
        Printer.error("Please run 'hfs2018 init' first")
        context.abort()

    Printer.info('Uploading to IPFS and updating IPNS record (optional). This may take some time...')
    with ipfs_daemon(IPFS_BIN):
        site_output_dir = os.path.join(DEFAULT_SITE_DIR, "site")
        Printer.info("We are uploading the site to IPFS now...")
        site_hash = add_to_ipfs(site_output_dir)
        Printer.info(f"The site is available at https://gateway.ipfs.io/ipfs/{site_hash}")

        if not skip_update_ipns:
            Printer.info("We are updating the IPNS record now...")
            ipns_hash = update_ipns_record(site_hash)

            Printer.ready(f'Your site is available on IPNS! You can reach it via:'
                          f' https://gateway.ipfs.io/ipns/{ipns_hash}')


@main.command()
def run():
    """Start the development server to preview output."""
    with cd(DEFAULT_SITE_DIR):
        serve()


@main.command()
@click.argument('name')
@click.pass_context
def add(context, name):
    Printer.start("Add new content...")
    if not os.path.exists(DEFAULT_SITE_DIR):
        Printer.error("Please run 'hfs2018 init' first")
        context.abort()
    try:
        add_content(DEFAULT_SITE_DIR, name)
    except OSError as error:
        Printer.error(error.args[0])
        context.abort()
    Printer.success("New content added to site!")


if __name__ == '__main__':
    main()