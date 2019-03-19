#! python3
import sys, os, fileinput
from xml.dom import minidom

def cuales_son(archivos):

	read = open(archivos)
	dato = read.readline()
	
	if dato.startswith('<archimate:BusinessService'):

		
		doc = minidom.parse(archivos)
		itemlist = doc.getElementsByTagName("properties")
		codigo = nombre = descripcion = tipo = ""
		for n in itemlist:
		    
		    key_n = n.attributes["key"].value

		    try:
		    	value_n = n.attributes["value"].value
		    except:
		    	value_n = ""

		    
		    #print("\n\nkey_n   =" + key_n)
		    #print("\nvalue_n =" + value_n)
		    

		    if key_n == "Código CRUE":
		    	codigo = value_n
		    if key_n == "Nombre del Servicio":
		    	nombre = value_n
		    if key_n == "Descripción Servicio":
		    	descripcion = value_n
		    if key_n == "Tipo":
		    	tipo = value_n

		if(tipo == "Servicio"):
			write.write(codigo + ";" + nombre + ";" + descripcion + "\n")

	read.close()
	


def devolverArchivos(carpeta):

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			cuales_son(os.path.join(carpeta,archivo))
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos(os.path.join(carpeta,archivo))




write = open ("./generado.csv", "w")

write.write("CATÁLOGO DE SERVICIOS TIC DE CRUE V3.0;;;;;;;\n")
write.write("Cód. CRUE;Nombre del Servicio;Descripción del Servicio\n")



if write:
	print("Archivo .csv generado.\n")



#Ruta Gabriel
devolverArchivos("C:/Users/Hp/AppData/Roaming/Archi4/model-repository/crue-tic-ae-pre/model")

#Ruta Pablo
#devolverArchivos("C:/Users/Usuario/AppData/Roaming/Archi4/model-repository/archimate/model", objeto, key, value)
write.close()
