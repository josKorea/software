import tkinter as tk
from tkinter import messagebox
#============================
# creating the window object
#============================
w = tk.Tk()
w.title("calculadora basica")
w.geometry("300x300")
#========================
# window title object
#========================
lbl_title = tk.Label(w, text="Basic Calculator"); lbl_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
#========================
# Numero 1 widget and properties
#========================
lbl_num1 = tk.Label(w, text="Numero 1:"); lbl_num1.grid(row=1, column=0, padx=(10,2), pady=5, sticky="w")
text_num1 = tk.Entry(w, width=15); text_num1.grid(row=1, column=1, padx=(0,10), pady=5, sticky="w")
#========================
# Numero 2 widget and properties
#========================
lbl_num2 = tk.Label(w, text="Numero 2:"); lbl_num2.grid(row=2, column=0, padx=(10,2), pady=5, sticky="w")
text_num2 = tk.Entry(w, width=15); text_num2.grid(row=2, column=1, padx=(0,10), pady=5, sticky="w")
#=======================
# funciones de operaciones
#========================v 
def sumar():
    n1 = float(text_num1.get())
    n2 = float(text_num2.get())
    messagebox.showinfo("Warning", "Data: " + str(n1 + n2))
def restar():
    n1 = float(text_num1.get())
    n2 = float(text_num2.get())
    messagebox.showinfo("Warning", "Data: " + str(n1 - n2))
def multiplicar():
    n1 = float(text_num1.get())
    n2 = float(text_num2.get())
    messagebox.showinfo("Warning", "Data: " + str(n1 * n2))
def dividir():
    n1 = float(text_num1.get())
    n2 = float(text_num2.get())
    messagebox.showinfo("Warning", "Data: " + str(n1 / n2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
#========================
# Buttons de operaciones
#========================
btn_sum = tk.Button(w, text="+", width=8, command=sumar); btn_sum.grid(row=3, column=0, padx=10, pady=5, sticky="w")
btn_res = tk.Button(w, text="-", width=8, command=restar); btn_res.grid(row=3, column=1, padx=10, pady=5, sticky="w")
btn_mul = tk.Button(w, text="*", width=8, command=multiplicar); btn_mul.grid(row=4, column=0, padx=10, pady=5, sticky="w")
btn_div = tk.Button(w, text="/", width=8, command=dividir); btn_div.grid(row=4, column=1, padx=10, pady=5, sticky="w")
btn_GetData=tk.Button(w, text="close window", command=w.destroy).grid(row=5, column=0, padx=10, pady=5, sticky="w")
w.mainloop()  