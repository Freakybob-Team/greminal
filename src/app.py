import os
import cmds.usredit as usredit
print("Greminal - The Greg Terminal")
print("By Freakybob Team - run help for list of commands")
print("Run osl for licenses.")
print("Set username with usredit")
print("Commands are stored in the cmds folder. if not found, run fix.")
username = "admin"
if os.path.exists("user.txt"):
    with open("user.txt", "r") as file:
        username = file.read()
def cmdInput():
    global cmd
    cmd = input(f"{username}@greminal:$ ")
cmdInput()
if cmd == "usredit":
    usredit.cmd()
if cmd == "fix":
    print("Not implemented")