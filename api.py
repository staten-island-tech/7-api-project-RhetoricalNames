import tkinter as tk

 
def search():
    number = input.cget(f"https://xkcd.com/{input}/info.0.json")
    print(number)

""" window = tk.Tk()
window.title("API")
window.geometry("1200x750")
window.resizable(False, False)
input = tk.Label(window, text = "Type a comic number")
font = ("Arial", 14)
input.pack(pady = 10)
searchbox = tk.Entry(window, font = ("Arial", 14), width = 30)
searchbox.pack(pady=5)
search = tk.Button(window, text = "Search",
font = ("Arial", 14), command = search)
search.pack(pady = 10)
window.mainloop() """
