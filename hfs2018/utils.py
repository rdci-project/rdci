import os
import subprocess
import tarfile
import time

import click
import requests

IPFS_URL="https://dist.ipfs.io/go-ipfs/v0.4.14/go-ipfs_v0.4.14_linux-amd64.tar.gz"
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


def run_ipfs_daemon():
    process = subprocess.Popen([IPFS_BIN_LOCATION, "daemon"])
    time.sleep(5)
    return process

def add_to_ipfs(file_content):
    process = subprocess.Popen([IPFS_BIN_LOCATION, "add"], stdin=subprocess.PIPE)
    process.stdin.write(bytes(file_content, encoding="UTF-8"))
    process.stdin.close()
    exit_code = process.wait()
    if exit_code == 0:
        return True
    else:
        return False

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


class Printer():

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
        prefix = click.style(f"{icon:3} {tag}", fg=color)
        click.echo(f"{prefix:19} {message}")
