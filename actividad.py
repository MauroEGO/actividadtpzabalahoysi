from tkinter import *

##################################################################

raiz=Tk()
raiz.title("actividad")
raiz.config(bg="violet", padx=20, pady=20)

label1=Label(raiz, text="Parcial Estudiante: Dahbar Franco, Garcìa Mauro", bg="violet", fg="yellow")
label1.pack()

ventana=Frame(raiz, bg="green", height=400, width=20)
ventana.pack()

##################################################################

botonverde=Button(ventana, text="Verde", fg="green", bg="violet")
botonverde.grid(row=1, column=0)

botonamarillo=Button(ventana, text="Amarillo", fg="yellow", bg="violet")
botonamarillo.grid(row=1, column=1)

botonrojo=Button(ventana, text="Rojo", fg="red", bg="violet")
botonrojo.grid(row=1, column=2)

##################################################################

labelnombre=Label(ventana, text="Nombre", bg="violet")
labelnombre.grid(row=2, column=0)


labelapellido=Label(ventana, text="Apellido", bg="violet")
labelapellido.grid(row=3, column=0)


labeldni=Label(ventana, text="DNI", bg="violet")
labeldni.grid(row=4, column=0)


labelcomentarios=Label(ventana, text="Comentarios", bg="violet")
labelcomentarios.grid(row=5, column=0, sticky="n")

##################################################################

entrynombre=Entry(ventana)
entrynombre.grid(row=2, column=1)

entryapellido=Entry(ventana)
entryapellido.grid(row=3, column=1)

entrydni=Entry(ventana)
entrydni.grid(row=4, column=1)

entrycomentarios=Text(ventana, height=5, width=15)
entrycomentarios.grid(row=5, column=1)

comentarioscroll=Scrollbar(ventana)
comentarioscroll.grid(row=5, column=2)

##################################################################

boton1=Button(raiz, text="enviar")
boton1.pack()

##################################################################

raiz.mainloop()