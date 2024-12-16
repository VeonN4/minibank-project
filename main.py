from database import DatabaseManager
from database import userHandler
import dotenv

connection = dotenv.get_key(".env", "MONGODB_ADDRESS")
client = DatabaseManager.initialize(connection)

MENU_OPTIONS = {
    "menu": ["Login", "Register"],
    "dashboard": ["Transfer", "Deposit", "Withdraw", "Change PIN", "Exit"],
}


def menu():
    print("\nVeonise Minibank\n")
    for i, option in enumerate(MENU_OPTIONS["menu"], start=1):
        print(f"{i}. {option}")

    choice = int(input("Enter your choice (1/2): "))
    choiceHandler(choice, "menu")


def choiceHandler(choice: int, loc: str, user=None):
    match loc:
        case "dashboard":
            match choice:
                case 1:
                    userTransfer(user)
                case 2:
                    userDeposit(user)
                case 3:
                    userWithdraw(user)
                case 4:
                    userChangePIN(user)
                case 5:
                    print("Exiting dashboard...")
                    return
        case "menu":
            match choice:
                case 1:
                    user = loginPrompt()
                    if user:
                        userDashboard(user)
                case 2:
                    user = register_prompt()
                    if user:
                        userDashboard(user)


def loginPrompt():
    while True:
        print("Login\n")
        user = input("Enter your name: ")
        pin = int(input("Enter your pin: "))

        if userHandler.validateUser(user, pin) == 1:
            print(f"Welcome, {user}!")
            return user
        else:
            print("Wrong username or PIN!")


def register_prompt():
    while True:
        print("\nRegister")
        user = input("Enter your name: ")
        pin = int(input("Enter your pin: "))
        confirm_pin = int(input("Confirm your pin: "))

        if pin != confirm_pin:
            print("PINs do not match! Please try again.")
        elif pin < 1000 or pin > 9999:
            print("PINs should be 4 digits")
        else:
            userHandler.create_user(user, pin)
            print("Registration successful!")
            return user


def userDashboard(user):
    choice = 0

    while choice != 5:
        print("\nDashboard Menu")
        print("Current Balance:", userHandler.get_user(user)["money"])
        for i, option in enumerate(MENU_OPTIONS["dashboard"], start=1):
            print(f"{i}. {option}")

        choice = int(input("Menu (1/2/3/4/5): "))
        choiceHandler(choice, "dashboard", user)


def userDeposit(user):
    print("\nDeposit\n")
    amount = int(input("Amount to deposit: Rp. "))
    if DatabaseManager.deposit(user, amount):
        print(f"Successfully deposited Rp. {amount}.")
    else:
        print("Deposit failed.")


def userWithdraw(user):
    print("\nWithdraw\n")
    amount = int(input("Amount to withdraw: Rp. "))
    if DatabaseManager.withdraw(user, amount):
        print(f"Successfully withdrew Rp. {amount}.")
    else:
        print("Withdrawal failed.")


def userChangePIN(user):
    print("\nChange PIN\n")
    current_pin = userHandler.get_user(user)["pin"]
    print(
        "Current PIN:", current_pin
    )  # Do not display the current PIN for security reasons

    while True:
        newPIN = int(input("New PIN: "))
        confirmation = int(input("Confirm New PIN: "))

        if newPIN != confirmation:
            print("PINs do not match! Please try again.")
        else:
            DatabaseManager.changePIN(user, newPIN)
            print("PIN changed successfully!")
            break


def userTransfer(user):
    print("\nTransfer")
    transferTo = input("Enter recipient's name (must match exactly): ")
    amount = int(input("Amount to transfer: Rp. "))

    DatabaseManager.transfer(user, transferTo, amount)


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nUh oh! You seem intended to stop the program. Goodbye!")
