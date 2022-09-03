import tkinter
from tkinter import ttk

window = tkinter.Tk()


def reiniciar(event):
    selected.set(None)



window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="hola", value=1, variable=selected)
r2 = ttk.Radiobutton(window, text="adios", value=2, variable=selected)
boton = tkinter.Button(window, text="reiniciar")
boton.bind('<Button-1>', reiniciar)

r1.grid(column=0, row=0)
r2.grid(column=0, row=1)
boton.grid(column=1, row=3)
window.mainloop()
