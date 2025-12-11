import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

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

def search():
    input = searchbox.get()
    user = requests.get(f"https://xkcd.com/{input}/info.0.json")
    stats = user.json()
    Toutput.config(text=stats, bg= "SteelBlue")

    response = requests.get(dict(stats)['img'])
    img_data = response.content
    print(img_data)
    pillow_image = Image.open(BytesIO(img_data))
    print(pillow_image)
    tk_image = ImageTk.PhotoImage(pillow_image)
    print(tk_image)
    Ioutput = tk.Label(image = tk_image)
    Ioutput.pack()



search_button = tk.Button(window, text = "Search",
font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = search)
search_button.pack(pady = 10)
window.mainloop()