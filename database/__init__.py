from pymongo import MongoClient
from pymongo.server_api import ServerApi

from . import errorHandler

class DatabaseManager:
    def __init__(self, connection: str):
        print("Hello this is Database Module")

    def createConnection(self, connection: str):
        self.connection = MongoClient(connection, server_api=ServerApi('1'))

        try:
            self.connection.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

            self.db           = self.connection["minibank"]
            self.collection   = self.db["users"]
        except Exception as e:
            print(e)


    def withdraw(self, user: str, value: int):
        try:
            if self.collection.find_one({'name': user}) is None:
                raise errorHandler.userNotFound(user)
            elif value <= 0:
                raise errorHandler.negativeuserBalance(value)
            elif self.collection.find_one({'name': user})["money"] <= 0:
                raise errorHandler.brokeAlert(value)
            else:
                self.collection.update_one({'name': user}, {'$inc': {'money': -value}})
        except Exception as e:
            print(e)

    def deposit(self, user: str, value: int):
        try:
            if self.collection.find_one({'name': user}) is None:
                raise errorHandler.userNotFound(user)
            elif value <= 0:
                raise errorHandler.negativeuserBalance(value)
            elif self.collection.find_one({'name': user})["money"] <= 0:
                raise errorHandler.brokeAlert(value)
            else:
                self.collection.update_one({'name': user}, {'$inc': {'money': value}})
        except Exception as e:
            print(e)

    def changePIN(self, user: str, pin: int):
        try:
            if self.collection.find_one({'name': user}) is None:
                raise errorHandler.userNotFound(user)
            else:
                self.collection.update_one({'name': user}, {'$set': {'pin': pin}})
        except Exception as e:
            print(e)

    def transfer(self, user: str, target: str, value: int):
        try:
            # Check user
            if self.collection.find_one({'name': user}) is None:
                raise errorHandler.userNotFound(user)
            # Check Target user
            elif self.collection.find_one({'name': target}) is None: 
                raise errorHandler.userNotFound(user)
            # Check if the value is negative
            elif value <= 0:
                raise errorHandler.negativeuserBalance(value)
            # Check the if the balance less than 0
            elif self.collection.find_one({'name': user})["money"] <= 0:
                raise errorHandler.brokeAlert(value)
            else:
                self.collection.update_one({'name': target}, {'$inc': {'money': value}})
                self.collection.update_one({'name': user}, {'$inc': {'money': -value}})
        except Exception as e:
            print(e)