from typing import Tuple
from parsers.base_parser import RangeParser


class VoltageRangeParser(RangeParser):
    def __init__(self) -> None:
        super().__init__(r'(\d+(\.\d+)?\s*V)\s*to\s*(\d+(\.\d+)?\s*V)')

    def extract_values(self, match: str) -> Tuple[float, float]:
        start = float(match[0].replace('V', '').strip())
        end = float(match[2].replace('V', '').strip())
        return start, end
