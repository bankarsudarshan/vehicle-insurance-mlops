from dataclasses import dataclass
import os
from pathlib import Path

from src.constants import *
from src.utils.main_utils import read_yaml_file


params = read_yaml_file(Path("params.yaml"))

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifacts_dir: str = ARTIFACTS_DIR

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, 
        DATA_INGESTION_DIR_NAME
    )
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, 
        DATA_INGESTION_FEATURE_STORE_DIR,
        DATA_INGESTION_RAW_DATA_FILE_NAME
    )
    training_file_path: str = os.path.join(
        data_ingestion_dir, 
        DATA_INGESTION_INGESTED_DIR,
        DATA_INGESTION_TRAIN_FILE_NAME
    )
    testing_file_path: str = os.path.join(
        data_ingestion_dir, 
        DATA_INGESTION_INGESTED_DIR,
        DATA_INGESTION_TEST_FILE_NAME
    )
    database_name: str = params['data_ingestion']['database_name']
    collection_name: str = params['data_ingestion']['collection_name']
    train_test_split_ratio: float = params['data_ingestion']['train_test_split_ratio']
    random_state = params['data_ingestion']['random_state']

@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        DATA_VALIDATION_DIR_NAME
    )
    schema_file_path: str = SCHEMA_FILE_PATH
    validation_report_file_path: str = os.path.join(
        data_validation_dir,
        DATA_VALIDATION_REPORT_FILE_NAME
    )