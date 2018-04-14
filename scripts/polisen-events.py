import os
import json

import requests
from jinja2 import Template


def get_events():
    """Get the latest events from the API."""
    response = requests.get('https://polisen.se/H4S-2018-handelser.json')
    response.encoding = 'utf-8-sig'
    data = json.loads(response.text)
    return data[:50]


def convert_event(event):
    """Convert an event to Markdown format."""
    with open('./scripts/template.j2') as handle:
        template = Template(handle.read())

    string = template.render(**event)
    return string


def process_events(data_dir):
    """Process all events."""
    events = get_events()
    for event in events:
        event_md = convert_event(event)
        out_path = os.path.join(data_dir, f"{event['id']}.md")
        with open(out_path, 'w') as handle:
            handle.write(event_md)


def main():
    process_events('./content/content/post')

if __name__ == '__main__':
    main()
