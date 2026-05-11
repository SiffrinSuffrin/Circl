from dataclasses import dataclass
from pathlib import Path

@dataclass
class SourcecodeInfo:
    from_line: int = 0
    to_line: int = 0
    from_position: int = 0
    to_position: int = 0
    file: str | Path = "<stdin>"
    def __copy__(self):
        return SourcecodeInfo(self.from_line, self.to_line, self.from_position, self.to_position, self.file)