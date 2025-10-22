"""
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>."
"""
try:    
    import os
    import urllib.request
    import subprocess
    try:
        import cmds.usredit as usredit
        import cmds.osl as osl
        import cmds.help as help
    except:
        print("A command couldn't be imported. Commands will not work other than update.")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Greminal - The Greg Terminal")
    print("By Freakybob Team - run help for list of commands")
    print("Run osl for licenses.")
    print("Set username with usredit")
    print("Commands are stored in the cmds folder. if not found, run update.")
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
    if cmd == "osl":
        osl.cmd()
        cmdInput()
    if cmd == "update":
        print("This command requires internet, and downloads from github.com.")
        input("Run CTRL+C to exit or press enter to continue.")
        urllib.request.urlretrieve("https://freakybob-team.github.io/greminal/src/cmds/update.py", "update.py")
        print("fix.py downloaded, now running")
        subprocess.call(['python', 'update.py'])
    if cmd == "help":
        help.cmd()
        cmdInput()
except:
    print(f"\nThere was either an error or you exited Greminal yourself. Hope to see you back soon, {username}! :)")