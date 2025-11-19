import tkinter as tk
def forward():
    text = entry.get()
def backward():
    text = entry.get()
window = tk.Tk()
window.title("Cipher")
window.geometry("1200x750")
window.resizable(False, False)
prompt = tk.Label(window, text = "Type something to encode")
font = ("Arial", 14)
prompt.pack(pady = 10)
prompt.pack(pady = 10)
entry = tk.Entry(window, font = ("Arial", 14), width = 30)
entry.pack(pady=5)
move_forward = tk.Button(window, text = "Shift forward",
font = ("Arial", 14), command = forward)
move_forward.pack(pady = 10)
move_backward = tk.Button(window, text = "Shift backward",
font = ("Arial", 14), command = forward)
move_backward.pack(side = tk.LEFT, padx = 10)
window.mainloop()
