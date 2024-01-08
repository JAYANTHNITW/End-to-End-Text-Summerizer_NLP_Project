from src.EndtoEndTextSummerizer.config.configuration import ConfigurationManager
from src.EndtoEndTextSummerizer.components.model_training import ModelTrainer
from src.EndtoEndTextSummerizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config = model_trainer_config)
        model_trainer_config.train()

