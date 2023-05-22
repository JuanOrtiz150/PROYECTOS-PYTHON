import tkinter as tk

raiz = tk.Tk()
raiz.overrideredirect(True)  # Quitar barra de título
raiz.etiqueta = tk.Label(
    raiz, text="Hola Tkinter!\nProgramando en Python\nparzibyte.me")
raiz.etiqueta.pack(side="top")

raiz.mainloop()
