from dataclasses import dataclass
from pathlib import Path
#entity: it is the return type of a classes
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path