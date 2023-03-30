# EXAMEN DE POO UNIDAD 2, CREANDO UN PROGRAMA PARA UNA TAQUERIA (NOMBRE FICTICIO: TACONEANDO)
# AUTORES: RAUL DANILO DURAN DZUL Y JUAN CARLOS ORTIZ SALAS
# FECHA: 31/03/23

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql


def eleccion():
    global cl
    cl = tk.Tk()
    cl.title("Pedido")
    cl.geometry("700x700")


eleccion()
