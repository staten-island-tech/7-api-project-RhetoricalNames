import tkinter as tk
import requests

#cd app
#Scripts\Activate.ps1

window = tk.Tk()
window.title("API")
window.geometry("1200x750")
window.resizable(False, False)

instructions = tk.Label(window, text = "Type a number")
instructions.pack(pady = 10)

username = tk.IntVar()
searchbox = tk.Entry(window, font = ("Arial", 14), width = 30, textvariable=username)
searchbox.pack(pady = 5)

Toutput = tk.Label(window, text="", fg="black", font=("Times New Roman", 14), wraplength=500)
Toutput.pack(pady=20)

Ioutput = tk.PhotoImage()

def search():
    input = searchbox.get()
    user = requests.get(f"https://xkcd.com/{input}/info.0.json")
    stats = user.json()
    Toutput.config(text=stats, bg= "SteelBlue")
    Ioutput.config(file=requests.get(dict(stats)['img']))
    print(dict(stats)['img'])


search_button = tk.Button(window, text = "Search",
font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = search)
search_button.pack(pady = 10)
window.mainloop()