
#this program creates an absolute file path

import os

fName = 'Hello.txt'

fPath = 'C:\\Python_Projects\\'

abPath = os.path.join(fPath, fName)

print(abPath)
