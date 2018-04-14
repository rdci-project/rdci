import os
import subprocess
import tarfile
import time
import re

import click
import requests

IPFS_URL="https://dist.ipfs.io/go-ipfs/v0.4.14/go-ipfs_v0.4.14_linux-amd64.tar.gz"
LOCAL_FILE="go-ipfs.tar.gz"
IPFS_BIN_LOCATION = "go-ipfs/ipfs"


class IPFSException(Exception):
    pass


def download_ipfs():
    r = requests.get(IPFS_URL, stream=True)
    with open(LOCAL_FILE, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    tar = tarfile.open(LOCAL_FILE)
    tar.extractall()
    tar.close()


def run_ipfs_daemon(ipfs_exe):
    process = subprocess.Popen([ipfs_exe, "daemon"])
    time.sleep(5)
    return process


def add_to_ipfs(dir_path):
    process = subprocess.Popen([IPFS_BIN_LOCATION, "add", "-r", "-Q", dir_path])
    exit_code = process.wait()
    if exit_code == 0:
        ipfs_site_hash = process.stdout
        return ipfs_site_hash
    else:
        raise IPFSException("The was a problem adding to IPFS")


def update_ipns_record(site_hash):
    process = subprocess.Popen([IPFS_BIN_LOCATION, "name", "publish", "-Q", site_hash])
    exit_code = process.wait()

    if exit_code == 0:
        stdout = process.stdout
        regex = r"^Published to (\w+)\:\s\/ipfs\/(\w+)$"
        matches = re.finditer(regex, stdout)
        ipns_hash = matches[0]
        return ipns_hash
    else:
        raise IPFSException("The was a problem updating IPNS")


class ipfs_daemon(object):
    """Context manager for launching IPFS daemon."""
    def __init__(self, ipfs_bin):
        self.process = None
        self.ipfs_bin = ipfs_bin
    
    def __enter__(self):
        self.process = run_ipfs_daemon(self.ipfs_bin)
    
    def __exit__(self, etype, value, traceback):
        self.process.terminate()


class cd(object):
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


class Printer(object):

    @classmethod
    def start(cls, message):
        """Print start message."""
        cls.echo(icon='●', tag='start', message=message, color='blue')

    @classmethod
    def info(cls, message):
        """Print info message."""
        cls.echo(icon='ℹ', tag='info', message=message, color='blue')
    
    @classmethod
    def success(cls, message):
        """Print success message."""
        cls.echo(icon='✔', tag='success', message=message, color='green')

    @classmethod
    def warn(cls, message):
        """Print warning message."""
        cls.echo(icon='⚠', tag='warn', message=message, color='yellow')

    @classmethod
    def error(cls, message):
        """Print error message."""
        cls.echo(icon='✖', tag='error', message=message, color='red')
    
    @classmethod
    def ready(cls, message):
        """Print ready message."""
        cls.echo(icon='♥', tag='ready', message=message, color='green')

    @staticmethod
    def echo(icon, tag, message, color):
        prefix = click.style(f"{icon:2} {tag}", fg=color)
        click.echo(f"{prefix:19} {message}")
