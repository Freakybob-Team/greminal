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
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        WHITE = '\033[97m'
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Greminal - The Greg Terminal")
    print("By Freakybob Team - run help for list of commands")
    print("Run osl for licenses.")
    print("Set username with usredit")
    username = "admin"
    if os.path.exists("user.txt"):
        with open("user.txt", "r") as file:
            username = bcolors.OKGREEN + file.read()
    def cmdInput():
        global cmd
        cmd = input(f"{username}{bcolors.HEADER}@greminal:${bcolors.WHITE} ")
    cmdInput()
    if cmd:
        if cmd == "usredit":
            usredit.cmd()
        else:
            print("Command not found!")
            cmdInput()
        if cmd == "osl":
            osl.cmd()
            cmdInput()
        else:
            print("Command not found!")
            cmdInput()
        if cmd == "update":
            print(bcolors.OKBLUE + "This command requires internet, and downloads from github.com.")            
            input("Run CTRL+C to exit or press enter to continue.")
            urllib.request.urlretrieve("https://freakybob-team.github.io/greminal/src/cmds/update.py", "update.py")
            print("update.py downloaded, now running")
            subprocess.call(['python', 'update.py'])
        else:
            print("Command not found!")
            cmdInput()
        if cmd == "help":
            help.cmd()
            cmdInput()
        else:
            print("Command not found!")
            cmdInput()
except:
    print(f"{bcolors.WARNING}\nThere was either an error or you exited Greminal yourself. Hope to see you back soon, {username}{bcolors.WHITE}! :)")