import tkinter as tk
def dates():
window = tk.Tk()
window.title("Timeline Creator")
window.geometry("1200x750")
window.resizable(False, False)
event = tk.Label(window, text = "Type an event")
font = ("Arial", 14)
event.pack(pady = 10)
event.pack(pady = 10)
entry = tk.Entry(window, font = ("Arial", 14), width = 30)
entry.pack(pady=5)
sort_button = tk.Button(window, text = "Sort Events!",
font = ("Arial", 14), command = dates)
sort_button.pack(pady=10)
window.mainloop()
