# ACTIVIDAD 5 USANDO BASE DE DATOS EN TABLA CON TK INTER (SE USAN DOS TABLAS DE 5 CAMPOS CADA UNA, UTILIZANDO SQLITE Y TREE)
# FECHA:23/03/23
# AUTOR: JUAN CARLOS ORTIZ SALAS

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

# *******************************EN ESTA PARTE DE CONECTA LA BASE DE DATOS, UTILIZANDO FUNCIONES CON LAS CUALES SE PUEDEN REALIZAR CONSULTAR E INGRESAR DATOS******


def conectar_db():
    conexion = sqlite3.connect("school1.db")
    conexion.execute("""
                create table if not exists list(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    edad varchar,
                    matricula varchar,
                    carrera varchar,
                    semestre varchar
                    )
    """)
    conexion.close()


def conectar_db2():
    conexion = sqlite3.connect("school2.db")
    conexion.execute("""
                create table if not exists list(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    edad varchar,
                    clave varchar,
                    carrera varchar,
                    asig varchar
                    )
    """)
    conexion.close()


def guardar_alum():
    conexion = sqlite3.connect("school1.db")
    if nombre_alu.get() == "" or edad_alu.get() == "" or matricula_alu.get() == "" or carrera_alu.get() == "" or semestre_alu.get() == "":
        messagebox.showerror("Error en los datos",
                             "Debe completar los datos del alumno")
        return
    conexion.execute(
        "insert into list(nombre, edad, matricula, carrera, semestre) values (?,?,?,?,?)", (nombre_alu.get(), edad_alu.get(), matricula_alu.get(), carrera_alu.get(), semestre_alu.get()))
    conexion.commit()
    messagebox.showinfo(
        message="Datos del alumno registrados", title="REGISTRO EXITOSO")
    conexion.close()


def consult_alum():
    conexion = sqlite3.connect("school1.db")
    consulta = "SELECT * FROM list ORDER BY id desc"
    fcursor = conexion.cursor()
    fcursor.execute(consulta)
    datos = fcursor.fetchall()
    for i in datos:
        lista_alum1.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5]))


def consult_mae():
    conexion = sqlite3.connect("school2.db")
    consulta = "SELECT * FROM list ORDER BY id desc"
    fcursor = conexion.cursor()
    fcursor.execute(consulta)
    datos = fcursor.fetchall()
    for i in datos:
        lista_mae1.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5]))


def guardar_mae():
    conexion = sqlite3.connect("school2.db")
    if nombre_maer.get() == "" or edad_maer.get() == "" or clave_maer.get() == "" or carrera_maer.get() == "" or asignacion_maer.get() == "":
        messagebox.showerror("Error en los datos",
                             "Debe completar los datos del alumno")
        return
    conexion.execute(
        "insert into list(nombre, edad, clave, carrera, asig) values (?,?,?,?,?)", (nombre_maer.get(), edad_maer.get(), clave_maer.get(), carrera_maer.get(), asignacion_maer.get()))
    conexion.commit()
    messagebox.showinfo(
        message="Datos del maestro registrados", title="REGISTRO EXITOSO")
    conexion.close()


conectar_db()
conectar_db2()

# ****************AQUI INICIA EL PROGRAMA CON UNA VENTANA DE SELECCION SOBRE ALUMNOS Y MAESTROS


def Principal():
    global ventana1
    ventana1 = tk.Tk()
    ventana1.title("Registro de maestros y alumnos")
    ventana1.geometry("500x400")
    Label(ventana1, text="Hola usuario, elija la opcion que desee", fg="midnight blue",
          width="300", height="3", font=("corbel light", 19)).pack()
    Label(ventana1, text="").pack()

    boton_in = Button(
        ventana1,
        text="Registrar alumno",
        height="4",
        width="30",
        command=ventanados
    )
    boton_in.place(x=140, y=150)

    boton_reg = Button(
        ventana1,
        text="Registrar maestro",
        height="4",
        width="30",
        command=ventanatres
    )
    boton_reg.place(x=140, y=250)

    ventana1.mainloop()

