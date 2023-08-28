from EndtoEndTextSummerizer.config.configuration import ConfigurationManager
from EndtoEndTextSummerizer.components.data_validation import DataValidation
from EndtoEndTextSummerizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()