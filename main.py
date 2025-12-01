import sys
from src.pipeline.training_pipeline import TrainPipeline
from src.logger import logging

from src.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact, ClassificationMetricArtifact,
)

if __name__ == "__main__":
    try:
        stage_name = sys.argv[1] if len(sys.argv) > 1 else None
        pipeline = TrainPipeline()

        if stage_name == 'data_ingestion':
            logging.info(f">>>>>> Stage {stage_name} started <<<<<<")
            data_ingestion_artifact = pipeline.start_data_ingestion()
            logging.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
            
        elif stage_name == 'data_validation':
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path='artifacts/data_ingestion/ingested/train.csv',
                test_file_path='artifacts/data_ingestion/ingested/test.csv',
            )
            logging.info(f">>>>>> Stage {stage_name} started <<<<<<")
            data_validation_artifact = pipeline.start_data_validation(data_ingestion_artifact)
            logging.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
            
        elif stage_name == 'data_transformation':
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path='artifacts/data_ingestion/ingested/train.csv',
                test_file_path='artifacts/data_ingestion/ingested/test.csv',
            )
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
            
        elif stage_name == 'model_trainer':
            data_transformation_artifact = DataTransformationArtifact(
                transformation_object_file_path = 'artifacts/data_transformation/transformation_objects/preprocessing.pkl',
                transformed_train_file_path = 'artifacts/data_transformation/transformed_data/train.npy',
                transformed_test_file_path = 'artifacts/data_transformation/transformed_data/test.npy'
            )
            
            logging.info(f">>>>>> Stage {stage_name} started <<<<<<")
            model_trainer_artifact = pipeline.start_model_trainer(
                data_transformation_artifact
            )
            logging.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
            
        elif stage_name == 'model_evaluation':
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path='artifacts/data_ingestion/ingested/train.csv',
                test_file_path='artifacts/data_ingestion/ingested/test.csv',
            )
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path='artifacts/model_trainer/trained_model/model.pkl',
                metrics_artifact='ye matter nahi karna chhiye. DEKHTE HAI RUN HOTA HAI KI NAHI',
            )
            
            logging.info(f">>>>>> Stage {stage_name} started <<<<<<")
            model_evaluation_artifact = pipeline.start_model_evaluation(
                data_ingestion_artifact,
                model_trainer_artifact
            )
            logging.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logging.exception(e)
        raise e