import tkinter as tk
from tkinter import ttk
#======================
# setting the window
#======================

window=tk.Tk()
window.title("working with widgets")
window.geometry("380x200")
window.resizable(False,False)

#==============================
# title label 
#==============================
tk.Label(window, text="adding widgets").grid(row=0, column=0, padx=2, pady=2, sticky="w")
cmbColor=ttk.Combobox(
    window,
    values=["verde","azul", "amarillo","violeta"] 
)
cmbColor.grid(row=1, column=0, padx=2, pady=2, sticky="w")
cmbDepto=ttk.Combobox(
    window,
    values=[
    "Ahuachapán","Santa Ana","Sonsonate","Chalatenango","La Libertad","San Salvador","Cuscatlán","La Paz","Cabañas","San Vicente","Usulután","San Miguel","Morazán","La Unión"]
    
)
cmbDepto.grid(row=2, column=0, padx=2, pady=2, sticky="w")


#========================
# Ading chckbox
#========================
acepto=0
chkAcepto=tk.Checkbutton(window, text="Acepto los terminos y condiciones", variable=acepto)
chkAcepto.grid(row=3, column=0, padx=2, pady=2, sticky="w")

#========================
# Adding radio buttons
#========================

genero=""
rdbMasculino=tk.Radiobutton(window, text="Masculino", variable=genero, value="M")
rdbMasculino.grid(row=4, column=0, padx=2, pady=2, sticky="w")
rdbFemenino=tk.Radiobutton(window, text="Femenino", variable=genero, value="F")
rdbFemenino.grid(row=5, column=0, padx=2, pady=2, sticky="w")
window.mainloop()