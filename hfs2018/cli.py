

# Init
# - Check if ipfs is installed
# - Check if static site exists

import click

@click.command()
def run():
    print("Hello Init!")

if __name__ == '__main__':
    run()