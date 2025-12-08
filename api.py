import tkinter as tk
import requests

#cd app
#Scripts\Activate.ps1
""" 
window = tk.Tk()
window.title("Chess API")
window.geometry("1200x750")
window.resizable(False, False)

instructions = tk.Label(window, text = "Type a username")
instructions.pack(pady = 10)

username = tk.StringVar()
searchbox = tk.Entry(window, font = ("Arial", 14), width = 30, textvariable=username)
searchbox.pack(pady = 5)

Uoutput = tk.Label(window, text="", fg="black", font=("Times New Roman", 14), wraplength=500)
Uoutput.pack(pady=20)

def search():
    Uinput = searchbox.get()
    user = requests.get(f"https://api.chess.com/pub/player/{Uinput}")
    print(user)
    stats = user.json()
    print(stats)
    Uoutput.config(text=stats, bg= "SteelBlue")

search_button = tk.Button(window, text = "Search",
font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = search)
search_button.pack(pady = 10)
window.mainloop() """
def search(a):
    Uinput = a
    user = requests.get(f"https://api.chess.com/pub/player/{Uinput}")
    print(user) #response 403
"""     stats = user.json()
    print(stats) """
search("erik")
def b(a):
    titleabbrev = a
    user = requests.get(f"https://api.chess.com/pub/titled/{titleabbrev}")
    print(user) #response 403
"""     stats = user.json()
    print(stats) """
b("erik")