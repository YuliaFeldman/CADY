from typing import Tuple
from parsers.base_parser import RangeParser


class TemperatureRangeParser(RangeParser):
    def __init__(self) -> None:
        super().__init__(r'[+-–]?\d{1,3}\s?°?\s?C\s?to\s?[+-–]?\d{1,3}\s?°?\s?C')

    def extract_values(self, match: str) -> Tuple[float, float]:
        def clean_value(value: str) -> float:
            value = value.strip()
            if value[0] == '–':
                value = '-' + value[1:]
            return float(value)

        cleaned_str = match.replace('°C', '').replace('to', '')
        temp_values = cleaned_str.split()
        start, end = map(clean_value, temp_values)
        return start, end

