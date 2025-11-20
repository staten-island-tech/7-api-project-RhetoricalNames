import tkinter as tk

response = Unirest.get("https://wordsapiv1.p.mashape.com/words/soliloquy",
  headers={
    "X-Mashape-Key": "<required>",
    "Accept": "application/json"
  }
)
def definition():
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
definition = tk.Button(window, text = "Definition",
font = ("Arial", 14), command = definition)
definition.pack(pady = 10)
window.mainloop()
