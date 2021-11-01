import tkinter as tk
from tkinter import font
import requests
from tkinter import *
from tkinter import messagebox


def fetchNews():
    country = country_text.get().lower()
    country_api = "https://api.printful.com/countries"
    country_code = requests.get(country_api)
    country_code_data = country_code.json()
    cc = 'none'
    results = country_code_data['result']
    for result in results:
        if country == result['name'].lower():
            cc = result['code']
    if cc == "none":
        messagebox.showerror('ERROR', "Country Not Found {}".format(country))

    custom_link = "https://newsapi.org/v2/top-headlines?country=" + \
        cc.lower()+"&apiKey=bdc912d442614e15846f1804f1b751d8"
    responce = requests.get(custom_link)
    api_data = responce.json()
    myArticals = api_data["articles"]
    print(myArticals)
    if(len(myArticals) == 0):
        messagebox.showinfo("NO NEWS", "{} Has No News".format(country))
    else:
        myTitles = ''
        c = 1
        for article in myArticals:
            myTitles = myTitles+str(c)+' . '+article['title']+'\n'
            v = int(c)+1
            c = v
        News_lbl['text'] = myTitles


root = tk.Tk()
root.geometry("1200x1200")
root.title("News App")

country_text = StringVar()
country_entry = Entry(root, textvariable=country_text)
country_entry.pack()

search_button = Button(root, text="Search", width=12, command=fetchNews)
search_button.pack()

News_lbl = Label(root, text='', font=("bold", 12))
News_lbl.pack()
root.mainloop()
