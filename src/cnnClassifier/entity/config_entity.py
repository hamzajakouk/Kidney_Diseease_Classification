from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data: Path
    unzip_dir: Path



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path : Path
    update_base_model_path : Path
    params_image_size : list
    params_learning_rate : float
    params_include_top : bool
    params_weights : str
    params_classes : int    