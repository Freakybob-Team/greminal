"""
This file is part of Greminal, by Freakybob Team.

Greminal is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Greminal is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Greminal. If not, see <https://www.gnu.org/licenses/>.
"""
def cmd():
    print("User Edit")
    print("What would you like to change your Greminal username to?")
    user = input("> ")
    with open("user.txt", "w") as file:
        file.write(user)
    print("Your username has been changed to " + user + "! Restart to see the changes.")