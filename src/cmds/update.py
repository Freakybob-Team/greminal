"""
This file is part of Greminal, by Freakybob Team.

Greminal is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Greminal is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Greminal. If not, see <https://www.gnu.org/licenses/>.
"""
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
urllib.request.urlretrieve("https://freakybob-team.github.io/greminal/src/app.py", "app.py")
print("Commands downloaded!")
subprocess.call(['python', 'app.py'])