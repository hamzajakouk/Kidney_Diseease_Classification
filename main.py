from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training_model import ModelTrainingTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation_model import EvaluationModelTrainingPipeline
from cnnClassifier import logger



STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<") 
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e    


STAGE_NAME = 'Prepare Base Model Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<") 
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e    

STAGE_NAME = 'Model Training Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<") 
    obj = ModelTrainingTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e    

STAGE_NAME = 'Model Evaluation Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<") 
    obj = EvaluationModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e   