import pytest
from components.component_parser import ComponentParser
from components.component_finder import ComponentFinder
from components.components_manager import ComponentsManager
from parsers.temperature_parser import TemperatureRangeParser
from parsers.voltage_parser import VoltageRangeParser


def test_component_parser(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    file = d / "test.txt"
    file.write_text("3.3V to 5.5V\n–30°C to -20°C")

    parsers = [VoltageRangeParser(), TemperatureRangeParser()]
    component_parser = ComponentParser(d, parsers)
    components = component_parser.read_and_parse_files()

    assert "test.txt" in components
    assert components["test.txt"]["voltage"] == (3.3, 5.5)
    assert components["test.txt"]["temperature"] == (-30.0, -20.0)


def test_find_operable_components():
    components = {
        "component1.txt": {"voltage": (3.3, 5.0), "temperature": (-20.0, 30.0)},
        "component2.txt": {"voltage": (1.0, 2.0), "temperature": (10.0, 15.0)}
    }
    operable = ComponentFinder.find_operable_components(components, voltage=4.0, temperature=25.0)
    assert operable == ["component1.txt"]


def test_components_manager(monkeypatch):
    def mock_read_and_parse_files(self):
        return {
            "component1.txt": {"voltage": (3.3, 5.0), "temperature": (-20.0, 30.0)},
            "component2.txt": {"voltage": (1.0, 2.0), "temperature": (-10.0, 15.0)}
        }
    monkeypatch.setattr(ComponentParser, "read_and_parse_files", mock_read_and_parse_files)
    manager = ComponentsManager()
    operable = manager.find_operable_components(voltage=4.0, temperature=25.0)
    assert operable == ["component1.txt"]