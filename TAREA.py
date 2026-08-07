import tkinter as tk
from tkinter import ttk

#======================
# Función para mostrar datos
#======================
def mostrar_datos():
    print("Nombre:", txtNombre.get())
    print("Bachillerato:", cmbBachillerato.get())
    print("Género:", genero.get())

    if beca.get() == "B":
        print("Posee beca: Sí")
    else:
        print("Posee beca: No")

#======================
# Ventana
#======================
window = tk.Tk()
window.title("Trabajando con Widgets")
window.geometry("800x500")
window.resizable(False, False)

tk.Label(window, text="Nombre").grid(row=0, column=0, padx=10, pady=10, sticky="w")

txtNombre = tk.Entry(window, width=30)
txtNombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Bachillerato").grid(row=1, column=0, padx=10, pady=10, sticky="w")

cmbBachillerato = ttk.Combobox(
    window,
    values=["Software", "Agropecuario", "Contador", "General"]
)
cmbBachillerato.grid(row=1, column=1, padx=10, pady=10)
tk.Label(window, text="Género").grid(row=2, column=0, padx=10, pady=10, sticky="w")

genero = tk.StringVar()
rdbMasculino = tk.Radiobutton(window, text="Masculino", variable=genero, value="Masculino")
rdbMasculino.grid(row=2, column=1, sticky="w")
rdbFemenino = tk.Radiobutton(window, text="Femenino", variable=genero, value="Femenino")
rdbFemenino.grid(row=3, column=1, sticky="w")

beca = tk.StringVar()

chkBeca = tk.Checkbutton(window, text="Posee beca", variable=beca, onvalue="B", offvalue="")
chkBeca.grid(row=4, column=1, sticky="w")

btnMostrar = tk.Button(window, text="Mostrar datos", command=mostrar_datos)
btnMostrar.grid(row=5, column=1, padx=10, pady=20)

window.mainloop()