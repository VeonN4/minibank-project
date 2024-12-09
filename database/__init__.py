from pymongo import MongoClient
from pymongo.server_api import ServerApi

from . import errorHandler

class DatabaseManager:
    connection = None
    db = None
    collection = None

    @classmethod
    def initialize(cls, connection_string):
        """Initialize the database connection."""
        cls.connection = MongoClient(connection_string, server_api=ServerApi('1'))

        try:
            cls.connection.admin.command('ping')
            print("Succesfully connected to database!")

            cls.db = cls.connection["minibank"]
            cls.collection = cls.db["users"]
        except Exception as e:
            print(e)
            exit()

    @staticmethod
    def withdraw(user: str, value: int):
        try:
            if DatabaseManager.collection.find_one({'name': user}) is None:
                raise errorHandler.userNotFound(user)
            elif value <= 0:
                raise errorHandler.negativeuserBalance(value)
            elif DatabaseManager.collection.find_one({'name': user})["money"] <= 0:
                raise errorHandler.brokeAlert(value)
            else:
                DatabaseManager.collection.update_one({'name': user}, {'$inc': {'money': -value}})
        except Exception as e:
            print(e)

    @staticmethod
    def deposit(user: str, value: int):
        try:
            if DatabaseManager.collection.find_one({'name': user}) is None:
                raise errorHandler.userNotFound(user)
            elif value <= 0:
                raise errorHandler.negativeuserBalance(value)
            elif DatabaseManager.collection.find_one({'name': user})["money"] <= 0:
                raise errorHandler.brokeAlert(value)
            else:
                DatabaseManager.collection.update_one({'name': user}, {'$inc': {'money': value}})
        except Exception as e:
            print(e)

    @staticmethod
    def changePIN(user: str, pin: int):
        try:
            if DatabaseManager.collection.find_one({'name': user}) is None:
                raise errorHandler.userNotFound(user)
            else:
                DatabaseManager.collection.update_one({'name': user}, {'$set': {'pin': pin}})
        except Exception as e:
            print(e)

    @staticmethod
    def transfer(user: str, target: str, value: int):
        try:
            # Check user
            if DatabaseManager.collection.find_one({'name': user}) is None:
                raise errorHandler.userNotFound(user)
            # Check Target user
            elif DatabaseManager.collection.find_one({'name': target}) is None: 
                raise errorHandler.userNotFound(target)
            # Check if the target transfer money to himself
            elif user == target:
                print("You can't transfer money to your account!")
            # Check if the value is negative
            elif value <= 0:
                raise errorHandler.negativeuserBalance(value)
            # Check if the balance is less than 0
            elif DatabaseManager.collection.find_one({'name': user})["money"] <= 0:
                raise errorHandler.brokeAlert(value)
            else:
                DatabaseManager.collection.update_one({'name': target}, {'$inc': {'money': value}})
                DatabaseManager.collection.update_one({'name': user}, {'$inc': {'money': -value}})
        except Exception as e:
            print(e)