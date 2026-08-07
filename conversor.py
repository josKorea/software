import tkinter as tk
from tkinter import messagebox
#============================
# creating the window object
#============================
w = tk.Tk()
w.title("Conversor de Medidas")
w.geometry("450x220")
#============================
# window title object
#============================
lbl_title = tk.Label(w, text="Conversor de Medidas")
lbl_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#============================
# Libras
#============================
lbl_lb = tk.Label(w, text="Libras:")
lbl_lb.grid(row=1, column=0, padx=10, pady=5, sticky="w")
txt_lb = tk.Entry(w, width=15)
txt_lb.grid(row=1, column=1, padx=10, pady=5)
#============================
# Metros
#============================
lbl_m = tk.Label(w, text="Metros:")
lbl_m.grid(row=2, column=0, padx=10, pady=5, sticky="w")
txt_m = tk.Entry(w, width=15)
txt_m.grid(row=2, column=1, padx=10, pady=5)
#============================
# Yardas
#============================
lbl_y = tk.Label(w, text="Yardas:")
lbl_y.grid(row=3, column=0, padx=10, pady=5, sticky="w")
txt_y = tk.Entry(w, width=15)
txt_y.grid(row=3, column=1, padx=10, pady=5)
#============================
# Funciones
#============================
def convertir_kg():
    libras = float(txt_lb.get())
    kilos = libras * 0.453592
    messagebox.showinfo("Resultado", "Kilogramos: " + str(kilos))
def convertir_km():
    metros = float(txt_m.get())
    km = metros / 1000
    messagebox.showinfo("Resultado", "Kilómetros: " + str(km))
def convertir_cm():
    yardas = float(txt_y.get())
    cm = yardas * 91.44
    messagebox.showinfo("Resultado", "Centímetros: " + str(cm))
#============================
# Buttons
#============================
btn_kg = tk.Button(w, text="Convertir a Kg", width=15, command=convertir_kg).grid(row=1, column=2, padx=10, pady=5)
btn_km = tk.Button(w, text="Convertir a Km", width=15, command=convertir_km).grid(row=2, column=2, padx=10, pady=5)
btn_cm = tk.Button(w, text="Convertir a Cm", width=15, command=convertir_cm).grid(row=3, column=2, padx=10, pady=5)
btn_salir = tk.Button(w, text="Close Window", width=15, command=w.destroy).grid(row=4, column=1, pady=15)
#============================
# Ejecutar ventana
#============================
w.mainloop()