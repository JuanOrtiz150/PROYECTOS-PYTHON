# PRACTICA 1: HACER UN CRUD EN PYTHON USANDO LO APRENDIDO EN LA UNIDAD ANTERIOR
# AUTOR: JUAN CARLOS ORTIZ SALAS
# FECHA: 27/04/23

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql

# CREAR LA TABLA DE DATOS, EN CASO DE QUE NO EXISTA SOLO IR A XAMPP Y CREAR UNA BASE DE DATOS QUE SE LLAME "almacen" PARA QUE EL PROGRAMA
# CREE POR SI SOLO LAS TABLAS Y PUEDA FUNCIONAR


db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="almacen"
)

cursor = db.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS productos (id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(255), cant INT(225), marca VARCHAR(225), estado VARCHAR(225), precio INT(225))")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS login (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), contra VARCHAR(225))")

# Aqui esta la parte del CRUD, agregue funciones para cada accion en la tabla

class saludo ():
    def __init__(self, user_tomar, take_and_salud):
        self.user_tomar = str(user_tomar)
        self.take_and_salud=str(take_and_salud)

    def hi(self):
        pass


class user_saludar(saludo):
    def hi(self):
        self.take_and_salud=user_verify.get()
        return ("Bienvenido {}".format(self.take_and_salud))
        


def valid_uno():
    global multi
    while True:
        try:
            multi = int()
            multi = 0

            multi = int(precio.get())*int(cantidad.get())
            break
        except ValueError:
            messagebox.showerror(
                title="AVISO", message="ERROR AL AGREGAR, VUELVA A INENTAR")
            return

    add_product()

def valid_dos():
    global multi
    while True:
        try:
            multi = int()
            multi = 0

            multi = int(precio.get())*int(cantidad.get())
            break
        except ValueError:
            messagebox.showerror(
                title="AVISO", message="ERROR AL AGREGAR, VUELVA A INENTAR")
            return

    edit_product()
    
def add_product():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="almacen"
    )

    # la funcion multi es para poder calcular el precio total del producto, se le asigna un valor 0 para que cuando se
    # inicie no tome datos erroneos. cabe resaltar que tambien se tiene que especificar el tipo de variable, en este caso INT

    # La variable filacrud me sirve para asignarle el valor de get_children() que hace que tome los valores de la tabla y con el
    # .delete se eliminen para posteriormente agregar los datos actualizados de la base de datos y no encimarlos.

    filacrud = lis_productos.get_children()
    for item in filacrud:
        lis_productos.delete(item)

    sql = "INSERT INTO productos (id, product, cant, marca, estado, precio) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        iid.get(), producto.get(), cantidad.get(), marca.get(), estado.get(), multi)

    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    except pymysql.Error:
        messagebox.showerror("AVISO",
                             "NO SE PUDO AGREGAR EL PRODUCTO")
        return
    finally:

        # aqui se realiza la consulta para tomar los datos ordenados en forma descendente, se puede hacer de forma acendente tambien colocando
        # asc, sin embargo me siento mas comodo usando desc. resalto que se tiene que poner que este ordenado con ORDER BY sino puede causar errores

        consulta = "SELECT * FROM productos ORDER BY id desc"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        for i in datos:
            lis_productos.insert("", 0, text=i[0], values=(
                i[1], i[2], i[3], i[4], i[5]))
        db.close()


