import tkinter as tk
from tkinter import messagebox
#============================
# creating the window object
#============================
w = tk.Tk()
w.title("Getting data From UI controls")
w.geometry("300x250")

#========================
# window title object
#========================
lbl_title = tk.Label(w, text="Getting data from UI controls")
lbl_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


#========================
#funcion get data
#========================
def showData():
    name=text_name.get()
    age=text_age.get()
    messagebox.showinfo("warning", "Data: " "" +name+ " " +age)

#========================
# Name widget and properties
#========================
lbl_name = tk.Label(w, text="Type your name")
lbl_name.grid(row=1, column=0, padx=(10,2), pady=5, sticky="w")

text_name = tk.Entry(w, width=15)
text_name.grid(row=1, column=1, padx=(0,10), pady=5, sticky="w")

#========================
# Age widget and properties
#========================
lbl_age = tk.Label(w, text="Type your age", anchor="w")
lbl_age.grid(row=2, column=0, padx=(10,2), pady=5, sticky="w")
text_age = tk.Entry(w, width=15)
text_age.grid(row=2, column=1, padx=(0,10), pady=5, sticky="w")

btn_GetData=tk.Button(w, text="Show data", command=showData).grid(row=3, column=0, padx=10, pady=5, sticky="w")
btn_GetData=tk.Button(w, text="close window", command=w.destroy).grid(row=3, column=1, padx=10, pady=5, sticky="w")


w.mainloop()