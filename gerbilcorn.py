# Pandas for converting resultset to csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import scipy as sy
#import pytesseract as pt
#import request as r
#import scrapy.crawler
#import scrapy
#from datetime import date

# ImportLibrarHere
from tkinter import *
from tkinter import ttk
import time
from PIL import ImageTk, Image
import os
import sqlite3
from tkinter import messagebox

# SplashScreen
sroot = Tk()
sroot.minsize(height=400, width=300)
sroot.title("Splash window")
sroot.configure()
spath = "Images/Autism_logo.jpg"
simg = ImageTk.PhotoImage(Image.open(spath))
my = Label(sroot, image=simg)
my.image = simg
my.place(x=0, y=0)

Frame(sroot, height=720, width=8, bg='black').place(x=520, y=0)

lbl1 = Label(sroot, text="Welcome to Gerbilcorn !",
             font='Ariel 24 ', fg='blue',)

lbl1.pack(side="bottom")

lbl1.pack(padx=100, pady=100)


# MainScreen

def mainroot():

    root = Tk()
    root.geometry('1080x500')
    root.minsize(width=1080, height=550)
    root.maxsize(width=1080, height=550)
    root.configure(bg='blue')
    root.title("Gerbilcorn:   Main Window")

# Add Window Functionality Here(like widgets, etc)
#
# End Of Main Window
#
# After this call the main window here

def call_mainroot():
    sroot.destroy()
    mainroot()


sroot.after(4000, call_mainroot)  # TimeOfSplashScreen
mainloop()


# Help option for the user
def show_help():
    print("Enter 'Help' for this helper.")
    print("Enter 'Done' to stop searching.")


show_help()

# BeautifulSoup for scraping html in sites

# 1st reference site = featoflouisville
url = "https://featoflouisville.org/calendar/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup.find('span').get_text("sensory friendly")
# urllib.request.urlopen()
