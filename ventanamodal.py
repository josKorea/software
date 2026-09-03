import tkinter as tk

root = tk.Tk()
root.title("this is the parent window")
root.geometry("350x250")

# adding the label control  to preset window

lbl_title=tk.Label(root, text="this is the main form")
lbl_title.grid(column=0, row=0, padx=5,pady=5,sticky="w")

lbltexto=tk.Label(root,text="texto reciclado").grid(column=0,row=1,padx=5,pady=5,sticky="w")
txttexto=tk.Entry(root)
txttexto.grid(column=1,row=1,padx=5,pady=5,sticky="w")
def abriModal():
    ventanaModa = tk.Toplevel(root)
    ventanaModa.title("Estas en la ventana modal")
    ventanaModa.geometry("250x250")
    ventanaModa.resizable(False, False)
    lbl_title_modal = tk.Label(ventanaModa, text="texto a pasar").grid(column=0,row=0,padx=5,pady=5,sticky="w")
     


    txt_modal1 = tk.Entry(ventanaModa)
    txt_modal1.grid(column=0, row=0, padx=5, pady=10)

    txt_modal2 = tk.Entry(ventanaModa)
    txt_modal2.grid(column=0, row=1, padx=5, pady=10)


lbl_title = tk.Label(root, text="this is the main form")
lbl_title.grid(column=0, row=0, padx=5, pady=5)

txt1 = tk.Entry(root)
txt1.grid(column=0, row=1, padx=5, pady=5)

txt2 = tk.Entry(root)
txt2.grid(column=0, row=2, padx=5, pady=5)

txt3 = tk.Entry(root)
txt3.grid(column=0, row=3, padx=5, pady=5)

btn_abrirModal = tk.Button(root, text="Abrir", command=abriModal)
btn_abrirModal.grid(column=0, row=4, padx=5, pady=5)

btn_cerrar = tk.Button(root, text="Close window", command=root.destroy)
btn_cerrar.grid(column=1, row=4, padx=5, pady=5)


root.mainloop()