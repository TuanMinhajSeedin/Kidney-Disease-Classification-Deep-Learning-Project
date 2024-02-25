from src.cnn_classifier import logger
from src.cnn_classifier.pipeline.stage_01_data_ingesion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>>>  {STAGE_NAME} started <<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>  {STAGE_NAME} completed <<<<<<<\n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e
    