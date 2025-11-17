import tkinter as tk
window = tk.Tk()
window.title("Timeline Creator") # title at the top of the window
window.geometry("1200x750") # set the size (width x height)
window.resizable(False, False) # keep it from being resized
event = tk.Label(window, text = "Type an event, followed by a date.")
font = ("Arial", 14)
event.pack(pady = 10)
window.mainloop()
