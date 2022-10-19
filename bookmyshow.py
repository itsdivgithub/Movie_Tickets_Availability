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

def parse_and_check_tickets(url_openned):

    url_soup= BeautifulSoup(url_openned , features="html5lib")
    a_class = url_soup.find_all("a", {"class": "_venue-name"})
    a_class_str = str(a_class)
    a_class_soup= Beautiful_soup(a_class_str, features="html5lib")
    strong= a_class_soup.find_all("strong")
    strong_str= str(strong)

    for element in strong:
        result= re.search(rf'{cinema}', str(element))
        if result is None:
            continue
        else:
            create_popup()
            exit()
    display.display("Tickets were not available at :" + str(datetime.datetime.now()))
    return

def fetch_html():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
        
    url_request = urllib2.Request(url=url, headers=headers)
    try:
        url_openned= urllib2.urlopen(url=url_request)
    except urllib2.HTTPError as e:
        display.display(e.code)
        display.display(e.read())
    
    parse_and_check_tickets(url_openned)
    return

def main():

    while True:
        fetch_html()
        time.sleep(300)

if __name__ == "__main__":
    main()

