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
		    sin_key = 0
		    try:
		    	key_n = n.attributes["key"].value
		    except:
		    	key_n = ""
		    	sin_key = 1

		    try:
		    	value_n = n.attributes["value"].value
		    except:
		    	value_n = ""


		    
		    # print("\n\nkey_n   =" + key_n)
		    # print("\nvalue_n =" + value_n)
		    

		    if key_n == "Código CRUE":
		    	codigo = value_n
		    if key_n == "Nombre del Servicio":
		    	nombre = value_n
		    if key_n == "Descripción Servicio":
		    	descripcion = value_n
		    if key_n == "Tipo":
		    	tipo = value_n

		    if sin_key == 1:
		    	print("El Objeto " + codigo + " " + nombre)
		    	if descripcion != "":
		    		print(" con Descripción: \"" + descripcion + "\"")
		    	print(" cuenta con una propiedad sin nombre definido.\n")

		if(tipo == "Servicio"):
			write.write(codigo + ";" + nombre + ";" + descripcion + "\n")
			if(codigo == ""):
				print("El Objeto " + nombre + " no tiene código definido")
			if(nombre == ""):
				print("El Objeto " + codigo + " no tiene nombre definido")
			if(descripcion == ""):
				print("El Objeto " + codigo + ", " + nombre + ", no tiene Descripción definida")
		else:
			if(codigo != "" or nombre != "" or descripcion != ""):
				print("El Objeto " + codigo + " " + nombre + " cumple con las características de Servicio, pero no tiene atributo Tipo.\n")

	read.close()
	


def devolverArchivos(carpeta):

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			cuales_son(os.path.join(carpeta,archivo))
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos(os.path.join(carpeta,archivo))




write = open ("./Servicios_CRUETIC.csv", "w")

write.write("CATÁLOGO DE SERVICIOS TIC DE CRUE V3.0;;;;;;;\n")
write.write("Cód. CRUE;Nombre del Servicio;Descripción del Servicio\n")







#Ruta Gabriel
devolverArchivos("C:/Users/Hp/AppData/Roaming/Archi4/model-repository/crue-tic-ae-pre/model")

#Ruta Pablo
#devolverArchivos("C:/Users/Usuario/AppData/Roaming/Archi4/model-repository/archimate/model", objeto, key, value)

if write:
	print("\n---------------------------Archivo Servicios_CRUETIC.csv generado.---------------------------\n")

write.close()
