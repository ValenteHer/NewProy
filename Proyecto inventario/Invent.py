from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
import pandas as pd
import os
from pandas import ExcelWriter
from openpyxl import load_workbook


def MainMain():

	def dataR1():	

		def Agregar():
			resultado = MessageBox.askquestion("Salir", "Esta seguro que desea agregar este producto")

			if resultado == "yes":

				dic1={'Nombre del producto' : [],'ID': [],'Cantidad': [],'Proveedor': [],'Precio($)': []}

				dic1['Nombre del producto'].append(Nombre.get())
				dic1['ID'].append(ID.get())
				dic1['Cantidad'].append(float(Cantidad.get()))
				dic1['Proveedor'].append(Proveedor.get())
				dic1['Precio($)'].append(float(Precio.get()))

				print(dic1)

				df = pd.DataFrame(dic1)
				writer = ExcelWriter('Inventario2.xlsx')
				df.to_excel(writer, sheet_name = 'Inventario2', index=False)
				writer.save()

				df2 = pd.read_excel('Inventario.xlsx')

				df3 = pd.concat([df2,df])

				writer = ExcelWriter('Inventario.xlsx')
				df3.to_excel(writer, sheet_name = 'Inventario', index=False)
				writer.save()


				MessageBox.showinfo("Info","Se ha actualizado la base de datos")

				Nombre.set("")
				ID.set("")
				Cantidad.set("")
				Proveedor.set("")
				Precio.set("")

				root2.destroy()

			else:
				root2.destroy()

		def cerrar():
			root2.destroy()

		root2 = Toplevel()		
		root2.title("datos")
		root2.resizable(0,0)
		root2.geometry('350x300')

		label = Label(root2, text = "Nombre del producto")
		label.grid(row = 0, column = 0, sticky = "e", padx = 5, pady = 5)
		entry = Entry(root2)
		entry.grid(row = 0, column = 1, padx = 5, pady = 5)
		entry.config(justify = "center",textvariable = Nombre, state = "normal")

		label2 = Label(root2, text = "ID")
		label2.grid(row = 1, column = 0, sticky = "e", padx = 5, pady = 5)
		entry2 = Entry(root2)
		entry2.grid(row = 1, column = 1, padx = 5, pady = 5)
		entry2.config(justify = "center",textvariable =ID)

		label3 = Label(root2, text = "Cantidad")
		label3.grid(row = 2, column = 0, sticky = "e", padx = 5, pady = 5)
		entry3 = Entry(root2)
		entry3.grid(row = 2, column = 1, padx = 5, pady = 5)
		entry3.config(justify = "center",textvariable =Cantidad)

		label4 = Label(root2, text = "Proveedor")
		label4.grid(row = 3, column = 0, sticky = "e", padx = 5, pady = 5)
		entry4 = Entry(root2)
		entry4.grid(row = 3, column = 1, padx = 5, pady = 5)
		entry4.config(justify = "center",textvariable =Proveedor)

		label5 = Label(root2, text = "Precio ($)")
		label5.grid(row = 4, column = 0, sticky = "e", padx = 5, pady = 5)
		entry5 = Entry(root2)
		entry5.grid(row = 4, column = 1, padx = 5, pady = 5)
		entry5.config(justify = "center",textvariable =Precio)

		boton1 = Button(root2, text="  AGREGAR  ", command = Agregar)
		boton1.grid(row = 6, column = 1, padx = 5, pady = 5)

		boton2 = Button(root2, text="  CANCELAR  ", command = cerrar)
		boton2.grid(row = 7, column = 1, padx = 5, pady = 5)	



	def dataR2():

		def Actualizar():

			resultado = MessageBox.askquestion("Salir", "¿Esta seguro que desea actualizar este producto?")

			if resultado == "yes":

				df2 = pd.read_excel('Inventario.xlsx')

				for I in df2['ID'].tolist():

					print(ID.get())

					if I == float(ID.get()):

						ide = I
						cant = Cantidad.get()
						mask =df2['ID'] == ide
						print(mask)
						DF = df2[mask]
						n_row = DF.index.values[0] #obtengo el valor del indice
						print(n_row)
						df2.loc[n_row,'Cantidad'] = df2.loc[n_row,'Cantidad'] + float(cant)

						df3 = df2

						writer = ExcelWriter('Inventario.xlsx')
						df3.to_excel(writer, sheet_name = 'Inventario', index=False)
						writer.save()

						MessageBox.showinfo("Info","Se ha actualizado el producto")

						roo.destroy()
						break

					else:
						pass

			else:
				pass

		def cerrar():
			roo.destroy()

		roo = Toplevel()		
		roo.title("Actualizar")
		roo.resizable(0,0)
		roo.geometry('300x200')

		ID = StringVar()
		Cantidad = StringVar()

		label2 = Label(roo, text = "ID")
		label2.grid(row = 1, column = 0, sticky = "e", padx = 5, pady = 5)
		entry2 = Entry(roo)
		entry2.grid(row = 1, column = 1, padx = 5, pady = 5)
		entry2.config(justify = "center",textvariable =ID)

		label3 = Label(roo, text = "Cantidad que será agregada")
		label3.grid(row = 2, column = 0, sticky = "e", padx = 5, pady = 5)
		entry3 = Entry(roo)
		entry3.grid(row = 2, column = 1, padx = 5, pady = 5)
		entry3.config(justify = "center",textvariable = Cantidad)

		boton1 = Button(roo, text="  Actualizar  ", command = Actualizar)
		boton1.grid(row = 3, column = 1, padx = 5, pady = 5)
		boton2 = Button(roo, text="  CANCELAR  ", command = cerrar)
		boton2.grid(row = 4, column = 1, padx = 5, pady = 5)



	def dataR3():

		def Eliminar():

			resultado = MessageBox.askquestion("Salir", "¿Está seguro que desea eliminar este producto?")

			if resultado == "yes":

				df2 = pd.read_excel('Inventario.xlsx')

				for I in df2['ID'].tolist():

					print(I)

					if I == float(ID.get()):

						print(I)

						ide = I
						cant = Cantidad.get()
						mask = df2['ID'] == ide
						print(mask)
						DF = df2[mask]
						n_row = DF.index.values[0] #obtengo el valor del indice
						print(n_row)
						df2.loc[n_row,'Cantidad'] = df2.loc[n_row,'Cantidad'] - float(cant)

						df3 = df2

						writer = ExcelWriter('Inventario.xlsx')
						df3.to_excel(writer, sheet_name = 'Inventario', index=False)
						writer.save()

						MessageBox.showinfo("Info","Se ha eliminado el(los) producto")

						root2.destroy()
						break

					else:
						pass

			else:
				pass
		def cerrar():
			root2.destroy()

		ID = StringVar()
		Cantidad = StringVar()
				
		root2 = Toplevel()		
		root2.title("datos")
		root2.resizable(0,0)
		root2.geometry('300x200')
		root2.iconbitmap()

		label2 = Label(root2, text = "ID")
		label2.grid(row = 1, column = 0, sticky = "e", padx = 5, pady = 5)
		entry2 = Entry(root2)
		entry2.grid(row = 1, column = 1, padx = 5, pady = 5)
		entry2.config(justify = "center",textvariable = ID )

		label3 = Label(root2, text = "Cantidad")
		label3.grid(row = 2, column = 0, sticky = "e", padx = 5, pady = 5)
		entry3 = Entry(root2)
		entry3.grid(row = 2, column = 1, padx = 5, pady = 5)
		entry3.config(justify = "center",textvariable = Cantidad )

		boton1 = Button(root2, text="  ELIMINAR  ", command = Eliminar)
		boton1.grid(row = 3, column = 1, padx = 5, pady = 5)
		boton2 = Button(root2, text="  CANCELAR  ", command = cerrar)
		boton2.grid(row = 4, column = 1, padx = 5, pady = 5)


	def dataR4():

		def cerrar():
			root4.destroy()

		def Consulta():

			opcion = StringVar()
			opcion.set(None)

			df2 = pd.read_excel('Inventario.xlsx')

			for I in df2['ID'].tolist():

				print(I)

				if I == float(ID.get()):

					print(I)

					ide = I
					mask = df2['ID'] == ide
					print(mask)
					DF = df2[mask]
					n_row = DF.index.values[0] #obtengo el valor del indice
					print(n_row)
					A = df2.loc[n_row,'Cantidad']
					opcion.set(A)

			room = Toplevel()
			room.title("Consulta")
			room.resizable(0,0)
			room.geometry('300x170')
			room.iconbitmap()



			Label(room, text = "").pack()

			Label(room, text = "Existe:", font = ("Microsoft YaHei",10)).pack()

			Label(room, text = "").pack()

			Label(room, textvariable = opcion).pack()		

			Label(room, text = "").pack()

			Label(room, text = " unidades del producto con el ID con sultado:", font = ("Microsoft YaHei",10)).pack()


		root4 = Toplevel()		
		root4.title("Consulta ID")
		root4.resizable(0,0)
		root4.geometry('200x150')
		root4.iconbitmap()

		label2 = Label(root4, text = "ID")
		label2.grid(row = 0, column = 0, sticky = "e", padx = 5, pady = 5)
		entry2 = Entry(root4)
		entry2.grid(row = 0, column = 1, padx = 5, pady = 5)
		entry2.config(justify = "center",textvariable = ID )

		boton1 = Button(root4, text="  CONSULTAR  ", command = Consulta)
		boton1.grid(row = 3, column = 1, padx = 5, pady = 5)
		boton2 = Button(root4, text="  CANCELAR  ", command = cerrar)
		boton2.grid(row = 4, column = 1, padx = 5, pady = 5)

	def choose():

		if opcion.get() == "Consuntará la existecia de un producto":
			dataR4()

		if opcion.get() == "Eliminará un producto existente del inventario":
			dataR3()

		if opcion.get() == "Introducirá los datos de un producto que desea actualizar":
			dataR2()

		if opcion.get() == "Introducirá los datos de un producto nuevo al inventario":
			dataR1()

	def seleccionar():
		monitor.config(text="{}".format(opcion.get()), font = ("Microsoft YaHei",10))

	ventana_principal.destroy()
	global root
	root = Tk()
	root.title("Invent")
	root.resizable(0,0)
	root.geometry('500x350')
	root.iconbitmap()

	Nombre = StringVar()
	ID = StringVar()
	Cantidad = StringVar()
	Proveedor = StringVar()
	Precio = StringVar()

	Label(root, text = "BIENVENIDO AL SISTEMA DE INVENTARIO", font =("Microsoft YaHei",16)).pack(anchor = "n")
	Label(root, text = " ").pack()

	texto = StringVar()
	texto.set("¿QUÉ DESEA HACER?")

	label = Label(root, text = "¿QUÉ DESEA HACER?", font = ("Microsoft YaHei",12))
	label.pack(anchor = "center")
	label.config(textvariable = texto)

	Label(root, text = "").pack()

	opcion = StringVar()
	opcion.set(None)

	Radiobutton(root, text = "Agregar producto al inventario", variable = opcion, value = "Introducirá los datos de un producto nuevo al inventario", command = seleccionar).pack()
	Radiobutton(root, text = "Actualizar producto en inventario", variable = opcion, value = "Introducirá los datos de un producto que desea actualizar", command = seleccionar).pack()
	Radiobutton(root, text = "Eliminar producto al inventario", variable = opcion, value = "Eliminará un producto existente del inventario", command = seleccionar).pack()
	Radiobutton(root, text = "Consultar existencia de producto", variable = opcion, value = "Consuntará la existecia de un producto", command = seleccionar).pack()

	Label(root, text = "").pack()

	monitor = Label(root)
	monitor.pack()

	Label(root, text = "").pack()

	Button(root, text="  ACEPTAR  ", command = choose).pack(side = "top")

	Label(root, text = "").pack()

#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", width="300", height="2", font=("Microsoft YaHei",13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"
 
    Label(ventana_registro, text="Introduzca datos").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, command = registro_usuario).pack() #BOTÓN "Registrarse"


#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".

def borrar_exito_login():
    ventana_exito.destroy()
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=MainMain).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
  
 
#VENTANA DE "Usuario no encontrado".ventana_no_clave
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"
    

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", font=("Microsoft YaHei",13)).pack()


 
 
ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.


