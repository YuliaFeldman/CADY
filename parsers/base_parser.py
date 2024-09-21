import re
from typing import Tuple, Optional


class RangeParser:
    def __init__(self, regex_pattern: str) -> None:
        self.regex = re.compile(regex_pattern)

    def parse(self, content: str) -> Optional[Tuple[float, float]]:
        matches = self.regex.findall(content)
        ranges = set()
        for m in matches:
            try:
                start, end = self.extract_values(m)
                ranges.add((start, end))
            except ValueError:
                continue
        return ranges.pop() if len(ranges) == 1 else None

    def extract_values(self, match: str) -> Tuple[float, float]:
        raise NotImplementedError("This method must be implemented by subclasses")