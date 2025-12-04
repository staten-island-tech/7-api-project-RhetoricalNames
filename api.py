import tkinter as tk
import requests

#cd app
#Scripts\Activate.ps1

window = tk.Tk()
window.title("API")
window.geometry("1200x750")
window.resizable(False, False)

instructions = tk.Label(window, text = "Type a comic number")
instructions.pack(pady = 10)

number = tk.IntVar()
searchbox = tk.Entry(window, font = ("Arial", 14), width = 30, textvariable=number)
searchbox.pack(pady = 5)

Toutput = tk.Label(window, text="", pady= 10, fg="black", font="Arial, 11", wraplength=500)

def search():
    search = searchbox.get()
    comic = requests.get(f"https://xkcd.com/{search}/info.0.json")
    transcript = comic.json()
    print(transcript)
    Toutput.config(text=transcript)

search_button = tk.Button(window, text = "Search",
font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = search)
search_button.pack(pady = 10)
window.mainloop()
