import tkinter as tk

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


def formulario_docente():
    form = tk.Toplevel(ventana)
    form.title("Formulario de Docente")
    form.geometry("350x300")


def formulario_sede():
    form = tk.Toplevel(ventana)
    form.title("Formulario de Sede")
    form.geometry("350x260")


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