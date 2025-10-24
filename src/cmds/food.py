import cmds.foodtools.eat as eat
import cmds.foodtools.cook as cook
def cmd(cmd):
    print("Welcome to Food!")
    request = cmd[5:]
    print(request)
    if request.startswith("install"):
        print("using python downloads")
        app = request[8:]
        eat.python(app)
    if request.startswith("temp"):
        print("using temp downloads; python")
        app = request[5:]
        cook.python(app)