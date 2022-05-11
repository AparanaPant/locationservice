
import os


class Config:
    DB_SERVER = os.environ.get('DB_HOST')
    DB_DATABASE_NAME = os.environ.get('DB_NAME')
    DB_PORT = os.environ.get('DB_PORT')
    DB_DATABASE_PASSWORD = os.environ.get('DB_PASSWORD')

    @property
    def MONGO_URI(self):
        return "mongodb+srv://jeevee:root@cluster0.e7fnc.mongodb.net/location?retryWrites=true&w=majority"
        # return f"mongodb+srv://{self.DB_SERVER}:{self.DB_DATABASE_PASSWORD}@cluster0.e7fnc.mongodb.net/{
        # self.DB_DATABASE_NAME}?retryWrites=true&w=majority " return f"mongodb://{self.DB_SERVER}:{self.DB_PORT}/{
        # self.DB_DATABASE_NAME}"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False