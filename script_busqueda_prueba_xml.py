#! python3
import sys, os, fileinput
from xml.dom import minidom

def cuales_son(archivos, objeto, key, value):

	f = open(archivos)
	dato = f.readline()
	if dato.startswith('<archimate:' + objeto):

		
		doc = minidom.parse(archivos)
		itemlist = doc.getElementsByTagName("properties")
		
		for n in itemlist:
		    
		    key_n = n.attributes["key"].value
		    value_n = n.attributes["value"].value
		    if key_n == "Nombre DNS":
		    	nombre = value_n
		    elif key_n == key:
		    	if value_n == value:
		    		print(nombre)
	f.close()


def devolverArchivos(carpeta, objeto, key, value):

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			cuales_son(os.path.join(carpeta,archivo), objeto, key, value)
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos(os.path.join(carpeta,archivo), objeto, key, value)


objeto= "Device"
key= "Tipo General"
value= "Blade"


print("Las máquinas tipo Blade son:\n")
devolverArchivos("C:/Users/Hp/AppData/Roaming/Archi4/model-repository/archimate/model", objeto, key, value)

print("\n\n\n")
"""
a = "Fin"
input(a)
"""