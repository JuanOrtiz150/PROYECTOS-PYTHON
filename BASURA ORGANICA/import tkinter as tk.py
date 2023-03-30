
import tkinter as tk
from tkinter import *
from tkinter import messagebox
ventana = tk.Tk()
ventana.geometry("500x400")
Label(text="INGRESE SU USUARIO Y CONTRASEÑA", bg="navy", fg="white",
      width="300", height="3", font=("Calibri", 15)).pack()
Label(text="").pack()

ventana.title("Ventana principal")

boton_in = tk.Button(
    ventana,
    text="Iniciar sesion",
    height="4",
    width="30"
)
boton_in.place(x=140, y=150)

boton_reg = tk.Button(
    ventana,
    text="Iniciar sesion",
    height="4",
    width="30"
)
boton_reg.place(x=140, y=250)

ventana.mainloop()
