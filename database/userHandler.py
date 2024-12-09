from . import DatabaseManager

def validateUser(user: str, pin: int):
    user_data = DatabaseManager.collection.find_one({'name': user})

    if user == user_data["name"] and pin == user_data["pin"]:
        return 1
    else:
        return 0

def create_user(user: str, pin: int):
    user_data = {'name': user, 'pin': pin, 'money': 10000}
    DatabaseManager.collection.insert_one(user_data)

def get_user(user: str):
    return DatabaseManager.collection.find_one({'name': user})