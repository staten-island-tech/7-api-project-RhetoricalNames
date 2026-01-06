import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
import random

#cd app
#Scripts\Activate.ps1

window = tk.Tk()
window.title("F2P game discovery")
window.geometry("1200x750")
window.resizable(False, False)
window.config(bg="light gray")

instructions = tk.Label(window, text = "Select a random game, than find more about it!", font= ("Arial", 15), bg="light gray")
instructions.pack(pady=10)
title_output = tk.Label(window, text="", font= ("Times New Roman", 12), bg="light gray")
title_output.pack(pady=5)
output = tk.Label(window, text="", bg="light gray", font=("Times New Roman", 14), wraplength=500)
output.pack(pady=20)
Ioutput = tk.Label(image="", bg="light gray")
Ioutput.pack(pady=10)
game_data = ""

def random_search():
    Ioutput.config(image="")
    data = requests.get("https://www.freetogame.com/api/games")
    random_number = random.randint(1, len(data.json()))
    data = data.json()
    global game_data
    game_data = requests.get(f"https://www.freetogame.com/api/game?id={data[random_number]["id"]}")
    game_data = game_data.json()
    title_output.config(text=f"Selected game: {game_data["title"]}")



def performance():
    if game_data == "":
        output.config(text="Game not selected!")
        return
    output.config(text=f"System requirements:{game_data["minimum_system_requirements"]}")

def thumbnail():
    if game_data == "":
        output.config(text="Game not selected!")
        return
    thumbnail_link = game_data["thumbnail"]
    response = requests.get(thumbnail_link)
    pillow_image = Image.open(BytesIO(response.content))
    pillow_image.thumbnail((300, 200), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(pillow_image)
    Ioutput.config(image=tk_image)
    Ioutput.image = tk_image

def info(): 
    if game_data == "":
        output.config(text="Game not selected!")
        return
    output.config(text=f"Developer: {game_data["developer"]}\nPublisher: {game_data["publisher"]}\nShort description: '{game_data["short_description"]}'\ngenre: '{game_data["genre"]}'\ndeveloper: '{game_data["developer"]}'\nGame link: {game_data["game_url"]}")

random_search_button = tk.Button(window, text="Random game", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = random_search)
random_search_button.pack(pady=10)
image_button = tk.Button(window, text="Search for thumbnail", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = thumbnail)
image_button.pack(pady=10)
stats_button = tk.Button(window, text="Performance information", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = performance)
stats_button.pack(pady=10)
info_button = tk.Button(window, text="Game information", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = info)
info_button.pack(pady=10)
window.mainloop() 
