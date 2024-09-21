from components.component_parser import ComponentParser
from parsers.temperature_parser import TemperatureRangeParser
from parsers.voltage_parser import VoltageRangeParser
from components.component_finder import ComponentFinder


class ComponentsManager:
    def __init__(self):
        self.directory = 'task_example_files'
        self.parsers = [VoltageRangeParser(), TemperatureRangeParser()]
        self.component_parser = ComponentParser(self.directory, self.parsers)
        self.components = self.component_parser.read_and_parse_files()

    def find_operable_components(self, voltage: float, temperature: float):
        operable_components = ComponentFinder.find_operable_components(self.components, voltage=voltage, temperature=temperature)
        return operable_components