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

instructions = tk.Label(window, text = "Type the name of a game", font= ("Arial", 15))
instructions.pack(pady = 10)

userinput = tk.StringVar()
searchbox = tk.Entry(window, font = ("Arial", 14), width = 20, textvariable=userinput)
searchbox.pack(pady = 5)

output = tk.Label(window, text="", fg="black", font=("Times New Roman", 14), wraplength=500)
output.pack(pady=20)

def find_statistics():
    gametitle = userinput.get()
    info = requests.get("https://www.freetogame.com/api/games")
    games_stats = info.json()
    for game in games_stats:
        if game["title"].lower() == gametitle.lower():
            output.config(
                text=f"Title: {game['title']}")
            return
    output.config(text="Output not found. Please try again.")

def performance():
    gametitle = userinput.get()
    info = requests.get("https://www.freetogame.com/api/games")
    games_stats = info.json()
    for game in games_stats:
        if game["title"].lower() == gametitle.lower():
            game_info = requests.get(f"https://www.freetogame.com/api/game?id={game['id']}")
            converted_data = game_info.json()
            output.config(
                text=converted_data["minimum_system_requirements"]
            )
            return
    output.config(text="Output not found. Please try again.")

def images():
    user = requests.get(f"https://www.freetogame.com/api/games/{userinput}")
    image = user.json()
    response = requests.get(image["screenshots"][0])
    response.raise_for_status()
    pillow_image = Image.open(BytesIO(response.content))
    tk_image = ImageTk.PhotoImage(pillow_image)
    tk_image.thumbnail((300, 200), Image.LANCZOS)
    Ioutput = tk.Label(image = tk_image)
    Ioutput.image = tk_image
    Ioutput.pack()

def random_search():
    


search_button = tk.Button(window, text="Search via name", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = find_statistics)
search_button.pack(pady=10)
image_button = tk.Button(window, text="Screenshots", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = images)
image_button.pack(pady=10)
stats_button = tk.Button(window, text="Performance information", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = performance)
stats_button.pack(pady=10)
random_search_button = tk.Button(window, text="Random game", font = ("Arial", 14), bg= "SteelBlue", fg= "White", command = random_search)
stats_button.pack(pady=10)
window.mainloop() 
