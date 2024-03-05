from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.components.data_ingestion import DataIngestion
from cnn_classifier import logger   

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_ingesion_config=config.get_data_ingestion_config()
        data_ingesion=DataIngestion(config=data_ingesion_config)
        data_ingesion.download_file()
        data_ingesion.extract_zip_file()


if __name__=='__main__':
    try:
        logger.info(f">>>>>>>  {STAGE_NAME} started <<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>  {STAGE_NAME} completed <<<<<<<\n\n x===========x")
    except Exception as e:
        logger.exception(e)
        raise e
    