def cmd():
    print("User Edit")
    print("What would you like to change your Greminal username to?")
    user = input("> ")
    with open("user.txt", "w") as file:
        file.write(user)
    print("Your username has been changed to " + user + "! Greminal will now close; restart to see the changes.")