def delete_product():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="almacen"
    )

    try:

        # Lo que hago aqui es tomar los datos de la tabla, especificamente la id, con .item y .selection, esto se hace porque al añadir
        # los datos a la tabla, estos se vuelven items por asi decirlo.

        lis_productos.item(lis_productos.selection())['values'][0]

    except IndexError as e:
        # mensaje de error y return para validar que se selecionen los datos
        messagebox.showerror(
            "AVISO", "PORFAVOR PRIMERO SELECCIONA UN ELEMENTO EN LA TABLA")
        return

    # Aqui hago que se borren las entradas de los widgets que tenemos, para que los datos puedan ser manipulados mas facil. aplico tambien el
    # .select y .item para darle un valor a cada uno y remplazarlo

    producto.insert(0, "")
    cantidad.delete(0, tk.END)
    marca.insert(0, "")
    estado.insert(0, "")
    precio.delete(0, tk.END)

    producto_t = lis_productos.item(lis_productos.selection())['values'][0]
    cantidad_t = lis_productos.item(lis_productos.selection())['values'][1]
    marca_t = lis_productos.item(lis_productos.selection())['values'][2]
    estado_t = lis_productos.item(lis_productos.selection())['values'][3]
    precio_t = lis_productos.item(lis_productos.selection())['values'][4]

    producto.set(producto_t)
    cantidad.insert(0, cantidad_t)
    marca.set(marca_t)
    estado.set(estado_t)
    precio.insert(0, precio_t)

    dato = lis_productos.item(lis_productos.selection())['values']
    # aqui uso DELETE FROM para eliminar datos, todo esto se aplica de misma forma a los demas CRUD
    sql = "DELETE FROM productos WHERE id = '{0}'".format(iid.get())

    preg = messagebox.askquestion(
        message="¿ESTA SEGURO DE QUERER ELIMINAR ESTE ELEMENTO?", title="AVISO")
    if preg == 'yes':
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        insertar()
    else:
        messagebox.showerror(message="ERROR AL ELIMINAR", title="AVISO")
        return

    cantidad.insert(0, "")

    # aqui hago lo mismo que en la parte de agregar, para actualizar los datos de la tabla luego de la eliminacion

    filacrud = lis_productos.get_children()
    for item in filacrud:
        lis_productos.delete(item)

    consulta = "SELECT * FROM productos ORDER BY id desc"
    cursor.execute(consulta)

    datos = cursor.fetchall()
    for i in datos:
        lis_productos.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5]))

    db.close()


def edit_product():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="almacen"
    )

    sql = "UPDATE productos SET product = '{0}', cant = '{1}', marca = '{2}', estado = '{3}', precio = '{4}' WHERE id = '{5}'".format(
        producto.get(), cantidad.get(), marca.get(), estado.get(), multi, iid.get())

    preg = messagebox.askquestion(
        message="¿ESTA SEGURO DE QUERER EDITAR ESTE ELEMENTO?", title="AVISO")
    if preg == 'yes':
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    else:
        messagebox.showerror(message="ERROR AL EDITAR", title="AVISO")
        return

    filacrud = lis_productos.get_children()
    for item in filacrud:
        lis_productos.delete(item)

    consulta = "SELECT * FROM productos ORDER BY id desc"
    cursor.execute(consulta)

    datos = cursor.fetchall()
    for i in datos:
        lis_productos.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5]))

    db.close()

# Este insertar sirve para darle valores a la tabla cuando el programa se inicie y asi mantener guardado los datos


def insertar():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="almacen"
    )

    filacrud = lis_productos.get_children()
    for item in filacrud:
        lis_productos.delete(item)

    consulta = "SELECT * FROM productos ORDER BY id desc"
    cursor.execute(consulta)
    # Y los resultados los almacenamos en la variable datos.
    datos = cursor.fetchall()
    for i in datos:
        lis_productos.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5]))
    db.close()

#


# AQUI ESTAN LAS FUNCIONES DE LAS BASE DE DATOS DEL LOGIN


#


def valid():
    if user_entry.get() == "" or contra_entry.get() == "":
        messagebox.showinfo(
            message="Algun campo sigue vacio, vuelva a intentar", title="AVISO DE USUARIO")
    else:
        reg_valid()


def reg_valid():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="almacen"
    )

    fcursor = db.cursor()

    sql = "INSERT INTO login (user, contra) VALUES ('{0}', '{1}')".format(
        user_entry.get(), contra_entry.get())

    try:
        fcursor.execute(sql)
        db.commit()
        vent1()
    except:
        db.rollback()
        messagebox.showinfo(
            message="Registro de usuario fallido, vuelva a intentar", title="AVISO DE USUARIO")
    finally:
        db.close()


def iniciosesion():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="almacen"
    )

    fcursor = db.cursor()

    fcursor.execute("SELECT contra FROM login WHERE user='" +
                    user_verify.get()+"' and contra='"+contra_verify.get()+"'")

    if (fcursor.fetchall()):
        vent3()
    else:
        messagebox.showinfo(title="INICIO DE SESION INCORRECTA",
                            message="EL USUARIO Y CONTRASENA NO SON CORRECTAS :/")

    db.close()

#


# AQUI SE ENCUENTRAN LAS VENTANAS DE LOGIN CATALOGADAS DE VENT1, VENT2, VENT3, ETC...
# En la parte del login no me extendere mucho, es un login que ya realizamos en actividades pasadas,
# para el login se utiliza la otra tabla que se creo dentro de la misma base de datos que se llama "login" y se hace una entrada para
# acceder y registrarse en el sistema.


