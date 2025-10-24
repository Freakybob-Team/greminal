import os
def cmd():
    mypath = os.getcwd()
    filenames =  os.listdir(mypath)
    for item in filenames:
        print(item)