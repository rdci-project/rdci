"""
# Hello World

This content is _very_ important.
"""
import os

import click
import yaml

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
        'theme': 'material',
        'docs_dir': 'data',
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
    click.edit()
