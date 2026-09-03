import tkinter as tk
from tkinter import messagebox

# -----------------------------------
# 1. Crear ventana principal
# -----------------------------------
ventana = tk.Tk()
ventana.title("Menú con Subopciones")
ventana.geometry("500x300")


# -----------------------------------
# 2. Funciones de las opciones
# -----------------------------------
def nuevo():
    messagebox.showinfo("Nuevo", "Has seleccionado Nuevo")


def abrir():
    messagebox.showinfo("Abrir", "Has seleccionado Abrir")


def guardar():
    messagebox.showinfo("Guardar", "Has seleccionado Guardar")


def salir():
    ventana.destroy()


def primero():
    ventana.destroy()
    messagebox.showinfo("Primero", "Has seleccionado Primero")

def segundo():
    ventana.destroy()
    messagebox.showinfo("Segundo", "Has seleccionado Segundo")

def tercero():
    ventana.destroy()
    messagebox.showinfo("Tercero", "Has seleccionado Tercero")

# -----------------------------------
# 3. Crear menú principal
# -----------------------------------
menu_principal = tk.Menu(ventana)


# -----------------------------------
# 4. Crear submenú Archivo
# -----------------------------------
menu_archivo = tk.Menu(menu_principal, tearoff=0)

menu_archivo.add_command(
    label="Nuevo",
    command=nuevo
)

menu_archivo.add_command(
    label="Abrir",
    command=abrir
)

menu_archivo.add_command(
    label="Guardar",
    command=guardar
)

menu_archivo.add_separator()

menu_archivo.add_command(
    label="Salir",
    command=salir
)


# -----------------------------------
# 5. Agregar el submenú Archivo
#    al menú principal
# -----------------------------------
menu_principal.add_cascade(
    label="Archivo",
    menu=menu_archivo
)


# -----------------------------------
# 6. Crear otro menú
# -----------------------------------
menu_ayuda = tk.Menu(menu_principal, tearoff=0)

menu_ayuda.add_command(
    label="Acerca de",
    command=lambda: messagebox.showinfo(
        "Acerca de",
        "Aplicación desarrollada con Python y Tkinter"
    )
)

menu_ayuda.add_command(
    label="Licencia",
    command=lambda: messagebox.showinfo(
        "Licencia",
        "Software educativo"
    )
)


# -----------------------------------
# 7. Agregar menú Ayuda
# -----------------------------------
menu_principal.add_cascade(
    label="Ayuda",
    menu=menu_ayuda
)

menu_softeare = tk.Menu(menu_principal, tearoff=0)

menu_softeare.add_command(
    label="primero",
    command=primero
)

menu_softeare.add_command(
    label="segundo",
    command=segundo     
)
menu_softeare.add_command(
    label="tercero",
    command=tercero
)
menu_principal.add_cascade(
    label="Software",
    menu=menu_softeare
)
# -----------------------------------
# 8. Agregar el menú a la ventana
# -----------------------------------
ventana.config(menu=menu_principal)


# -----------------------------------
# 9. Ejecutar aplicación
# -----------------------------------
ventana.mainloop()
