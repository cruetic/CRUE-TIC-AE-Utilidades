#! python3
import sys, os, fileinput
from xml.dom import minidom

def cuales_son(archivos):

	read = open(archivos)
	dato = read.readline()
	
	if dato.startswith('<archimate:Device'):

		
		doc = minidom.parse(archivos)
		itemlist = doc.getElementsByTagName("properties")
		NombreDNS = So = T_Hardware = T_General = Servidor = Contendor = ""
		
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
		    

		    if key_n == "Nombre DNS":
		    	NombreDNS = value_n
		    if key_n == "SO":
		    	So = value_n
		    if key_n == "Tipo Hardware":
		    	T_Hardware = value_n
		    if key_n == "Tipo General":
		    	T_General = value_n
		    if key_n == "Servidor":
		    	Servidor = value_n
		    if key_n == "Contenedor":
		    	Contendor = value_n

		    if sin_key == 1:
		    	print("El Objeto " + NombreDNS + " cuenta con una propiedad sin nombre definido.\n")
		    	
		if not NombreDNS == So == T_Hardware == T_General == Servidor == Contendor == "":
			write.write(NombreDNS + ";" + So + ";" + T_Hardware + ";" + T_General + ";" + Servidor + ";" + Contendor + "\n")
			salto=0
			if(NombreDNS == ""):
				print("Existe un servidor sin nombre definido.")
				salto=1
			if(So == ""):
				print("El Servidor " + NombreDNS + " no tiene SO definido")
				salto=1
			if(T_Hardware == ""):
				print("El Servidor " + NombreDNS + " no tiene Tipo de Hardware definido")
				salto=1
			if(T_General == ""):
				print("El Servidor " + NombreDNS + " no tiene Tipo General definido")
				salto=1
			if salto ==1:
				print("\n")
		"""
		if(Servidor == ""):
			print("El Servidor " + NombreDNS + " no tiene Tipo_Servidor definido")
		if(Contendor == ""):
			print("El Servidor " + NombreDNS + " no tiene Tipo_Contendor definido")
		"""
	
	read.close()
	


def devolverArchivos(carpeta):

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			cuales_son(os.path.join(carpeta,archivo))
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos(os.path.join(carpeta,archivo))




write = open ("./Servidores.csv", "w")

write.write("SERVIDORES;;;;;;;\n")
write.write("Nombre DNS;SO;Tipo de Hardware;Tipo General;Servidor;Contendor\n")




print("\n\n\n")


#Ruta Gabriel
devolverArchivos("C:/Users/Hp/AppData/Roaming/Archi4/model-repository/archimate/model")

#Ruta Pablo
#devolverArchivos("C:/Users/Usuario/AppData/Roaming/Archi4/model-repository/archimate/model", objeto, key, value)

if write:
	print("\n---------------------------Archivo Servidores.csv generado.---------------------------\n\n\n")

write.close()
