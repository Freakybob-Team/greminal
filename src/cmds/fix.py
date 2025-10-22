import urllib.request
import json
import os
import subprocess
print("This file uses Internet, and downloads from github.com")
input("Run CTRL+C to exit or press enter to continue.")
with urllib.request.urlopen("https://freakybob-team.github.io/greminal/data/cmds.json") as url:
    data = json.loads(url.read().decode())
for item in data:
    if os.path.exists("cmds/"):
        print("cmds/ found; not creating")
    else:
        os.mkdir("cmds/")
    urllib.request.urlretrieve("https://freakybob-team.github.io/greminal/src/cmds/" + item["name"] + ".py", "cmds/" + item["name"]  + ".py")
print("Commands downloaded!")
subprocess.call(['python', 'app.py'])