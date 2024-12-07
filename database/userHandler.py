from database import DatabaseManager

def validateUser(user: str, pin: str):
    if user == DatabaseManager().collection.find_one({'name': user}) and pin == DatabaseManager().collection.find_one({'pin': pin}):
        return 1
    else:
        return 0