Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 1
>>> num2 = 2
>>> 
>>> 
>>> print(num1 + num2)
3
>>> num1 = 102
>>> num2 = 2.1
>>> num1 = 1.2
>>> print(num1+num2)
3.3
>>> print(num1*num2)
2.52
>>> num1 = "1"
>>> print(num1+num2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(num1+num2)
TypeError: can only concatenate str (not "float") to str
>>> print(int(num1)+num2)
3.1
>>> 
