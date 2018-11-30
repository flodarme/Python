
"""
    For this drill, you will need to write a script that will check a specific
    folder on the hard drive, verify whether those files end with a “.txt” file
    extension and if they do, print those qualifying file names and their
    corresponding modified time-stamps to the console.

"""


import fnmatch
import os
import datetime

fName = ''
fPath = 'C:\\python drill\\'


for fName in os.listdir(fPath):
    if fnmatch.fnmatch(fName, '*.txt'):
        abPath = os.path.join(fPath, fName)
        time =  os.path.getmtime(abPath)
        modTime = datetime.datetime.fromtimestamp(time)
        print("{} {} {}".format(fName, abPath, modTime))
