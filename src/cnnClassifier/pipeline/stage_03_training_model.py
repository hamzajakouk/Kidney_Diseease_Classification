from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training_model import Training
from cnnClassifier import logger


STAGE_NAME = 'Data Ingestion stage'

class ModelTrainingTrainingPipeline:
    def __init__(self) :
        pass

    def main(self):   
        config = ConfigurationManager()
        training_model_config = config.get_training_config()
        training_model = Training(config=training_model_config)
        training_model.get_base_model()
        training_model.train_valid_generator()
        training_model.train()
    
