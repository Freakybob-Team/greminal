import os
import urllib.request
import subprocess
try:
    import cmds.usredit as usredit
except:
    print("A command couldn't be imported. Commands will not work other than fix.")
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
    print("This command requires internet, and downloads from github.com.")
    input("Run CTRL+C to exit or press enter to continue.")
    urllib.request.urlretrieve("https://freakybob-team.github.io/greminal/src/cmds/fix.py", "fix.py")
    print("fix.py downloaded, now running")
    subprocess.call(['python', 'fix.py'])