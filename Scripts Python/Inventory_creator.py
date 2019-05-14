#! python3
import sys, os, fileinput, codecs, datetime, platform, win32api, math
from xml.dom import minidom


def cuales_son(archivo):

	read = open(archivo)
	dato = read.readline()
	
	if dato.startswith('<archimate:ArchimateDiagramModel'):

		
		
		try:
			doc = minidom.parse(archivo)
			itemlist = doc.getElementsByTagName("properties")
			tipo = ""
			
			for n in itemlist:
			    try:
			    	key_n = n.attributes["key"].value
			    except:
			    	key_n = ""

			    try:
			    	value_n = n.attributes["value"].value
			    except:
			    	value_n = ""

			    if key_n == "Tipo":
			    	tipo = value_n

			
			if tipo == "Dinámica":
				analizar_propiedades(archivo)
		except:
			x=0



	read.close()

def niveles(i):
        switcher={
                "Strategy":'strategy',
                "Business":'business',
                "Technology & Physical":'technology',
                "Motivation":'motivation',
            }
        return switcher.get(i,i)



def analizar_propiedades(archivo):

	read = open(archivo)
	dato = read.readline()
	
	
		
	doc = minidom.parse(archivo)
	itemlist = doc.getElementsByTagName("properties")
	nivel = objeto = agrupacion = ""
	
	for n in itemlist:
	    
	    try:
	    	key_n = n.attributes["key"].value
	    except:
	    	key_n = ""
	 
	    try:
	    	value_n = n.attributes["value"].value
	    except:
	    	value_n = ""

	    if key_n == "Nivel":
	    	nivel = value_n
	    if key_n == "Objeto":
	    	objeto = value_n.replace(" ", "") 
	    if key_n == "Agrupación":
	    	agrupacion = value_n
	x = datetime.datetime.now()
	nombre_archivo = "./../../Archimate/model/diagrams/ArchimateDiagramModel_Inventario_" + objeto + "_" + agrupacion + str(x.day) + "-" + str(x.month) + "-" + str(x.year) + "_" + str(x.hour) + "·" + str(x.minute) + "·" + str(x.second) + ".xml"
	write = codecs.open (nombre_archivo, "w", "utf-8")

	x_grupo = 0
	y_grupo = 100

	x_objeto = 60
	y_objeto = 0

	
	ruta = "./../../Archimate/model/" + niveles(nivel)
	propiedades.clear()
	if agrupacion != "":
		devolverArchivos_busquedapropiedades(ruta, objeto, agrupacion)
	else:
		propiedades.append("(vacio)")
		agrupacion = "(vacio)"
	
	
	read2 = codecs.open(archivo, "r", "utf-8")

	
	itemlist2 = doc.getElementsByTagName("archimate:ArchimateDiagramModel")
	nombre_vista = ""
	for n in itemlist2:

		nombre_vista = n.attributes["name"].value
		
		print(archivo)
		print(objeto)
	
	linea = read2.readline()
	while linea.find("children") == -1 and linea.find("properties") == -1:				
			
		if linea.find("name") != -1:
			linea = "    name=\"" + nombre_vista + "\"\n"
		write.write(linea)
		linea = read2.readline()
	num_grupo = 1
	altura_grupo = latitud_grupo = 0
	for i in propiedades:
		ids.clear()
		devolverArchivos_obtenerobjetos(ruta, objeto, agrupacion, i)
		latitud_grupo = str(int(altura_grupo) + int(latitud_grupo) + 120)
		altura_grupo = str(48 * (math.ceil((len(ids)/5))+1) + (55 * math.ceil((len(ids)/5))))
		
		
		
		if len(ids)<=5:
			ancho_grupo = str((len(ids) * 120) + (x_objeto * (len(ids)+1)))
		else:
		 	ancho_grupo = str((5 * 120) + (x_objeto * (5+1)))
		write.write("  <children\n      xsi:type=\"archimate:DiagramModelGroup\"\n      id=\"grupo_" + objeto + agrupacion + i + "\"\n      name=\"" + i + "\"\n      textAlignment=\"1\">")
		write.write("\n    <bounds\n        x=\"200\"\n        y=\"" + latitud_grupo + "\"\n        width=\"" + ancho_grupo + "\"\n        height=\"" + altura_grupo + "\"/>\n")
		num_grupo += math.ceil((len(ids)/5))
		num_objetos = 1
		altura = str(48)
		#print(ids)
		for j in ids:
			
			ancho = str((x_objeto * num_objetos) + (120 * (num_objetos-1)))

			write.write("    <children\n        xsi:type=\"archimate:DiagramModelArchimateObject\"\n        id=\"id_" + objeto + j + "\">\n      <bounds\n          x=\"" + ancho + "\"\n          y=\"" + altura + "\"\n          width=\"120\"\n          height=\"55\"/>\n")
			write.write("      <archimateElement\n          xsi:type=\"archimate:" + objeto + "\"\n          href=\"" + j + "\"/>\n    </children>\n")

			num_objetos += 1
			if num_objetos == 6:
				num_objetos = 1
				altura = str(int(altura) + 103)

		
		write.write("  </children>\n")
		

	
	for n in itemlist:
	    write.write("  <properties\n")
	    try:
	    	key_n = n.attributes["key"].value
	    except:
	    	key_n = ""
	    
	    write.write("      key=\"" + key_n + "\"\n")	

	    try:
	    	value_n = n.attributes["value"].value
	    	value_n = value_n.replace("&", "&amp;")
	    except:
	    	value_n = ""
	    write.write("      value=\"" + value_n + "\"/>\n")	
	    
	write.write("</archimate:ArchimateDiagramModel>")

	print("\nNueva vista actualizada: " + nombre_vista + "\n")
	

	read.close()
	read2.close()
	write.close()


	write = codecs.open (archivo, "w", "utf-8")
	read = codecs.open(nombre_archivo, "r", "utf-8")

	for linea in read:

		write.write(linea)

	write.close()
	read.close()

	os.remove(nombre_archivo)



