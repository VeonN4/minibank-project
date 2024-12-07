class negativeMoney(Exception):
    def __init__(self, value):
        message = f"You can't deposit negative money {value}"            
        self.errors = value

        super().__init__(message)

class userNotFound(Exception):
    def __init__(self, value):
        message = f"{value} is not found."            
        self.errors = value

        super().__init__(message)

class brokeAlert(Exception):
    def __init__(self, value):
        message = f"You don't have enough money, your current money is {value}"            
        self.errors = value

        super().__init__(message)