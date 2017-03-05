__author__ = "moramaz"

from flask import Flask, request, Response
import subprocess

app = Flask("Practica2")

class NodoSimple:
	def __init__(self, dato, siguiente):
		self.dato = dato
		self.siguiente = siguiente

class ListaSimple:
	def __init__(self):
		self.Inicio = None
		self.Tamano = 0

	def Agregar(self, dato, posicion):
		if self.Tamano == 0:
			self.Inicio = NodoSimple(dato, None)
		else:
			Nuevo = None
			if posicion == -1:
				Nuevo = self.Inicio
				while(Nuevo.siguiente != None):
					Nuevo = Nuevo.siguiente
				Nuevo.siguiente = NodoSimple(dato, None)
			elif posicion == 0:
				Nuevo = NodoSimple(dato, self.Inicio)
				self.Inicio = Nuevo
			else:
				EnIndice = self.Inicio
				Nuevo = NodoSimple(dato, None)
				i = 0
				while(i < posicion):
					EnIndice = EnIndice.siguiente
					i = i + 1
				Nuevo.siguiente = EnIndice.siguiente
				EnIndice.siguiente = Nuevo
		self.Tamano = self.Tamano + 1

	def Borrar(self, indice):
		if indice == 0:
			self.Inicio = self.Inicio.siguiente
		else:
			Actual = self.Inicio
			i = 0
			while(i < indice - 1):
				Actual = Actual.siguiente
				i = i + 1
			if i < self.Tamano - 1:
				Actual.siguiente = Actual.siguiente.siguiente
		self.Tamano = self.Tamano - 1

	def Buscar(self, dato):
		Auxiliar = self.Inicio
		i = 0
		while(i < self.Tamano - 1):
			if Auxiliar.dato == dato:
				return i
			Auxiliar = Auxiliar.siguiente
			i = i + 1
		return -1996

	def Graficar(self):
		Archivo = open('/home/moramaz/Escritorio/Lista_simple.dot', 'w')
<<<<<<< HEAD
		Grafo_dot = "digraph ListaSimple{\n\tnode [shape = box];\n\trankdir=LR\n\tlabel=\"Lista Simple\"\n\n"
=======
		Grafo_dot = "digraph ListaSimple{\nlabel = \"Lista Simple\"\n\n"
>>>>>>> origin/master
		if self.Tamano != 0:
			Auxiliar = self.Inicio
			Indice = 0
			while(Auxiliar != None):
				Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + Auxiliar.dato + "\"];\n"
				Auxiliar = Auxiliar.siguiente
				Indice = Indice + 1
			Grafo_dot += "\n"
			Auxiliar = self.Inicio
			Indice = 0
			while(Auxiliar.siguiente != None):
				Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + "[label = \"Siguiente\"];\n"
				Auxiliar = Auxiliar.siguiente
				Indice = Indice + 1
		Grafo_dot += "}"
		Archivo.write(Grafo_dot)
		Archivo.close()
		subprocess.call(['dot', '/home/moramaz/Escritorio/Lista_simple.dot', '-o', '/home/moramaz/Escritorio/Lista_simple.png', '-Tpng', '-Gcharset=utf8'])

class Cola:
	def __init__(self):
		self.Inicio = None
		self.Fin = None
		self.Tamano = 0

	def Queue(self, dato):
		if self.Tamano == 0:
			self.Inicio = NodoSimple(dato, None)
			self.Fin = self.Inicio
		else:
			self.Fin.siguiente = NodoSimple(dato, None)
			self.Fin = self.Fin.siguiente
		self.Tamano = self.Tamano + 1

	def Dequeue(self):
		if self.Tamano != 0:
			Cabeza = self.Inicio
			self.Inicio = self.Inicio.siguiente
			self.Tamano = self.Tamano - 1
			return Cabeza.dato
		return -1996

	def Graficar(self):
		Archivo = open('/home/moramaz/Escritorio/Cola.dot', 'w')
<<<<<<< HEAD
		Grafo_dot = "digraph Cola{\n\tnode [shape = box];\n\tlabel=\"Cola\""
