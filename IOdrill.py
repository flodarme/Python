"""
    For this drill, you will need to write a script that will check a specific
    folder on the hard drive, verify whether those files end with a “.txt” file
    extension and if they do, print those qualifying file names and their
    corresponding modified time-stamps to the console.

"""


import datetime
import os
import fnmatch

fName = '*.txt'
fPath = 'C:\\python drill\\'


def time_modified(fPath):
    t = os.path.getmtime(fPath)
    return datetime.datetime.fromtimestamp(t)


def start():
    for fName in os.listdir(fPath):
        if fnmatch.fnmatch(fName, '*.txt'):
            abPath = os.path.join(fPath, fName)
            time = time_modified(fPath)
            print("{}    {}    {}".format(fName, abPath, time ))
        

        


if __name__=="__main__":
    start()





