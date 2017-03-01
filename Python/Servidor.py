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
		Grafo_dot = "digraph ListaSimple{\nlabel = \"Lista Simple\"\n\n"
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
		Grafo_dot = "digraph Cola{\n label = \"Cola\""
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
		Grafo_dot = "digraph Pila{\n label = \"Pila\""
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

class Matriz:
	def __init__(self):
		self.columnas = None			#Cabecera
		self.filas = None				#Cabecera

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



List = ListaSimple()
Queue = Cola()
Stak = Pila()
Matrix = Matriz()


@app.route('/')
def init():
	return "esto es una prueba :v"

#INSERTAR
@app.route('/list_add', methods=['POST'])
def list_add():
	dato = str(request.form['dato'])
	List.Agregar(str(dato), -1)
	List.Graficar()
	return ""

@app.route('/matrix_add', methods=['POST'])
def matrix_add():
	inicial = str(request.form['inicial'])
	dominio = str(request.form['dominio'])
	nombre = str(request.form['nombre'])
	Matrix.Agregar(str(inicial), str(dominio), str(nombre))
	print "se agrego " + str(nombre) + "@" + str(dominio) + " a la matriz."

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