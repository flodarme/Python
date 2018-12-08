#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.7.1
#
# Author:       Florence Darko-Mensah
#
# Purpose:      Check Files. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

import drill121_check_files_main
import drill121_check_files_func



def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
    """
    self.btn_browser1 = tk.Button(self.master,width=16,height=1,text='Browse...',font=("Helvetica", 14))
    self.btn_browser1.grid(row=3,column=0,padx=(27,10),pady=(50,0),sticky=N+W)
    self.btn_browser2 = tk.Button(self.master,width=16,height=1,text='Browse...',font=("Helvetica", 14))
    self.btn_browser2.grid(row=4,column=0,padx=(27,0),pady=(12,0),sticky=N+W)
    self.btn_fcheck = tk.Button(self.master,width=16,height=2,text='Check for files...',font=("Helvetica", 14))
    self.btn_fcheck.grid(row=5,column=0,padx=(27,0),pady=(12,0),sticky=N+W)
   

    self.txt_browser1 = tk.Entry(self.master,text='')
    self.txt_browser1.grid(row=3,column=1,rowspan=1,columnspan=2,padx=(27,0),pady=(50,0),sticky=N+E+W)
    self.txt_browser2 = tk.Entry(self.master,text='')
    self.txt_browser2.grid(row=4,rowspan=1,column=1,columnspan=2,padx=(27,0),pady=(12,0),sticky=N+E+W)
    
    

    
    self.btn_close = tk.Button(self.master,width=16,height=2,text='Close Program',font=("Helvetica", 14), command=lambda: drill121_check_files_func.close(self))
    self.btn_close.grid(row=5,column=9,columnspan=1,padx=(27,0),pady=(0,0),sticky=E)




if __name__ == "__main__":
    pass
