import tkinter as tk

# ------------------------------
# Ventana principal (padre)
# ------------------------------
ventana = tk.Tk()
ventana.title("Formulario Padre")
ventana.geometry("400x350")

tk.Label(ventana, text="FORMULARIO PADRE", font=("Arial", 16, "bold")).pack(pady=20)

tk.Label(ventana, text="Nombre recibido:").pack()
entry_nombre_padre = tk.Entry(ventana, width=30)
entry_nombre_padre.pack(pady=5)

tk.Label(ventana, text="Edad recibida:").pack()
entry_edad_padre = tk.Entry(ventana, width=30)
entry_edad_padre.pack(pady=5)


# ------------------------------
# Función que abre el modal
# ------------------------------
def abrir_modal():
    modal = tk.Toplevel(ventana)
    modal.title("Formulario Modal")
    modal.geometry("300x250")
    modal.grab_set()  # bloquea la ventana padre mientras el modal esté abierto

    tk.Label(modal, text="Nombre:").pack(pady=(20, 0))
    entry_nombre_modal = tk.Entry(modal, width=25)
    entry_nombre_modal.pack(pady=5)

    tk.Label(modal, text="Edad:").pack(pady=(10, 0))
    entry_edad_modal = tk.Entry(modal, width=25)
    entry_edad_modal.pack(pady=5)

    # Al presionar Aceptar, copiamos los datos al formulario padre
    def aceptar():
        nombre = entry_nombre_modal.get()
        edad = entry_edad_modal.get()

        entry_nombre_padre.delete(0, tk.END)
        entry_nombre_padre.insert(0, nombre)

        entry_edad_padre.delete(0, tk.END)
        entry_edad_padre.insert(0, edad)

        modal.destroy()

    frame_botones = tk.Frame(modal)
    frame_botones.pack(pady=20)

    tk.Button(frame_botones, text="Aceptar", command=aceptar).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Cancelar", command=modal.destroy).pack(side="left", padx=5)


tk.Button(ventana, text="Abrir formulario modal", command=abrir_modal).pack(pady=30)

ventana.mainloop()