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

instructions = tk.Label(window, text = "Type a number", font= ("Arial", 16))
instructions.pack(pady = 10)

username = tk.IntVar()
searchbox = tk.Entry(window, font = ("Arial", 14), width = 30, textvariable=username)
searchbox.pack(pady = 5)

Toutput = tk.Label(window, text="", fg="black", font=("Times New Roman", 14), wraplength=500)
Toutput.pack(pady=20)

def search_transcript():
    input = searchbox.get()
    user = requests.get(f"https://xkcd.com/{input}/info.0.json")
    stats = user.json()
    Toutput.config(text=stats['transcript'])

def other_stats():
    input = searchbox.get()
    user = requests.get(f"https://xkcd.com/{input}/info.0.json")
    stats = user.json()
    Toutput.config(text=f"Year: {stats['year']}, Month: {stats['month']}")

def search_image():
    input = searchbox.get()
    user = requests.get(f"https://xkcd.com/{input}/info.0.json")
    stats = user.json()
    response = requests.get(stats['img'])
    response.raise_for_status()
    pillow_image = Image.open(BytesIO(response.content))
    tk_image = ImageTk.PhotoImage(pillow_image)
    tk_image.thumbnail((300, 200), Image.LANCZOS)
    Ioutput = tk.Label(image = tk_image)
    Ioutput.image = tk_image
    Ioutput.pack()


search_button = tk.Button(window, text="Search for transcript", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = search_transcript)
search_button.pack(pady=10)
image_button = tk.Button(window, text="Search for image", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = search_image)
image_button.pack(pady=20)
stats_button = tk.Button(window, text="Other information", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = other_stats)
stats_button.pack(pady=20)
window.mainloop() 
