import os


PIPELINE_NAME: str = ""
ARTIFACTS_DIR: str = "artifacts"
MONGODB_URL_KEY = "MONGODB_URL"

"""
Data Ingestion related constants
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
RAW_DATA_FILE_NAME: str = "raw_data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
Data Validation related contants
"""
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
DATA_VALIDATION_REPORT_FILE_NAME: str = "validation_report.json"

"""
Data Transformation related constants
"""
TARGET_COLUMN: str = "Response"
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
TRANSFORMED_DATA_DIR: str = "transformed_data"
TRANSFORMATION_OBJECTS_DIR: str = "transformation_objects"
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"

"""
Model Trainer related constants
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"