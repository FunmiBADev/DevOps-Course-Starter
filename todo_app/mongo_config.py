import os

class MongoDBConfig:
    """ Mongo API Data Configuration variables """

    def __init__(self):
        self.PRIMARY_CONNECTION_STRING = os.environ.get('PRIMARY_CONNECTION_STRING')
        self.MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
        self.COLLECTION_NAME = os.environ.get('COLLECTION_NAME')
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError(
                "No SECRET_KEY set for Flask application. Did you follow the setup instructions?")