=======
		Grafo_dot = "digraph Cola{\n label = \"Cola\""
>>>>>>> origin/master
		if self.Tamano != 0:
			Auxiliar = self.Inicio
			Indice = 0
			while(Auxiliar != None):
				Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + str(Auxiliar.dato) + "\"];\n"
				Auxiliar = Auxiliar.siguiente
				Indice = Indice + 1
			Grafo_dot += "\n"
			Auxiliar = self.Inicio
			Indice = 0
			while(Auxiliar.siguiente != None):
				Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + "[label = \"Siguiente\"];\n"
				Auxiliar = Auxiliar.siguiente
				Indice = Indice + 1
		Grafo_dot += "}"
		Archivo.write(Grafo_dot)
		Archivo.close()
		subprocess.call(['dot', '/home/moramaz/Escritorio/Cola.dot', '-o', '/home/moramaz/Escritorio/Cola.png', '-Tpng', '-Gcharset=utf8'])

class Pila:
	def __init__(self):
		self.Inicio = None
		self.Tamano = 0

	def Push(self, dato):
		if self.Tamano == 0:
			self.Inicio = NodoSimple(dato, None)
		else:
			self.Inicio = NodoSimple(dato, self.Inicio)
		self.Tamano = self.Tamano + 1

	def Pop(self):
		if self.Tamano != 0:
			Cabeza = self.Inicio
			self.Inicio = self.Inicio.siguiente
			self.Tamano = self.Tamano - 1
			return Cabeza.dato
		return -1996

	def Graficar(self):
		Archivo = open('/home/moramaz/Escritorio/Pila.dot', 'w')
<<<<<<< HEAD
		Grafo_dot = "digraph Pila{\n\tnode [shape = box];\n\tlabel=\"Pila\""
=======
		Grafo_dot = "digraph Pila{\n label = \"Pila\""
>>>>>>> origin/master
		if self.Tamano != 0:
			Auxiliar = self.Inicio
			Indice = 0
			while(Auxiliar != None):
				Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + str(Auxiliar.dato) + "\"];\n"
				Auxiliar = Auxiliar.siguiente
				Indice = Indice + 1
			Grafo_dot += "\n"
			Auxiliar = self.Inicio
			Indice = 0
			while(Auxiliar.siguiente != None):
				Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + "[label = \"Siguiente\"];\n"
				Auxiliar = Auxiliar.siguiente
				Indice = Indice + 1
		Grafo_dot += "}"
		Archivo.write(Grafo_dot)
		Archivo.close()
		subprocess.call(['dot', '/home/moramaz/Escritorio/Pila.dot', '-o', '/home/moramaz/Escritorio/Pila.png', '-Tpng', '-Gcharset=utf8'])

class NodoMatriz:
<<<<<<< HEAD
	def __init__(self, dato):
		self.dato = dato
		self.id = None
		self.inicial = None
		self.dominio = None
		self.arriba = None
		self.abajo = None
		self.derecha = None
		self.izquierda = None
		self.adelante = None
		self.atras = None
=======
	def __init__(self, dato, adelante, atras):
		self.dato = dato				#String
		self.adelante = adelante		#NodoMatriz
		self.atras = atras				#NodoMatriz

class Profundidad:
	def __init__ (self):
		self.inicio = None				#NodoMatriz
		self.fin = None					#NodoMatriz
		self.arriba = None				#Profundidad
		self.abajo = None				#Profundidad
		self.derecha = None				#Profundidad
		self.izquierda = None			#Profundidad
		self.tamano = 0

	def Insertar(self, dato, esNodo):
		if esNodo:
			if tamano == 0:
				inicio = dato
				fin = inicio
			else:
				dato.adelante = fin
				fin.atras = dato
				fin = fin.atras
		else:
			if tamano == 0:
				inicio = NodoMatriz(dato, None, None)
				fin = inicio
			else:
				fin.atras = NodoMatriz(dato, fin, None)
				fin = fin.atras
		tamano = tamano + 1
		return fin

