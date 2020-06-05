from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
import pandas as pd
import os
from pandas import ExcelWriter

dic1={'Nombre del producto' : [],'ID': [],'Cantidad': [],'Proveedor': [],'Precio($)': []}

df = pd.DataFrame(dic1)
df = df[['Nombre del producto','ID','Cantidad','Proveedor','Precio($)']]
writer = ExcelWriter('Inventario.xlsx')
df.to_excel(writer, 'Hoja de datos', index=False)
MessageBox.showinfo("Info","Se ha generado un archivo excel en la carpeta actual con el nombre 'Inventario' ")
writer.save()

