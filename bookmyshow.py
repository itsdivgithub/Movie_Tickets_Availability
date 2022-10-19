import sys
import os 
import time
import re
import urllib.request as urllib2
import tkinter
import webbrowser
import datetime
from IPython import display
from bs4 import BeautifulSoup

url='https://in.bookmyshow.com/buytickets/act-1978-bengaluru/movie-bang-ET00300389-MT/20201128'
cinema='PVR: South X Mall, Kanpur'

def open_url():
    chrome_path ='open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    return


def create_popup():
    root= tkinter.Tk()
    text= 'Theater is now Open!'
    label= tkinter.Label(root, text=text)
    label.pack()
    test= tkinter.Button(root, text="Click Me!", command=open_url)
    test.pack()
    root.test =test
    quit= tkinter.Button(root, text="Quit", command= root.destroy)
    quit.pack()

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

    return

    
