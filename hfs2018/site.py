"""
# Hello World

This content is _very_ important.
"""
import os

import click
import yaml

from hfs2018.utils import Printer

def setup_site(output_dir, name=None):
    """Setup a new site."""
    data_dir = os.path.join(output_dir, 'data')
    config_path = os.path.join(output_dir, 'mkdocs.yml')
    first_page_path = os.path.join(data_dir, 'index.md')

    if os.path.exists(data_dir):
        click.secho(f"directory alredy exists: {data_dir}", color="red")
        return

    os.makedirs(data_dir, exist_ok=True)

    config_data = {
        'site_name': name or os.path.basename(output_dir),
        'theme': {
            'name': 'material',
            'custom_dir': 'theme',
        },
        'docs_dir': 'data',
        'markdown_extensions': [
            'meta'
        ]
    }

    with open(config_path, 'w') as handle:
        yaml.dump(
            config_data,
            stream=handle,
            indent=2,
            default_flow_style=False,
            allow_unicode=True,
        )
    
    with open(first_page_path, 'w') as handle:
        handle.write(__doc__)


def add_content(output_dir, name):
    """Add new content to the site."""
    message = edit_content(name=name)
    file_path = os.path.join(output_dir, 'data', f"{name}.md")
    if os.path.exists(file_path):
        raise OSError(f"File already exists: {file_path}")

    with open(file_path, 'w') as handle:
        handle.write(message)

def edit_content(name=None):
    template = f"""# {name or 'title'}

Text...
    """
    MARKER = '# Everything below is ignored\n'
    message = click.edit(f'{template}\n\n' + MARKER)
    if message is not None:
        return message.split(MARKER, 1)[0].rstrip('\n')