class NodoCabecera:
	def __init__ (self, encabezado, siguiente, anterior):
		self.encabezado = encabezado	#String
		self.primera = None				#Profundidad
		self.siguiente = siguiente		#NodoCabecera
		self.anterior = anterior		#NodoCabecera

class Cabecera:
	def __init__ (self):
		self.inicio = None				#NodoCabecera

	def Existe(self, dato):
		auxiliar = inicio
		while(auxiliar.siguiente != None):
			if auxiliar.encabezado == dato:
				return True
			auxiliar = auxiliar.siguiente
		return False

	def Obtener(self, dato):
		if inicio.encabezado == dato:
			return inicio
		auxiliar = inicio
		while(auxiliar.siguiente != None):
			if auxiliar.encabezado == dato:
				return auxiliar
			auxiliar = auxiliar.siguiente
		return None

	def Insertar(self, dato):
		auxiliar = NodoCabecera(dato, None, None)
		if inicio == None:
			inicio = auxiliar
		else:
			if(Existe(dato)):
				auxiliar = Obtener(dato)
			else:
				if dato.lower() < inicio.encabezado.lower():
					inicio.anterior = auxiliar
					auxiliar.siguiente = inicio
					inicio = auxiliar
				else:
					actual = inicio
					while(actual.encabezado.lower() < dato.lower()):
						actual = actual.siguiente
					auxiliar.anterior = actual.anterior
					actual.anterior.siguiente = auxiliar
					actual.anterior = auxiliar
					auxiliar.siguiente = actual
		return auxiliar
>>>>>>> origin/master