# *****AQUI SE CREA UNA VENTANA DE ALUMNO DONDE SE RELLENAN LOS CAMPOS PARA PODER REGISTRARSE, LO MISMO EN EL CASO DE LA VENTANA DEL MAESTRO


def ventanados():
    global ventana2
    ventana2 = Tk()
    ventana2.title("Registrar alumno")
    ventana2.geometry("500x400")
    Label(ventana2, text="Hola alumno, porfavor registrate", fg="midnight blue",
          width="300", height="3", font=("corbel light", 18)).pack()
    Label(ventana2, text="").pack()

    global nombre_alu
    global edad_alu
    global matricula_alu
    global carrera_alu
    global semestre_alu

    nombre_alu = StringVar
    edad_alu = StringVar
    matricula_alu = StringVar
    carrera_alu = StringVar
    semestre_alu = StringVar

    nombre_alu = tk.Entry(ventana2, font=("calibri", 12))
    nombre_alu.place(width=225, height=20, x=195, y=100)

    edad_alu = tk.Entry(ventana2, font=("calibri", 12))
    edad_alu.place(width=225, height=20, x=195, y=125)

    matricula_alu = tk.Entry(ventana2, font=("calibri", 12))
    matricula_alu.place(width=225, height=20, x=195, y=150)

    carrera_alu = ttk.Combobox(ventana2, state="readonly", values=[
        "SISTEMAS", "ADMINISTRACION", "LOGISTICA", "ANIMACION", "ELECTROMECANICA", "ENERGIAS RENOVABLES"], font=("calibri", 10))
    carrera_alu.place(x=195, y=175, width=225, height=20)

    semestre_alu = ttk.Combobox(ventana2, state="readonly", values=[
        "1", "2", "3", "4", "5", "6", "7", "8", "9"], font=("calibri", 10))
    semestre_alu.place(x=195, y=200, width=225, height=20)

    Label(ventana2, text="Nombre:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=86)

    Label(ventana2, text="Edad:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=112)

    Label(ventana2, text="Matricula:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=138)

    Label(ventana2, text="Carrera:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=164)

    Label(ventana2, text="Semestre:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=190)

    boton_reg1 = Button(
        ventana2,
        text="REGISTRAR ALUMNO",
        height="2",
        width="30",
        command=guardar_alum
    )
    boton_reg1.place(x=140, y=250)

    boton_most1 = Button(
        ventana2,
        text="Mostrar lista de alumnos",
        height="2",
        width="30",
        command=listadealumnos
    )
    boton_most1.place(x=140, y=300)

    ventana2.mainloop()


def ventanatres():
    global ventana3
    ventana3 = Tk()
    ventana3.title("Registrar Maestro")
    ventana3.geometry("500x400")
    Label(ventana3, text="Hola maestro, por favor ingrese sus datos", fg="midnight blue",
          width="300", height="3", font=("corbel light", 18)).pack()
    Label(ventana3, text="").pack()

    global nombre_maer
    global edad_maer
    global clave_maer
    global carrera_maer
    global asignacion_maer

    nombre_maer = StringVar
    edad_maer = StringVar
    clave_maer = StringVar
    carrera_maer = StringVar
    asignacion_maer = StringVar

    nombre_maer = tk.Entry(ventana3, font=("calibri", 12))
    nombre_maer.place(width=225, height=20, x=195, y=100)

    edad_maer = tk.Entry(ventana3, font=("calibri", 12))
    edad_maer.place(width=225, height=20, x=195, y=125)

    clave_maer = tk.Entry(ventana3, font=("calibri", 12), show="●")
    clave_maer.place(width=225, height=20, x=195, y=150)

    carrera_maer = ttk.Combobox(ventana3, state="readonly", values=[
        "SISTEMAS", "ADMINISTRACION", "LOGISTICA", "ANIMACION", "ELECTROMECANICA", "ENERGIAS RENOVABLES"], font=("calibri", 10))
    carrera_maer.place(x=195, y=175, width=225, height=20)

    asignacion_maer = ttk.Combobox(ventana3, state="readonly", values=[
        "MAT1045", "CBA1145", "CAL1245", "POO1345", "PROG445"], font=("calibri", 10))
    asignacion_maer.place(x=195, y=200, width=225, height=20)

    Label(ventana3, text="Nombre:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=86)

    Label(ventana3, text="Edad:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=112)

    Label(ventana3, text="Clave:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=138)

    Label(ventana3, text="Carrera:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=164)

    Label(ventana3, text="Asignacion:", fg="grey1", width="8",
          height="2", font=("corbel", 11)).place(x=100, y=190)

    boton_reg2 = Button(
        ventana3,
        text="REGISTRAR MAESTRO",
        height="2",
        width="30",
        command=guardar_mae
    )
    boton_reg2.place(x=140, y=250)

    boton_most2 = Button(
        ventana3,
        text="Mostrar lista de registros",
        height="2",
        width="30",
        command=listademaestros
    )
    boton_most2.place(x=140, y=300)

    ventana3.mainloop()

# *****AQUI SE MUESTRA LA LISTA HACIENDO UNA CONSULTA EN LA BASE DE DATOS Y LLAMANDO LA FUNCION PARA AGREGARLO AL TREE


def listadealumnos():
    ventana2.destroy()
    global ventanalista1
    global lista_alum1
    ventanalista1 = tk.Tk()
    ventanalista1.title("Lista de alumnos")
    ventanalista1.geometry("1250x400")

    Label(ventanalista1, text="Alumnos registrados", bg="navy", fg="white",
          width="125", height="2", font=("Calibri", 15)).place(x=0, y=10)

    boton_most1 = Button(
        ventanalista1,
        text="Cerrar lista",
        height="1",
        width="15",
        command=ventanalista1.destroy
    )
    boton_most1.place(x=1000, y=65)

    tabla_alum = LabelFrame(ventanalista1, text="Alumnos")
    tabla_alum.grid(row=2, column=0, columnspan=5, padx=10, pady=5)
    tabla_alum.place(x=10, y=85)

    lista_alum1 = ttk.Treeview(
        tabla_alum, height=12, columns=("#1", "2", "3", "4", "#"))
    lista_alum1.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

    lista_alum1.heading("#0", text="ID", anchor=CENTER)
    lista_alum1.heading("#1", text="Nombre", anchor=CENTER)
    lista_alum1.heading("#2", text="Edad", anchor=CENTER)
    lista_alum1.heading("#3", text="Matricula", anchor=CENTER)
    lista_alum1.heading("#4", text="Carrera", anchor=CENTER)
    lista_alum1.heading("#5", text="Semestre", anchor=CENTER)

    consult_alum()


def listademaestros():
    ventana3.destroy()
    global ventanalista2
    global lista_mae1
    ventanalista2 = tk.Tk()
    ventanalista2.title("Lista de maestros")
    ventanalista2.geometry("1250x400")

    Label(ventanalista2, text="Maestros en el sistema", bg="navy", fg="white",
          width="125", height="2", font=("Calibri", 15)).place(x=0, y=10)

    boton_most2 = Button(
        ventanalista2,
        text="Cerrar lista",
        height="1",
        width="15",
        command=ventanalista2.destroy
    )
    boton_most2.place(x=1000, y=65)

    tabla_mae = LabelFrame(ventanalista2, text="Maestros")
    tabla_mae.grid(row=2, column=0, columnspan=5, padx=10, pady=5)
    tabla_mae.place(x=10, y=85)

    lista_mae1 = ttk.Treeview(
        tabla_mae, height=12, columns=("#1", "2", "3", "4", "#"))
    lista_mae1.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

    lista_mae1.heading("#0", text="ID", anchor=CENTER)
    lista_mae1.heading("#1", text="Nombre", anchor=CENTER)
    lista_mae1.heading("#2", text="Edad", anchor=CENTER)
    lista_mae1.heading("#3", text="Clave", anchor=CENTER)
    lista_mae1.heading("#4", text="Carrera", anchor=CENTER)
    lista_mae1.heading("#5", text="Asignacion", anchor=CENTER)

    consult_mae()


Principal()
