from dataclasses import dataclass
from pathlib import Path


#From this can access these are the variables from other file.Consider as an entity. Frozen means cannot change variable values
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir:Path
    base_model_path:Path
    updated_base_model_path:Path
    params_image_size:list
    params_learning_rate:float
    params_include_top:bool
    params_weights:str
    params_classes:int


@dataclass(frozen=True)
class TrainingConfg:
    root_dir:Path
    trained_model_path:Path
    updated_base_model_path:Path   #saved model
    training_data:Path    #images to train
    params_epochs:int
    params_batch_size:int
    params_is_augmentation:bool
    params_image_size:list
