#! python3
import sys, os, fileinput
#sys.stdout.write("hello from Python %s\n" % (sys.version,))
"""
f = open("Prueba-device.xml")

linea = f.readline()
while linea != "" and linea != "      key=\"Nombre DNS\"\n" :
    linea = f.readline()
nombre = f.readline()

linea = f.readline()
while linea != "" and linea != "      key=\"Tipo General\"\n":
    linea = f.readline()


if f.readline() == "      value=\"Servidor Stanalone, Blade, cabina de almacenamiento, otro\"/>\n":
	print(nombre)

"""
"""
linea = f.readline()
while linea !=  "":
    linea = f.readline()
    print(linea,end="")
"""
#f.close()
def cuales_son(archivos, objeto, key, value):
	"""
	archivos_y_carpetas = os.listdir(".")
	archivos = []
	print(archivos_y_carpetas)
	for i in archivos_y_carpetas:
	    if os.path.isfile(i):
	    	archivos += [i]
	

	print("\n\n\n")
	print(archivos)
	print("\n\n\n")
"""
	
	

	ini=0
	a=0 
	no=0
	for linea in fileinput.input(archivos):
		#sys.stdout.write(linea)
		
		if ini==0:
			primera = linea
			primera = primera.replace("<archimate:", "")
			if primera != objeto + "\n":
				no=1
			ini=1
		if a==1 and no==0:
			nombre = linea
			a=0
		if linea == "      key=\"Nombre DNS\"\n" and no==0:
			a=1
		if a==2 and no==0:
			if linea == "      value=\""+ value + "\"/>\n":
				nombre = nombre.replace("      value=\"", "")
				nombre = nombre.replace("\"/>", "")
				sys.stdout.write(nombre)
				nombre = ""
			a=0
		if linea == "      key=\"" +key + "\"\n" and no==0:
			a=2



def devolverArchivos(carpeta, objeto, key, value):

	for archivo in os.listdir(carpeta):

		#print(os.path.join(carpeta,archivo))
		if os.path.isfile(os.path.join(carpeta,archivo)):
			cuales_son(os.path.join(carpeta,archivo), objeto, key, value)

		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos(os.path.join(carpeta,archivo), objeto, key, value)

 

#archivos_y_carpetas=devolverArchivos(".")



objeto= "Device"
key= "Tipo General"
value= "Blade"


print("Las máquinas tipo Blade son:\n")
devolverArchivos("C:/Users/Hp/AppData/Roaming/Archi4/model-repository/archimate/model", objeto, key, value)











print("\n\n\n")
a = "Fin"
input(a)
