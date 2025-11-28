import sys
from src.pipeline.training_pipeline import TrainPipeline
from src.logger import logging

if __name__ == "__main__":
    try:
        stage_name = sys.argv[1] if len(sys.argv) > 1 else None
        pipeline = TrainPipeline()

        if stage_name == 'data_ingestion':
            logging.info(f">>>>>> Stage {stage_name} started <<<<<<")
            pipeline.start_data_ingestion()
            logging.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
            
        # elif stage_name == 'data_validation': ...

    except Exception as e:
        logging.exception(e)
        raise e