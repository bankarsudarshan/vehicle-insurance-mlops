from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    train_file_path: str 
    test_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformation_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ClassificationMetricArtifact:
    f1_score: float
    accuracy: float
    precision_score: float
    recall_score: float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str 
    metrics_artifact: ClassificationMetricArtifact