class Matriz:
	def __init__(self):
		self.inicio = NodoMatriz("Matriz")
		self.inicio.id = 0
		self.id = 1

	def __DominioExiste(self, dominio):
		if self.inicio.derecha == None:
			return False
		auxiliar = self.inicio.derecha
		while auxiliar != None:
			if auxiliar.dato == dominio:
				return True
			auxiliar = auxiliar.derecha
		return False

	def __InicialExiste(self, inicial):
		if self.inicio.abajo == None:
			return False
		auxiliar = self.inicio.abajo
		while auxiliar != None:
			if auxiliar.dato == inicial:
				return True
			auxiliar = auxiliar.abajo
		return False

	def Insertar(self, inicial, dominio, dato):
		NodoFila = NodoMatriz(inicial)
		NodoColumna = NodoMatriz(dominio)
		NodoDato = NodoMatriz(dato)
		NodoDato.id = self.id
		self.id += 1
		if self.inicio.abajo == None:
			self.inicio.abajo = NodoFila
			NodoFila.id = self.id
			self.id += 1
		elif self.inicio.abajo.dato.lower() > inicial.lower():
			NodoFila.abajo = self.inicio.abajo
			self.inicio.abajo.arriba = NodoFila
			self.inicio.abajo = NodoFila
			NodoFila.id = self.id
			self.id += 1
		else:
			auxiliar = self.inicio.abajo
			while auxiliar != None:
				if auxiliar.dato.lower() < inicial.lower() and auxiliar.abajo == None:
					auxiliar.abajo = NodoFila
					NodoFila.arriba = auxiliar
					NodoFila.id = self.id
					self.id += 1
					break
				elif auxiliar.dato.lower() < inicial.lower():
					auxiliar = auxiliar.abajo
				elif auxiliar.dato.lower() == inicial.lower():
					NodoFila = auxiliar
					break
				else:
					NodoFila.arriba = auxiliar.arriba
					auxiliar.arriba.abajo = NodoFila
					NodoFila.abajo = auxiliar
					auxiliar.arriba = NodoFila
					NodoFila.id = self.id
					self.id += 1
					break
		if self.inicio.derecha == None:
			self.inicio.derecha = NodoColumna
			NodoColumna.id = self.id
			self.id += 1
		elif self.inicio.derecha.dato.lower() > dominio.lower():
			NodoColumna.derecha = self.inicio.derecha
			self.inicio.derecha.izquierda = NodoColumna
			self.inicio.derecha = NodoColumna
			NodoColumna.id = self.id
			self.id += 1
		else:
			auxiliar = self.inicio.derecha
			while auxiliar != None:
				if auxiliar.dato.lower() < dominio.lower() and auxiliar.derecha == None:
					auxiliar.derecha = NodoColumna
					NodoColumna.izquierda = auxiliar
					NodoColumna.id = self.id
					self.id += 1
					break
				elif auxiliar.dato.lower() < dominio.lower():
					auxiliar = auxiliar.derecha
				elif auxiliar.dato.lower() == dominio.lower():
					NodoColumna = auxiliar
					break
				else:
					NodoColumna.izquierda = auxiliar.izquierda
					auxiliar.izquierda.derecha = NodoColumna
					NodoColumna.derecha = auxiliar
					auxiliar.izquierda = NodoColumna
					NodoColumna.id = self.id
					self.id += 1
					break
		NodoDato.inicial = inicial
		NodoDato.dominio = dominio
		if NodoColumna.abajo == None:
			NodoColumna.abajo = NodoDato
			NodoDato.arriba = NodoColumna
		elif NodoColumna.abajo.inicial.lower() > inicial.lower():
			NodoDato.abajo = NodoColumna.abajo
			NodoColumna.abajo.arriba = NodoDato
			NodoDato.arriba = NodoColumna
			NodoColumna.abajo = NodoDato
		else:
			auxiliar = NodoColumna.abajo
			while auxiliar != None:
				if auxiliar.inicial.lower() == inicial.lower():
					while auxiliar != None:
						if auxiliar.atras == None:
							auxiliar.atras = NodoDato
							NodoDato.adelante = auxiliar
							break
						auxiliar = auxiliar.atras
					break
				elif auxiliar.abajo == None and auxiliar.dato.lower() < NodoDato.dato.lower():
					auxiliar.abajo = NodoDato
					NodoDato.arriba = auxiliar
					break
				elif auxiliar.dato.lower() < NodoDato.dato.lower():
					auxiliar = auxiliar.abajo
				else:
					NodoDato.arriba = auxiliar.arriba
					auxiliar.arriba.abajo = NodoDato
					NodoDato.abajo = auxiliar
					auxiliar.arriba = NodoDato
					break
		if NodoFila.derecha == None:
			NodoFila.derecha = NodoDato
			NodoDato.izquierda = NodoFila
		elif NodoFila.derecha.inicial.lower() > inicial.lower():
			NodoDato.derecha = NodoFila.derecha
			NodoFila.derecha.izquierda = NodoDato
			NodoDato.izquierda = NodoFila
			NodoFila.derecha = NodoDato
		else:
			auxiliar = NodoFila.derecha
			while auxiliar != None:
				if NodoDato.adelante != None or NodoDato.atras != None:
					break
				elif auxiliar.derecha == None and auxiliar.dominio.lower() < NodoDato.dominio.lower():
					auxiliar.derecha = NodoDato
					NodoDato.izquierda = auxiliar
					break
				elif auxiliar.dominio.lower() < NodoDato.dominio.lower():
					auxiliar = auxiliar.derecha
				else:
					NodoDato.izquierda = auxiliar.izquierda
					auxiliar.izquierda.derecha = NodoDato
					NodoDato.derecha = auxiliar
					auxiliar.izquierda = NodoDato
					break

