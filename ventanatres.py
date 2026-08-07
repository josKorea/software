import  tkinter as tk
#---window desing object
ventana =tk.Tk()

window=tk.Tk()

window.title("Formulario GUI con grid")

window.geometry("800x500")
#--- creating labels nombre
label_nombre = tk.Label(window, text="Nombre:").grid(row=0, column=0)

#... creating entry for nombre
txt_nombre = tk.Entry(window)
txt_nombre.grid(row=0, column=1)
txt_nombre.grid(row=0, column=1)
window.mainloop()