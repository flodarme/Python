Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fName = "Florence"
>>> lName = "Quaye-Sowah"
>>> prinf(fName + lName)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    prinf(fName + lName)
NameError: name 'prinf' is not defined
>>> print(fName + lName)
FlorenceQuaye-Sowah
>>> print(fName + " " + lName)
Florence Quaye-Sowah
>>> print("Hello {} {}, welcome to Python!.".format(fName,lName))
Hello Florence Quaye-Sowah, welcome to Python!.
>>> fname = input("What is your first name?\n>>> ")
What is your first name?
>>> fname = input("What is your \"first name?\"\n>>> ")
>>> fname = input("What is your \"first name?\"\n>>> ")
What is your "first name?"
>>> fname = input("What is your 'first name'?\n>>> ")
>>> fname = input("What is your 'first name'?\n>>> ")
What is your 'first name'?
>>> Florence
>>> fName
'Florence'
>>> 