<<<<<<< HEAD
	def Graficar(self):
		Grafo_dot = "digraph Matriz{\n\trankdir=UD;\n\tnode [shape = box];\n\tlabel = \"Matriz\"" 
		paraAbajo = self.inicio
		paraDerecha = paraAbajo.derecha
		paraAtras = paraDerecha.atras
		y = 0
		while paraAbajo != None:
			if y == 0:
				Grafo_dot += "\n\t{\n\t\trank=min;"
				Grafo_dot += "\n\t\tNode" + str(paraAbajo.id) + " [label = \"" + paraAbajo.dato + "\", rankdir = LR]"
			elif paraAbajo.abajo == None:
				Grafo_dot += "\n\t{\n\t\trank=max;"
				Grafo_dot += "\n\t\tNode" + str(paraAbajo.id) + " [label = \"" + paraAbajo.dato + "\"]"
			else:	
				Grafo_dot += "\n\t{\n\t\trank=same;"
				Grafo_dot += "\n\t\tNode" + str(paraAbajo.id) + " [label = \"" + paraAbajo.dato + "\"]"
			while paraDerecha != None:
				if y == 0:
					Grafo_dot += "\n\t\tNode" + str(paraDerecha.id) + " [label = \"" + paraDerecha.dato + "\", rankdir = LR]"
				else:
					Grafo_dot += "\n\t\tNode" + str(paraDerecha.id) + " [label = \"" + paraDerecha.dato + "\"]"
				paraDerecha = paraDerecha.derecha
			Grafo_dot += "\n\t}"
			y += 1
			paraAbajo = paraAbajo.abajo
			if paraAbajo != None:
				paraDerecha = paraAbajo.derecha
		Grafo_dot += "\n\n"
		paraAbajo = self.inicio
		paraDerecha = paraAbajo.derecha
		paraAtras = paraDerecha.atras
		y = 0
		while paraAbajo != None:
			while paraDerecha != None:
				while paraAtras != None:
					Grafo_dot += "\n\tNode" + str(paraAtras.id) + " [label = \"" + paraAtras.dato + "\"]"
					paraAtras = paraAtras.atras
				paraDerecha = paraDerecha.derecha
				if paraDerecha != None:
					paraAtras = paraDerecha.atras
			y += 1
			paraAbajo = paraAbajo.abajo
			if paraAbajo != None:
				paraDerecha = paraAbajo.derecha
				paraAtras = paraDerecha.atras
		Grafo_dot += "\n\n"
		paraAbajo = self.inicio
		paraDerecha = paraAbajo.derecha
		paraAtras = paraDerecha.atras
		y = 0
		while paraAbajo != None:
			if paraAbajo.abajo != None:
				Grafo_dot += "\n\tNode" + str(paraAbajo.id) + " -> Node" + str(paraAbajo.abajo.id) + ";"
			if paraAbajo.arriba != None:
				Grafo_dot += "\n\tNode" + str(paraAbajo.id) + " -> Node" + str(paraAbajo.arriba.id) + ";"
			if paraAbajo.derecha != None:
				Grafo_dot += "\n\tNode" + str(paraAbajo.id) + " -> Node" + str(paraAbajo.derecha.id) + ";"
			if paraAbajo.izquierda != None:
				Grafo_dot += "\n\tNode" + str(paraAbajo.id) + " -> Node" + str(paraAbajo.izquierda.id) + ";"
			while paraDerecha != None:
				if paraDerecha.abajo != None:
					Grafo_dot += "\n\tNode" + str(paraDerecha.id) + " -> Node" + str(paraDerecha.abajo.id) + ";"
				if paraDerecha.arriba != None:
					Grafo_dot += "\n\tNode" + str(paraDerecha.id) + " -> Node" + str(paraDerecha.arriba.id) + ";"
				if paraDerecha.derecha != None:
					Grafo_dot += "\n\tNode" + str(paraDerecha.id) + " -> Node" + str(paraDerecha.derecha.id) + ";"
				if paraDerecha.izquierda != None:
					Grafo_dot += "\n\tNode" + str(paraDerecha.id) + " -> Node" + str(paraDerecha.izquierda.id) + ";"
				if paraDerecha.atras != None:
					Grafo_dot += "\n\tNode" + str(paraDerecha.id) + " -> Node" + str(paraDerecha.atras.id) + ";"
				if paraDerecha.adelante != None:
					Grafo_dot += "\n\tNode" + str(paraDerecha.id) + " -> Node" + str(paraDerecha.adelante.id) + ";"
				while paraAtras != None:
					if paraAtras.atras != None:
						Grafo_dot += "\n\tNode" + str(paraAtras.id) + " -> Node" + str(paraAtras.atras.id) + ";"
					if paraAtras.adelante != None:
						Grafo_dot += "\n\tNode" + str(paraAtras.id)  + " -> Node" + str(paraAtras.adelante.id) + ";"
					paraAtras = paraAtras.atras
				paraDerecha = paraDerecha.derecha
				if paraDerecha != None:
					paraAtras = paraDerecha.abajo
			y += 1
			paraAbajo = paraAbajo.abajo
			if paraAbajo != None:
				paraDerecha = paraAbajo.derecha
				paraAtras = paraDerecha.atras
		Grafo_dot += "\n}" 
		Archivo = open('/home/moramaz/Escritorio/Matriz.dot', 'w') 
		Archivo.write(Grafo_dot) 
		Archivo.close() 
		subprocess.call(['dot', '/home/moramaz/Escritorio/Matriz.dot', '-o', '/home/moramaz/Escritorio/Matriz.png', '-Tpng', '-Gcharset=utf8']) 
