# Pandas for converting resultset to csv
import requests
from bs4 import BeautifulSoup as bs
import csv
import html5lib
import pandas as pd
import scipy as sy
import re
#import pytesseract as pt
#import scrapy.crawler
#import scrapy
#from datetime import date

# Import Library Here
from tkinter import *
from tkinter import ttk
import time
from PIL import ImageTk, Image
import os
import sqlite3
from tkinter import messagebox

# -----------------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------------
# Connect to an external/3rd party API and read data into your app
# Visualize data in a graph, chart, or other visual representation of data
# Create a class, then create at least one object of that class and populate it with data
# Implement a regular expression (regex) to ensure a field either a phone number or an email address is always stored and displayed in the same format
# Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
# -----------------------------------------------------------------------------------


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


def call_mainroot():
    sroot.destroy()
    mainroot()


# Functionality, buttons etc
root = Tk()
l = Label(root, text="Upcoming Sensory Friendly Showings")
l.pack()
b = Button(root, text="Check Times")
b.pack(side=LEFT)

# Help option for the user


def show_help():
    print("Enter 'Help' for this helper.")
    print("Enter 'Done' to stop searching.")


show_help()

l = Label(root, text="Help")
l.pack()
b2 = Button(root, text="Click Here", command=show_help)
b2.pack(side=LEFT)

# Time Of Splash Screen
sroot.after(4000, call_mainroot)
mainloop()

# End Of Main Window

# REQUIREMENT: Create a class, then create at least one object of that class and populate it with data

# 1st reference site = featoflouisville
URL = "https://featoflouisville.org/calendar/"
r = requests.get(URL)
print(r.content.prettify())

soup = bs(r.content, 'html5lib')
print(soup.prettify())

shows = []  # a list to store quotes
table = soup.find('div')

for row in table.findALL('div', class_='simcal-event-title'):
    show = {}
    show['url'] = row.a['href']
    show['img'] = row.img['src']
    shows.append(show)

filename = 'Autism_Friendly_Showings.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img'])
    w.writeheader()
    for show in shows:
        w.writerow(show.prettify())

# Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
