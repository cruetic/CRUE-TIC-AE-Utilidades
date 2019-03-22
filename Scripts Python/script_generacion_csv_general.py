#! python3
import sys, os, fileinput
from xml.dom import minidom

def cuales_son(archivos):

	read = open(archivos)
	dato = read.readline()
	
	if dato.startswith('<archimate:' + parametro[1]):

		
		doc = minidom.parse(archivos)
		itemlist = doc.getElementsByTagName("properties")
		
				
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

		    cont = 0
		    for i in propiedades:
		    	if key_n == i:

		    		valor_propiedad[cont] = value_n
		    	cont += 1

		    

		    if sin_key == 1:
		     	print("El Objeto ")
		     	for i in valor_propiedad:
		     		print(i)
		     	print(" cuenta con una propiedad sin nombre definido.\n")


		cont = 0   	
		for i in valor_propiedad:
			if i == "":
				cont += 1

		if cont < len(valor_propiedad):
			for i in valor_propiedad:
				write.write(i + ";")
			write.write("\n")

			cont2 = 0
			salto = 0
			for i in valor_propiedad:
				if(i == ""):
					print("El objeto")
					for i in valor_propiedad:
						print(i,end=", ")
					print("\nno cuenta con " + propiedades[cont2] + " definido.")
					salto=1
				cont2 += 1
			if salto ==1:
				print("\n")	
	
	read.close()


def get_propiedades(archivos):

	read = open(archivos)
	dato = read.readline()
	
	if dato.startswith('<archimate:' + parametro[1]):

		
		doc = minidom.parse(archivos)
		itemlist = doc.getElementsByTagName("properties")
		
		for n in itemlist:
		   
		    try:
		    	key_n = n.attributes["key"].value
		    except:
		    	key_n = ""
		    			   		    
		    if not key_n in propiedades and key_n != "":
		    	propiedades.append(key_n)
		    	
	read.close()
	


def devolverArchivos(carpeta):

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			cuales_son(os.path.join(carpeta,archivo))
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos(os.path.join(carpeta,archivo))

def devolverArchivos_previo(carpeta):

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			get_propiedades(os.path.join(carpeta,archivo))
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos_previo(os.path.join(carpeta,archivo))





##### main

parametro = sys.argv
print(parametro[1])
write = open ("./Lista_" + parametro[1] + ".csv", "w")

write.write(parametro[1] + ";;;;;;;\n")

propiedades = []
valor_propiedad = []

devolverArchivos_previo("C:/Users/Hp/AppData/Roaming/Archi4/model-repository/archimate/model")

print(propiedades)

for i in propiedades:
	write.write(i + ";")
	valor_propiedad.append("")
	print(valor_propiedad)
write.write("\n")


print("1")

print("\n\n\n")


#Ruta Gabriel
devolverArchivos("C:/Users/Hp/AppData/Roaming/Archi4/model-repository/archimate/model")

#Ruta Pablo
#devolverArchivos("C:/Users/Usuario/AppData/Roaming/Archi4/model-repository/archimate/model", objeto, key, value)

if write:
	print("\n---------------------------Archivo Lista_" + parametro[1] + ".csv generado.---------------------------\n\n\n")

write.close()
