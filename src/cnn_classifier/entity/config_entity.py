from dataclasses import dataclass
from pathlib import Path


#From this can access these are the variables from other file.Consider as an entity. Frozen means cannot change variable values
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

