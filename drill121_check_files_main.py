#
# Python Ver:   3.7.1
#
# Author:       Florence Darko-Mensah
#
# Purpose:      Check File GUI. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

import drill121_check_files_func
import drill121_check_files_gui


# Frame is the Tkinter frame class that my class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(750,250) #(Height, Width)
        self.master.maxsize(750,250)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill121_check_files_func.ask_quit(self))
        arg = self.master
    

        # load  the GUI widgets from a separate module, 
         
        drill121_check_files_gui.load_gui(self)
       
        
        

        
"""
  
    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
