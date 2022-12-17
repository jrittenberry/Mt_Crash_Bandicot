def show_balance(balance):
    print(float(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return float(amount) + float(balance)


def withdraw(balance):
    amount = input("Enter amount to withdraw ")
    return float(balance) - float(amount)


def logout(name):
    print("Goodbye", name, "! ")
