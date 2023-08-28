from dataclasses import dataclass
from pathlib import Path


#entity: it is the return type of a classes of data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


 #entity of data validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list