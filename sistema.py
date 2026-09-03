import tkinter as tk
from tkinter import messagebox

# -----------------------------------
# 1. Crear ventana principal
# -----------------------------------
ventana = tk.Tk()
ventana.title("Sistema Académico - Menú Principal")
ventana.geometry("500x300")


# -----------------------------------
# 2. Funciones para abrir formularios
# -----------------------------------

def formulario_estudiante():
    form = tk.Toplevel(ventana)
    form.title("Formulario de Estudiante")
    form.geometry("350x300")

    tk.Label(form, text="Nombre:").pack(pady=(15, 0))
    entry_nombre = tk.Entry(form, width=30)
    entry_nombre.pack()

    tk.Label(form, text="Apellido:").pack(pady=(10, 0))
    entry_apellido = tk.Entry(form, width=30)
    entry_apellido.pack()

    tk.Label(form, text="Edad:").pack(pady=(10, 0))
    entry_edad = tk.Entry(form, width=30)
    entry_edad.pack()

    tk.Label(form, text="Grado:").pack(pady=(10, 0))
    entry_grado = tk.Entry(form, width=30)
    entry_grado.pack()

    def guardar_estudiante():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        edad = entry_edad.get()
        grado = entry_grado.get()

        if not nombre or not apellido:
            messagebox.showwarning("Atención", "Nombre y apellido son obligatorios")
            return

        messagebox.showinfo(
            "Estudiante guardado",
            f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nGrado: {grado}"
        )
        form.destroy()

    tk.Button(form, text="Guardar", command=guardar_estudiante).pack(pady=20)


def formulario_docente():
    form = tk.Toplevel(ventana)
    form.title("Formulario de Docente")
    form.geometry("350x300")

    tk.Label(form, text="Nombre:").pack(pady=(15, 0))
    entry_nombre = tk.Entry(form, width=30)
    entry_nombre.pack()

    tk.Label(form, text="Apellido:").pack(pady=(10, 0))
    entry_apellido = tk.Entry(form, width=30)
    entry_apellido.pack()

    tk.Label(form, text="Especialidad:").pack(pady=(10, 0))
    entry_especialidad = tk.Entry(form, width=30)
    entry_especialidad.pack()

    tk.Label(form, text="Teléfono:").pack(pady=(10, 0))
    entry_telefono = tk.Entry(form, width=30)
    entry_telefono.pack()

    def guardar_docente():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        especialidad = entry_especialidad.get()
        telefono = entry_telefono.get()

        if not nombre or not apellido:
            messagebox.showwarning("Atención", "Nombre y apellido son obligatorios")
            return

        messagebox.showinfo(
            "Docente guardado",
            f"Nombre: {nombre}\nApellido: {apellido}\nEspecialidad: {especialidad}\nTeléfono: {telefono}"
        )
        form.destroy()

    tk.Button(form, text="Guardar", command=guardar_docente).pack(pady=20)


def formulario_sede():
    form = tk.Toplevel(ventana)
    form.title("Formulario de Sede")
    form.geometry("350x260")

    tk.Label(form, text="Nombre de la Sede:").pack(pady=(15, 0))
    entry_nombre = tk.Entry(form, width=30)
    entry_nombre.pack()

    tk.Label(form, text="Dirección:").pack(pady=(10, 0))
    entry_direccion = tk.Entry(form, width=30)
    entry_direccion.pack()

    tk.Label(form, text="Teléfono:").pack(pady=(10, 0))
    entry_telefono = tk.Entry(form, width=30)
    entry_telefono.pack()

    def guardar_sede():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()

        if not nombre:
            messagebox.showwarning("Atención", "El nombre de la sede es obligatorio")
            return

        messagebox.showinfo(
            "Sede guardada",
            f"Nombre: {nombre}\nDirección: {direccion}\nTeléfono: {telefono}"
        )
        form.destroy()

    tk.Button(form, text="Guardar", command=guardar_sede).pack(pady=20)


# -----------------------------------
# 3. Crear menú principal
# -----------------------------------
menu_principal = tk.Menu(ventana)

# --- Menú Estudiante ---
menu_estudiante = tk.Menu(menu_principal, tearoff=0)
menu_estudiante.add_command(label="Registrar Estudiante", command=formulario_estudiante)
menu_principal.add_cascade(label="Estudiante", menu=menu_estudiante)

# --- Menú Docentes ---
menu_docentes = tk.Menu(menu_principal, tearoff=0)
menu_docentes.add_command(label="Registrar Docente", command=formulario_docente)
menu_principal.add_cascade(label="Docentes", menu=menu_docentes)

# --- Menú Sede ---
menu_sede = tk.Menu(menu_principal, tearoff=0)
menu_sede.add_command(label="Registrar Sede", command=formulario_sede)
menu_principal.add_cascade(label="Sede", menu=menu_sede)

# -----------------------------------
# 4. Asignar menú a la ventana
# -----------------------------------
ventana.config(menu=menu_principal)

# -----------------------------------
# 5. Etiqueta de bienvenida
# -----------------------------------
tk.Label(
    ventana,
    text="Sistema Académico\nSelecciona una opción del menú",
    font=("Arial", 14),
    justify="center"
).pack(expand=True)

# -----------------------------------
# 6. Ejecutar aplicación
# -----------------------------------
ventana.mainloop()