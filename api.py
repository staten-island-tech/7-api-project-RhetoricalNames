import tkinter as tk
import requests

#cd app
#Scripts\Activate.ps1
 
def search(input):
    comic = requests.get(f"https://xkcd.com/{input}/info.0.json")
    transcript = comic.json()
    print(dict(transcript))

window = tk.Tk()
window.title("API")
window.geometry("1200x750")
window.resizable(False, False)

instructions = tk.Label(window, text = "Type a comic number")
instructions.pack(pady = 10)

number = tk.IntVar()
searchbox = tk.Entry(window, font = ("Arial", 14), width = 30, textvariable=number)
searchbox.pack(pady = 5)

search_button = tk.Button(window, text = "Search",
font = ("Arial", 14), command = lambda: search(number.get()))
search_button.pack(pady = 10)
window.mainloop()