=======
	def Agregar(self, inicial, dominio, nombre):
		nodoFila = filas.Insertar(inicial)
		nodoColumna = columnas.Insertar(dominio)
		nodoDato = None
		if filas.primera == None:
			filas.primera = Profundidad()
			nodoDato = filas.primera.Insertar(nombre, False)
			if columnas.primera == None:
				columnas.primera = Profundidad()
				columnas.primera.Insertar(nodoDato, True)
			else:
				primerita = Profundidad()
				if nombre.lower() < columnas.primera.inicio.dato.lower():
					primerita.Insertar(nodoDato, True)
					primerita.abajo = columnas.primera
					columnas.primera = primerita
				else:
					actual = columnas.primera
					while(actual.inicio.dato.lower() < nombre.lower()):
						actual = actual.abajo


>>>>>>> origin/master

List = ListaSimple()
Queue = Cola()
Stak = Pila()
Matrix = Matriz()

<<<<<<< HEAD
@app.route('/')
def init():
	return ""
=======

@app.route('/')
def init():
	return "esto es una prueba :v"
>>>>>>> origin/master

#INSERTAR
@app.route('/list_add', methods=['POST'])
def list_add():
	dato = str(request.form['dato'])
	List.Agregar(str(dato), -1)
	List.Graficar()
<<<<<<< HEAD
	return "s"

@app.route('/matrix_add', methods=['POST'])
def matrix_add():
	inicial = str(request.form['inicial'])
	dominio = str(request.form['dominio'])
	nombre = str(request.form['nombre'])
	Matrix.Insertar(str(inicial), str(dominio), str(nombre))
	Matrix.Graficar()
	return ""

=======
	return ""

@app.route('/matrix_add', methods=['POST'])
def matrix_add():
	inicial = str(request.form['inicial'])
	dominio = str(request.form['dominio'])
	nombre = str(request.form['nombre'])
	Matrix.Agregar(str(inicial), str(dominio), str(nombre))
	print "se agrego " + str(nombre) + "@" + str(dominio) + " a la matriz."

>>>>>>> origin/master
@app.route('/queue_add', methods=['POST'])
def queue_add():
	dato = int(request.form['dato'])
	Queue.Queue(int(dato))
	Queue.Graficar()
	return ""

@app.route('/stak_add', methods=['POST'])
def stak_add():
	dato = int(request.form['dato'])
	Stak.Push(int(dato))
	Stak.Graficar()
	return ""

#ELIMINAR
@app.route('/list_remove', methods=['POST'])
def list_remove():
	indice = int(request.form['indice'])
	List.Borrar(int(indice))
	List.Graficar()
	return ""

@app.route('/matrix_remove', methods=['POST'])
def matrix_remove():
	print ":3"

@app.route('/queue_remove', methods=['POST'])
def queue_remove():
	dato = Queue.Dequeue()
	Queue.Graficar()
	return str(dato)

@app.route('/stak_remove', methods=['POST'])
def stak_remove():
	dato = Stak.Pop()
	Stak.Graficar()
	return str(dato)

#BUSCAR
@app.route('/list_search', methods=['POST'])
def list_search():
	dato = str(request.form['dato'])
	return str(List.Buscar(dato))

@app.route('/matrix_search_letter', methods=['POST'])
def matrix_search_letter():
	return ":3"

@app.route('/matrix_search_domain', methods=['POST'])
def matrix_search_domain():
	return ":3"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')