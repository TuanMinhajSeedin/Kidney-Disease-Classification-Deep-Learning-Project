from src.cnn_classifier import logger
from src.cnn_classifier.pipeline.stage_01_data_ingesion import DataIngestionTrainingPipeline
from src.cnn_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnn_classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnn_classifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>>>  {STAGE_NAME} started <<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>  {STAGE_NAME} completed <<<<<<<\n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e
    



STAGE_NAME="Prepare Base Model Stage"
try:
    logger.info(f">>>>>>>  {STAGE_NAME} started <<<<<<<")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>  {STAGE_NAME} completed <<<<<<<\n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Traininge"
try:
    logger.info(f">>>>>>>  {STAGE_NAME} started <<<<<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>  {STAGE_NAME} completed <<<<<<<\n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e

