def login(database, username, password):
    if username in database and password == database[username]:
        print("Welcome to your account ", username, "! ")
        return username
    elif username in database and password != database[username]:
        print("Incorrect password")
        return ""
    else:
        print("Username not found")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered ")
        return ""
    else:
        print("Username has been registered ")
