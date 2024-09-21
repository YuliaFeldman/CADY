import pytest
from parsers.voltage_parser import VoltageRangeParser
from parsers.temperature_parser import TemperatureRangeParser


def test_voltage_range_parser():
    parser = VoltageRangeParser()
    content = "3.3V to 5V"
    result = parser.parse(content)
    assert result == (3.3, 5.0)


def test_temperature_range_parser():
    parser = TemperatureRangeParser()
    content = "-30°C to –20°C"
    result = parser.parse(content)
    assert result == (-30.0, -20.0)
