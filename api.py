import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

#cd app
#Scripts\Activate.ps1

window = tk.Tk()
window.title("F2P game discovery")
window.geometry("1200x750")
window.resizable(False, False)

instructions = tk.Label(window, text = "Type the name of a free game", font= ("Arial", 15))
instructions.pack(pady = 10)

username = tk.StringVar()
searchbox = tk.Entry(window, font = ("Arial", 14), width = 30, textvariable=username)
searchbox.pack(pady = 5)

output = tk.Label(window, text="", fg="black", font=("Times New Roman", 14), wraplength=500)
output.pack(pady=20)

def stats():
    if input not in requests.get("https://www.freetogame.com/api/games"["title"]):
        output.config(text="Game not in database")
    else:
        input = searchbox.get()
        info = requests.get(f"https://www.freetogame.com/api/games{input}")
        stats = info.json()
        output.config(text=f"Title: {stats["title"]}, status: {stats["status"]}")

def performance():
    input = searchbox.get()
    user = requests.get(f"https://www.freetogame.com/api/games/{input}")
    stats = user.json()
    output.config(text=f"Year: {stats['year']}, Month: {stats['month']}")

def images():
    input = searchbox.get()
    user = requests.get(f"https://www.freetogame.com/api/games/{input}")
    image = user.json()
    response = requests.get(image["screenshots"][0])
    response.raise_for_status()
    pillow_image = Image.open(BytesIO(response.content))
    tk_image = ImageTk.PhotoImage(pillow_image)
    tk_image.thumbnail((300, 200), Image.LANCZOS)
    Ioutput = tk.Label(image = tk_image)
    Ioutput.image = tk_image
    Ioutput.pack()


search_button = tk.Button(window, text="Search for name", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = stats)
search_button.pack(pady=10)
image_button = tk.Button(window, text="Screenshots", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = images)
image_button.pack(pady=20)
stats_button = tk.Button(window, text="Performance information", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = performance)
stats_button.pack(pady=20)
window.mainloop() 
