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
        RAW_DATA_FILE_NAME
    )
    training_file_path: str = os.path.join(
        data_ingestion_dir, 
        DATA_INGESTION_INGESTED_DIR,
        TRAIN_FILE_NAME
    )
    testing_file_path: str = os.path.join(
        data_ingestion_dir, 
        DATA_INGESTION_INGESTED_DIR,
        TEST_FILE_NAME
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

@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        DATA_TRANSFORMATION_DIR_NAME
    )
    transformed_train_file_path: str = os.path.join(
        data_transformation_dir,
        TRANSFORMED_DATA_DIR,
        TRAIN_FILE_NAME.replace("csv", "npy")
    )
    transformed_test_file_path: str = os.path.join(
        data_transformation_dir,
        TRANSFORMED_DATA_DIR,
        TEST_FILE_NAME.replace("csv", "npy")
    )
    transformation_object_file_path: str = os.path.join(
        data_transformation_dir,
        TRANSFORMATION_OBJECTS_DIR,
        PREPROCSSING_OBJECT_FILE_NAME
    )

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        MODEL_TRAINER_DIR_NAME
    )
    trained_model_file_path: str = os.path.join(
        model_trainer_dir,
        MODEL_TRAINER_TRAINED_MODEL_DIR,
        TRAINED_MODEL_FILE_NAME
    )
    expected_accuracy: float = params['model_trainer']['expected_score']
    params = params['model_trainer']['model_params']

@dataclass
class ModelEvaluationConfig:
    changed_threshold_score: float = params['model_evaluation']['changed_threshold_score']
    bucket_name: str = MODEL_BUCKET_NAME
    s3_model_key_path: str = TRAINED_MODEL_FILE_NAME

@dataclass
class ModelPusherConfig:
    bucket_name: str = MODEL_BUCKET_NAME
    s3_model_key_path: str = TRAINED_MODEL_FILE_NAME