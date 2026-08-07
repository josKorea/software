import tkinter as tk

ventana =tk.Tk()

ventana.title("mi primer Formulario")

ventana.geometry("800x500")
tk.Label(ventana, text="codigo Institucion:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="nombre:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="apellido:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="grado:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="seccion:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="edad:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="fecha de nac:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="especialidad:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="NIE:").pack()
tk.Entry(ventana).pack()
tk.Label(ventana, text="N° de dui Responsable:").pack()
tk.Entry(ventana).pack()



tk.Button(ventana, text="Guardad").pack()
tk.Button(ventana, text="Salir").pack()

ventana.mainloop()