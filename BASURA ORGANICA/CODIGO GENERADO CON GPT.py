import tkinter as tk
import sqlite3

# Creamos una conexión a la base de datos
conn = sqlite3.connect('alumnos.db')

# Creamos una tabla 'alumnos' si no existe
conn.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                grado TEXT NOT NULL,
                seccion TEXT NOT NULL
              )''')

# Función para insertar un nuevo alumno en la base de datos


def insertar_alumno():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    grado = entry_grado.get()
    seccion = entry_seccion.get()

    conn.execute('INSERT INTO alumnos (nombre, edad, grado, seccion) VALUES (?, ?, ?, ?)',
                 (nombre, edad, grado, seccion))
    conn.commit()

    # Limpiamos los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_grado.delete(0, tk.END)
    entry_seccion.delete(0, tk.END)


# Creamos la ventana principal
root = tk.Tk()
root.title('Registro de Alumnos')

# Creamos los campos de entrada y etiquetas correspondientes
label_nombre = tk.Label(root, text='Nombre:')
label_nombre.grid(row=0, column=0, padx=5, pady=5)

entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_edad = tk.Label(root, text='Edad:')
label_edad.grid(row=1, column=0, padx=5, pady=5)

entry_edad = tk.Entry(root)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

label_grado = tk.Label(root, text='Grado:')
label_grado.grid(row=2, column=0, padx=5, pady=5)

entry_grado = tk.Entry(root)
entry_grado.grid(row=2, column=1, padx=5, pady=5)

label_seccion = tk.Label(root, text='Sección:')
label_seccion.grid(row=3, column=0, padx=5, pady=5)

entry_seccion = tk.Entry(root)
entry_seccion.grid(row=3, column=1, padx=5, pady=5)

# Creamos el botón para insertar un nuevo alumno
button_insertar = tk.Button(root, text='Insertar', command=insertar_alumno)
button_insertar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Mostramos la ventana principal
root.mainloop()

# Cerramos la conexión a la base de datos
conn.close()
