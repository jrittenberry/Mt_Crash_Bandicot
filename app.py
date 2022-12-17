from banking_pkg.account import show_balance, withdraw, logout, deposit


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")

name = input("Enter name to register: ")

pin = input("Enter PIN: ")

balance = 0

print(name, "has a been registered with a starting balance of $", str(balance))

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name == name_to_validate and pin == pin_to_validate:
        print("Login Succesful!")
        break
    else:
        print("Invalid Credentials!")
        continue

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        print("Current Balance: $", balance)
    elif option == "2":
        balance = deposit(balance)
        print("Current Balance: $", balance)
    elif option == "3":
        balance = withdraw(balance)
        print("Current Balance: $", balance)
    elif option == "4":
        logout(name)
        break
    else:
        print("Error. Try inputing a valid response.")
        continue
