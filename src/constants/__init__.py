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
DATA_INGESTION_RAW_DATA_FILE_NAME: str = "raw_data.csv"
DATA_INGESTION_TRAIN_FILE_NAME: str = "train.csv"
DATA_INGESTION_TEST_FILE_NAME: str = "test.csv"

"""
Data Validation realted contants
"""
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
DATA_VALIDATION_REPORT_FILE_NAME: str = "validation_report.json"