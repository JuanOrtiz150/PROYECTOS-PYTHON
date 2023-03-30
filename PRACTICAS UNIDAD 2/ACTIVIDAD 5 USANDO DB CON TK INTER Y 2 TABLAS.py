# ACTIVIDAD 5 USANDO BASE DE DATOS EN TABLA CON TK INTER
# FECHA:23/03/23
# AUTOR: JUAN CARLOS ORTIZ SALAS

import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3


def conectar_db():
    conexion = sqlite3.connect("streaming.db")
    conexion.execute("""
                create table if not exists login(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    anio int,
                    autor varchar,
                    album varchar,
                    duracion varchar,
                    director varchar,
                    duracion2 varchar, 
                    anio2 int,
                    titulo varchar,
                    id2 interger primary key AUTOINCREMENT,
                    clificacion int
                    )
    """)
    conexion.close()


def ventanauno():
    global ventana1
    ventana1 = Tk()
    ventana1.title("Streaming xuan")
    ventana1.geometry("500x500")
    Label(ventana1, text="", bg="navy", fg="white",
          width="300", height="3", font=("Calibri", 15)).pack()
    Label(ventana1, text="").pack()