def definir_propiedades(archivo, objeto, agrupacion):

	read = open(archivo)
	dato = read.readline()
	
	if dato.startswith('<archimate:' + objeto):

		
		doc = minidom.parse(archivo)
		itemlist = doc.getElementsByTagName("properties")
		
		for n in itemlist:
		   
		    try:
		    	key_n = n.attributes["key"].value
		    except:
		    	key_n = "(vacio)"

		    try:
		    	value_n = n.attributes["value"].value
		    except:
		    	value_n = "(vacio)"
		    			   		    
		    if not value_n in propiedades and key_n == agrupacion and value_n != "":
		    	propiedades.append(value_n)
		    	
	read.close()


def obtener_objetos(archivo, objeto, agrupacion, grupo):

	read = open(archivo)
	dato = read.readline()

	if dato.startswith('<archimate:' + objeto):


		doc = minidom.parse(archivo)


		itemlist = doc.getElementsByTagName("archimate:" + objeto)
		identificador = ""
		for n in itemlist:

			identificador = n.attributes["id"].value



			

		itemlist = doc.getElementsByTagName("properties")
		if itemlist == [] and agrupacion == "(vacio)" and grupo == "(vacio)":
			ids.append(objeto + "_" + identificador + ".xml#" + identificador)
		
		for n in itemlist:

			try:
				key_n = n.attributes["key"].value
				
			except:
				key_n = "(vacio)"

			try:
				value_n = n.attributes["value"].value
			except:
				value_n = "(vacio)"

			if key_n == agrupacion and value_n == grupo:
				ids.append(objeto + "_" + identificador + ".xml#" + identificador)
				break
				
	read.close()


def devolverArchivos_obtenerobjetos(carpeta, objeto, agrupacion, grupo):

	try:
		index = carpeta.find('\\', 100)
		ini = carpeta[0:index]
		fin = carpeta[index:len(carpeta)]
		carpeta=win32api.GetShortPathName(win32api.GetShortPathName(ini) + fin)
	except:
		carpeta = carpeta

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			obtener_objetos(os.path.join(carpeta,archivo), objeto, agrupacion, grupo)
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos_obtenerobjetos(os.path.join(carpeta,archivo), objeto, agrupacion, grupo)


def devolverArchivos_busquedapropiedades(carpeta, objeto, agrupacion):

	try:
		index = carpeta.find('\\', 100)
		ini = carpeta[0:index]
		fin = carpeta[index:len(carpeta)]
		carpeta=win32api.GetShortPathName(win32api.GetShortPathName(ini) + fin)
	except:
		carpeta = carpeta

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			definir_propiedades(os.path.join(carpeta,archivo), objeto, agrupacion)
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos_busquedapropiedades(os.path.join(carpeta,archivo), objeto, agrupacion)



