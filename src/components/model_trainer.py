import sys
from typing import Tuple

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from src.exception import MyException
from src.logger import logging
from src.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact, ClassificationMetricArtifact
from src.entity.config_entity import ModelTrainerConfig
from src.entity.estimator import MyModel
from src.utils.main_utils import load_numpy_array_data, load_object, save_object

class ModelTrainer:
    def __init__(
            self,
            data_transformation_artifact: DataTransformationArtifact,
            model_trainer_config: ModelTrainerConfig
        ):
        """
        :param data_transformation_artifact: Output reference of data transformation artifact stage
        :param model_trainer_config: Configuration for model training
        """
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config

    def get_model_object_and_report(self, train: np.array, test: np.array) -> Tuple[object, object]:
        """
        This function trains a RandomForestClassifier with specified parameters and
        outputs metric artifact object and trained model object
        """
        try:
            logging.info("Training RandomForestClassifier with specified parameters")

            x_train, y_train, x_test, y_test = train[:, :-1], train[:, -1], test[:, :-1], test[:, -1]
            logging.info("train-test split done.")

            params = self.model_trainer_config.params
            model = RandomForestClassifier(
                n_estimators = params['n_estimators'],
                min_samples_split = params['min_samples_split'],
                min_samples_leaf = params['min_samples_leaf'],
                max_depth = params['max_depth'],
                criterion = params['criterion'],
                random_state = params['random_state']
            )
            logging.info("RandomForestClassifier model initialized")

            logging.info("Model training started...")
            model.fit(x_train, y_train)
            logging.info("Model training done.")

            # Predictions and evaluation metrics
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)

            metrics_artifact = ClassificationMetricArtifact(
                f1_score=f1, 
                accuracy=accuracy, 
                precision_score=precision, 
                recall_score=recall
            )
            return model, metrics_artifact
        
        except Exception as e:
            raise MyException(e, sys) from e

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        """
        This function initiates the model training steps
        outputs model trainer artifact
        """
        try:
            logging.info("--- Starting Model Trainer Component ---")
            
            train_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_file_path)
            test_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_file_path)
            logging.info("train-test data loaded")
            
            trained_model, metrics_artifact = self.get_model_object_and_report(train=train_arr, test=test_arr)
            logging.info("trained model and metrics artifact loaded.")
            
            preprocessing_obj = load_object(file_path=self.data_transformation_artifact.transformation_object_file_path)
            logging.info("Preprocessing obj loaded.")

            if metrics_artifact.accuracy < self.model_trainer_config.expected_accuracy:
                logging.info("No model found with score above the base score")
                raise Exception("No model found with score above the base score")

            logging.info("Saving new model as performace is better than previous one")
            my_model = MyModel(preprocessing_object=preprocessing_obj, trained_model_object=trained_model)
            save_object(self.model_trainer_config.trained_model_file_path, my_model)
            logging.info("Saved final model object that includes both preprocessing and the trained model")

            # Create and return the ModelTrainerArtifact
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path = self.model_trainer_config.trained_model_file_path,
                metrics_artifact = metrics_artifact,
            )
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        
        except Exception as e:
            raise MyException(e, sys) from e