from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path

from src.constants import *
from src.utils.main_utils import read_yaml_file


params = read_yaml_file(Path("params.yaml"))

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = ARTIFACT_DIR

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifact_dir, 
        params['data_ingestion']['dir_name']
    )
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, 
        params['data_ingestion']['feature_store_dir'], 
        params['data_ingestion']['raw_data_file']
    )
    training_file_path: str = os.path.join(
        data_ingestion_dir, 
        params['data_ingestion']['ingested_dir'], 
        params['data_ingestion']['train_file']
    )
    testing_file_path: str = os.path.join(
        data_ingestion_dir, 
        params['data_ingestion']['ingested_dir'], 
        params['data_ingestion']['test_file']
    )
    train_test_split_ratio: float = params['data_ingestion']['train_test_split_ratio']
    collection_name: str = params['data_ingestion']['collection_name']