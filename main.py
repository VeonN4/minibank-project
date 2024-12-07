from database import DatabaseManager
from database import userHandler
import dotenv

connection = dotenv.get_key(".env", "MONGODB_ADDRESS")
client = DatabaseManager.createConnection(connection)

def menu():
    pass

def choiceHandler(choice: int):
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

def loginPrompt():
    user = input("Enter your name: ")
    password = input("Enter your name: ")

    if userHandler.validateUser(user, password) == 1:
        pass
    else:
        pass



