from HealthcareChatbot.entity.config_entity import DataBaseConfig
from HealthcareChatbot.utils.common import read_yaml
from HealthcareChatbot.constants import *

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config_file_path = config_file_path
        self.params_filepath = params_filepath
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_filepath)

    def get_database_config(self) -> DataBaseConfig:
        return DataBaseConfig(
            host=self.config.database_config.host,
            user=self.config.database_config.user,
            password=self.config.database_config.password,
            database=self.config.database_config.database,
        )
    
    def get_model_config(self):
        return self.config.model_config
    
if __name__ == "__main__":
    config_manager = ConfigurationManager()
    print(config_manager.get_database_config())