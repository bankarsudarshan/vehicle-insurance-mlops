import sys
from src.pipeline.training_pipeline import TrainPipeline
from src.logger import logging

from src.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)

if __name__ == "__main__":
    try:
        stage_name = sys.argv[1] if len(sys.argv) > 1 else None
        pipeline = TrainPipeline()

        data_ingestion_artifact = None
        data_validation_artifact = None
        data_transformation_artifact = None

        if stage_name == 'data_ingestion':
            logging.info(f">>>>>> Stage {stage_name} started <<<<<<")
            data_ingestion_artifact = pipeline.start_data_ingestion()
            logging.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
            
        elif stage_name == 'data_validation':
            if data_ingestion_artifact is None:
                data_ingestion_artifact = DataIngestionArtifact(
                    train_file_path='artifacts/data_ingestion/ingested/train.csv',
                    test_file_path='artifacts/data_ingestion/ingested/test.csv',
                )
            logging.info(f">>>>>> Stage {stage_name} started <<<<<<")
            data_validation_artifact = pipeline.start_data_validation(data_ingestion_artifact)
            logging.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
            
        elif stage_name == 'data_transformation':
            if data_ingestion_artifact is None:
                data_ingestion_artifact = DataIngestionArtifact(
                    train_file_path='artifacts/data_ingestion/ingested/train.csv',
                    test_file_path='artifacts/data_ingestion/ingested/test.csv',
                )
            if data_validation_artifact is None:
                data_validation_artifact = DataValidationArtifact(
                    validation_status = True,
                    message = "Dummy validation artifact",
                    report_file_path= "iski real value ki koi jarurat nahi hai shayad"
                )
            logging.info(f">>>>>> Stage {stage_name} started <<<<<<")
            data_transformation_artifact = pipeline.start_data_transformation(
                data_ingestion_artifact,
                data_validation_artifact
            )
            logging.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logging.exception(e)
        raise e