#
def vent1():
    global ventana1
    global user_verify
    global contra_verify

    ventana1 = tk.Tk()
    ventana1.title("Hola, usuario")
    ventana1.geometry("500x500")
    Label(ventana1, text="Hola usuario, bienvenido", fg="midnight blue",
          width="300", height="3", font=("corbel light", 22)).pack()
    Label(ventana1, text="Inicia sesion para poder acceder", fg="gray1",
          width="300", height="3", font=("corbel light", 10)).pack()
    Label(ventana1, text="").pack()

    Label(ventana1, text="Usuario", fg="gray1",
          width="15", height="3", font=("corbel light", 10)).place(x=190, y=190)

    Label(ventana1, text="Contrasena", fg="gray1",
          width="15", height="3", font=("corbel light", 10)).place(x=190, y=245)

    Label(ventana1, text="¿no tienes usuario?", fg="gray1",
          width="15", height="3", font=("corbel light", 8)).place(x=150, y=400)

    user_verify = tk.Entry(ventana1, font=("calibri light", 12))
    user_verify.place(width=225, height=30, x=135, y=225)

    contra_verify = tk.Entry(ventana1, show="●", font=("calibri light", 12))
    contra_verify.place(width=225, height=30, x=135, y=280)


    boton_ini = Button(
        ventana1,
        text="Entrar",
        fg="midnight blue",
        height="2",
        width="15",
        font=("calibri light", 10),
        command=iniciosesion
    )
    boton_ini.place(x=185, y=335)

    boton_regis = Button(
        ventana1,
        text="Registrarse",
        fg="midnight blue",
        height="1",
        width="11",
        font=("calibri light", 7),
        command=vent2

    )
    boton_regis.place(x=250, y=412)

    ventana1.mainloop()


def vent2():
    ventana1.destroy()

    global user_entry
    global contra_entry
    global ventana_registro
    ventana_registro = tk.Tk()
    ventana_registro.title("Registrate, es gratis")
    ventana_registro.geometry("500x500")

    Label(ventana_registro, text="¿Nuevo? Registrate", fg="midnight blue",
          width="300", height="3", font=("corbel light", 22)).pack()
    Label(ventana_registro, text="EL registro es gratis :)", fg="gray1",
          width="300", height="3", font=("corbel light", 10)).pack()
    Label(ventana_registro, text="").pack()

    Label(ventana_registro, text="Usuario", fg="gray1",
          width="15", height="3", font=("corbel light", 10)).place(x=190, y=190)

    Label(ventana_registro, text="Contrasena", fg="gray1",
          width="15", height="3", font=("corbel light", 10)).place(x=190, y=245)

    user_entry = tk.Entry(ventana_registro, font=("calibri light", 12))
    user_entry.place(width=225, height=30, x=135, y=225)

    contra_entry = tk.Entry(ventana_registro, show="●",
                            font=("calibri light", 12))
    contra_entry.place(width=225, height=30, x=135, y=280)

    boton_reg = Button(
        ventana_registro,
        text="Registrarse",
        fg="midnight blue",
        height="2",
        width="15",
        font=("calibri light", 10),
        command=valid

    )
    boton_reg.place(x=185, y=335)

    boton_regi = Button(
        ventana_registro,
        text="Volver",
        fg="midnight blue",
        height="1",
        width="11",
        font=("calibri light", 7),
        command=vent1

    )
    boton_regi.place(x=210, y=412)

# *******MENU CRUD*******
# Aqui inicia el menu y la tabla de datos, primero creo la ventana y luego defino variables globales, asi como su tipo, (en lo personal uso variables globales
# porque se me hace mas comodo el trabajar de esa manera), luego creo el label frame que es donde ira la tabla.