def devolverArchivos(carpeta):

	try:
		index = carpeta.find('\\', 100)
		ini = carpeta[0:index]
		fin = carpeta[index:len(carpeta)]
		carpeta=win32api.GetShortPathName(win32api.GetShortPathName(ini) + fin)
	except:
		carpeta = carpeta

	for archivo in os.listdir(carpeta):

		if os.path.isfile(os.path.join(carpeta,archivo)):
			cuales_son(os.path.join(carpeta,archivo))
			
		if os.path.isdir(os.path.join(carpeta,archivo)):

			devolverArchivos(os.path.join(carpeta,archivo))


def anadir(archivo):

	# print(archivo)
	read = open(archivo, encoding="utf8", errors='ignore')

	nombre_archivo = archivo + "temporal"
	# print(nombre_archivo)
	# print("antes")
	write = open(nombre_archivo, "w", encoding="utf-8")
	# print("despues")


	for linea in read:

		if linea.find("\r") == -1:
			linea.replace("\n", "\r\n")

		write.write(linea)

	write.close()
	read.close()
	
	read = open(nombre_archivo, encoding="utf8", errors='ignore')
	write = codecs.open(archivo, "w", "utf-8")

	for linea in read:

		write.write(linea)

	write.close()
	read.close()

	#os.remove(nombre_archivo)



def borrar(archivo):

	if archivo.find("temporal") != -1:
		os.remove(archivo)

def anadirsaltos(carpeta):

	

	try:
		index = carpeta.find('\\', 100)
		ini = carpeta[0:index]
		fin = carpeta[index:len(carpeta)]
		carpeta=win32api.GetShortPathName(win32api.GetShortPathName(ini) + fin)
	except:
		carpeta = carpeta

	if carpeta.find(".git") == -1:
		for archivo in os.listdir(carpeta):
			
			if os.path.isfile(os.path.join(carpeta,archivo)):
				anadir(os.path.join(carpeta,archivo))

			if os.path.isdir(os.path.join(carpeta,archivo)):
				anadirsaltos(os.path.join(carpeta,archivo))


def borrar_archivos(carpeta):

	try:
		index = carpeta.find('\\', 100)
		ini = carpeta[0:index]
		fin = carpeta[index:len(carpeta)]
		carpeta=win32api.GetShortPathName(win32api.GetShortPathName(ini) + fin)
	except:
		carpeta = carpeta

	if carpeta.find(".git") == -1:
		for archivo in os.listdir(carpeta):
			
			if os.path.isfile(os.path.join(carpeta,archivo)):
				borrar(os.path.join(carpeta,archivo))
								
			if os.path.isdir(os.path.join(carpeta,archivo)):
				borrar_archivos(os.path.join(carpeta,archivo))



######    main

if platform.system() == "Linux":

	
	returned = os.system("cd ./../.. && git clone https://github.com/alu0100888041/Archimate.git Archimate")
	if returned != 0:
		print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~El repositorio ya estaba clonado previamente.~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		os.system("cd ../../Archimate && git pull")

		


	print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~Repositorio actualizado~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	propiedades = []
	ids = []
	devolverArchivos("../../Archimate/model/diagrams")

	print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~Vistas actualizadas~~~~~~~~~~~~~~~~~~~~~~~~~\n")



		
	os.system("cd ../../Archimate && git add .")
	os.system("cd ../../Archimate && git commit -m \"Actualizando vistas Dinámicas desde Inventory_creator.py\"")
	os.system("cd ../../Archimate && git push origin master")

	print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~Repositorio subido a Github.~~~~~~~~~~~~~~~~~~~~~~~~~\n")

elif platform.system() == "Windows":
	returned = os.system("cd ./../.. & git clone git@github.com:alu0100888041/Archimate.git Archimate")
	if returned != 0:
		print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~El repositorio ya estaba clonado previamente.~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		os.system("cd ../../Archimate & git pull")

		


	print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~Repositorio actualizado~~~~~~~~~~~~~~~~~~~~~~~~~\n")


	ruta_absoluta = os.getcwd()
	ruta = "/../../Archimate/model"
	ruta_final = ruta_absoluta + ruta


	borrar_archivos(ruta_final)
	anadirsaltos(ruta_final)
	borrar_archivos(ruta_final)


	
	

	propiedades = []
	ids = []
	devolverArchivos("../../Archimate/model/diagrams")

	print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~Vistas actualizadas~~~~~~~~~~~~~~~~~~~~~~~~~\n")



		
	os.system("cd ../../Archimate & git add .")
	os.system("cd ../../Archimate & git commit -m \"Actualizando vistas Dinámicas desde Inventory_creator.py\"")
	os.system("cd ../../Archimate & git push origin master")

	print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~Repositorio subido a Github.~~~~~~~~~~~~~~~~~~~~~~~~~\n")
