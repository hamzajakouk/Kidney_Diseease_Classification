from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation_model import Evaluation
from cnnClassifier import logger

STAGE_NAME = 'Model Evaluation stage'

class EvaluationModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        Evaluation_model_config = config.get_evaluation_config()
        Evaluation_model = Evaluation(config=Evaluation_model_config)
        Evaluation_model.evaluation()
        Evaluation_model.save_score()
        #Evaluation_model.log_into_mlflow()

STAGE_NAME = 'Modul Evaluation stage'
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<") 
        obj = EvaluationModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e  