def vent3():
    global ventana_crud
    ventana_crud = tk.Tk()
    ventana_crud.title("EL ALMACEN")
    ventana_crud.geometry("1280x700")

    global tab_productos
    global lis_productos
    global hiuser

    # VARIABLES DE LOS PRODUCTOS
    global iid
    global producto
    global cantidad
    global marca
    global estado
    global precio

    iid = int()
    cantidad = int()
    precio = int()

    # TABLA DE LOS PRODUCTOS DEL ALMACEN

    tab_productos = LabelFrame(
        ventana_crud, text=" INVENTARIO: ")
    tab_productos.grid(row=7, column=0, columnspan=6, padx=20, pady=25)
    tab_productos.place(x=10, y=300)

    # El treeview se parece mucho a una matriz, asi que solo defino el nombre de las columnas y al ser muy parecido a una matriz inicia en 0 y las columnas 5

    lis_productos = ttk.Treeview(
        tab_productos, height=10, columns=("#1", "#2", "#3", "#4", "#"))
    lis_productos.grid(row=7, column=0, columnspan=4, padx=20, pady=20)

    lis_productos.heading("#0", text="ID", anchor=CENTER)
    lis_productos.heading("#1", text="Producto", anchor=CENTER)
    lis_productos.heading("#2", text="Cantidad", anchor=CENTER)
    lis_productos.heading("#3", text="Marca", anchor=CENTER)
    lis_productos.heading("#4", text="Estado", anchor=CENTER)
    lis_productos.heading("#5", text="Precio", anchor=CENTER)

    move_up = Scrollbar(tab_productos, command=lis_productos.yview)
    move_up.grid(row=7, column=4, sticky="nsew")
    lis_productos.config(yscrollcommand=move_up.set)

    hiuser=user_saludar(user_verify.get(), 0)

    insertar()

    # ENTRADAS PARA QUE FUNCIONE EL CRUD

    Label(ventana_crud, text="ID", fg="snow", bg="gray15", width="15",
          height="1", font=("calibri", 8)).place(x=45, y=50)

    Label(ventana_crud, text="PRODUCTO", fg="snow", bg="gray15", width="15",
          height="1", font=("calibri", 8)).place(x=45, y=80)

    Label(ventana_crud, text="CANTIDAD", fg="snow", bg="gray15", width="15",
          height="1", font=("calibri", 8)).place(x=45, y=110)

    Label(ventana_crud, text="MARCA", fg="snow", bg="gray15", width="15",
          height="1", font=("calibri", 8)).place(x=45, y=140)

    Label(ventana_crud, text="ESTADO", fg="snow", bg="gray15", width="15",
          height="1", font=("calibri", 8)).place(x=45, y=170)

    Label(ventana_crud, text="PRECIO C/U", fg="snow", bg="gray15", width="15",
          height="1", font=("calibri", 8)).place(x=45, y=200)

    Label(ventana_crud, text=hiuser.hi(), fg="midnight blue",
          width="15", height="2", font=("corbel light", 32)).place(x=850, y=25)

    Label(ventana_crud, text="Agrega, elimina o edita lo que necesites", fg="gray1",
          width="35", height="1", font=("corbel light", 12)).place(x=820, y=115)

    Label(ventana_crud, text="(Recuerda agregar \n el id antes de \n eliminar algun dato :))", fg="gray1",
          width="35", height="3", font=("corbel light", 8)).place(x=515, y=100)

    iid = tk.Entry(ventana_crud, font=("calibri light", 12)
                   )
    iid.place(width=225, height=20, x=150, y=50)

    producto = ttk.Combobox(ventana_crud, font=("calibri light", 12), state="readonly", values=[
        "Camiseta", "Tenis", "Blusas deportivas", "calcetas", "Gorras", "Short", "Sport"]
    )
    producto.place(width=225, height=20, x=150, y=80)

    cantidad = tk.Entry(ventana_crud, font=("calibri light", 12)
                        )
    cantidad.place(width=225, height=20, x=150, y=110)

    marca = ttk.Combobox(ventana_crud, font=("calibri light", 12), state="readonly", values=[
        "Cuma", "Licenciado Valeriano", "Air Jorge", "PILA"]
    )
    marca.place(width=225, height=25, x=150, y=140)

    estado = ttk.Combobox(ventana_crud, font=("calibri light", 12), state="readonly", values=[
        "Nuevo", "Seminuevo", "Buen estado"]
    )
    estado.place(width=225, height=25, x=150, y=170)

    precio = tk.Entry(ventana_crud, font=("calibri light", 12)
                      )
    precio.place(width=225, height=20, x=150, y=200)

    boton_add = Button(
        ventana_crud,
        text="Agregar",
        fg="snow",
        bg="gray15",
        height="2",
        width="15",
        font=("calibri light", 10),
        command=valid_uno
    )
    boton_add.place(x=450, y=50)

    boton_delete = Button(
        ventana_crud,
        text="Eliminar",
        fg="snow",
        bg="gray15",
        height="2",
        width="15",
        font=("calibri light", 10),
        command=delete_product
    )
    boton_delete.place(x=450, y=100)

    boton_modify = Button(
        ventana_crud,
        text="Editar",
        fg="snow",
        bg="gray15",
        height="2",
        width="15",
        font=("calibri light", 10),
        command=valid_dos
    )
    boton_modify.place(x=450, y=150)


    ventana_crud.mainloop()


vent1()
