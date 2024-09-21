import os
from typing import List

from parsers.base_parser import RangeParser


class ComponentParser:
    def __init__(self, directory: str, parsers: List[RangeParser]) -> None:
        self.directory = directory
        self.parsers = parsers

    def read_and_parse_files(self):
        components = {}
        for filename in os.listdir(self.directory):
            if filename.endswith('.txt'):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    content = file.read()
                    component_ranges = {}
                    for parser in self.parsers:
                        range_type = parser.__class__.__name__.replace('RangeParser', '').lower()
                        component_ranges[range_type] = parser.parse(content)
                    components[filename] = component_ranges
        return components
