from HealthcareChatbot.config.configuration import ConfigurationManager
from HealthcareChatbot import logger
import mysql.connector

config_manager = ConfigurationManager()

class DataBase:
    def __init__(self, config_manager= config_manager):
        self.config_manager = config_manager
    
    def fetch_database(self):
        config = self.config_manager.get_database_config()
        mydb = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        return mydb
    
if __name__ == "__main__":
    database = DataBase()
    db = database.fetch_database()   
    logger.info("Database connection established")