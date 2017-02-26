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
		if Tamano == 0:
			Inicio = NodoSimple(dato, None)
		else:
			Nuevo = None
			if posicion == -1:
				Nuevo = Inicio
				while(Nuevo.siguiente != None):
					Nuevo = Nuevo.siguiente
				Nuevo.siguiente = NodoSimple(dato, None)
			elif posicion == 0:
				Nuevo = NodoSimple(dato, Inicio)
				Inicio = Nuevo
			else:
				EnIndice = Inicio
				Nuevo = NodoSimple(dato, None)
				i = 0
				while(i < posicion):
					EnIndice = EnIndice.siguiente
					i = i + 1
				Nuevo.siguiente = EnIndice.siguiente
				EnIndice.siguiente = Nuevo
		Tamano = Tamano + 1

	def Borrar(self, indice): 
		Actual = Inicio
		i = 0
		while(i < indice - 1):
			Actual = Actual.siguiente
			i = i + 1
		if i < Tamano - 1:
			Actual.siguiente = Actual.siguiente.siguiente

	def Buscar(self, dato):
		Auxiliar = Inicio
		i = 0
		while(i < Tamano - 1):
			if Auxiliar.dato == dato:
				return i
			Auxiliar = Auxiliar.siguiente
			i = i + 1
		return -1

	def Graficar(self):
		Archivo = open('Lista_simple.dot', 'w')
		Archivo.close()
		Archivo = open('Lista_simple.dot', 'a')
		Grafo_dot = "digraph ListaSimple{\n label = \"Lista Simple\""
		Auxiliar = Inicio
		Indice = 0
		while(Auxiliar != None):
			Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + Auxiliar.dato + "\"];\n"
			Auxiliar = Auxiliar.siguiente
			Indice = Indice + 1
		Grafo_dot += "\n"
		Auxiliar = Inicio
		Indice = 0
		while(Auxiliar.siguiente != None):
			Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + "[label = \"Siguiente\"];\n"
			Auxiliar = Auxiliar.siguiente
			Indice = Indice + 1
		Grafo_dot += "}"
		Archivo.close()
		subprocess.call(['dot', 'Lista_simple.dot', '-o', 'Lista_simple.png', '-Tpng', '-Gcharset=utf8'], shell = True)

	Graficar()

class Cola:
	def __init__(self):
		self.Inicio = None
		self.Fin = None
		self.Tamano = 0

	def Queue(self, dato):
		if Tamano == 0:
			Inicio = NodoSimple(dato, None)
			Fin = Inicio
		else:
			Fin.siguiente = NodoSimple(dato, None)
			Fin = Fin.siguiente
		Tamano = Tamano + 1

	def Dequeue(self):
		if Tamano != 0:
			Cabeza = Inicio
			Inicio = Inicio.siguiente
			Tamano = Tamano - 1
			return Cabeza.dato
		return -1996

	def Graficar(self):
		Archivo = open('Cola.dot', 'w')
		Archivo.close()
		Archivo = open('Cola.dot', 'a')
		Grafo_dot = "digraph Cola{\n label = \"Cola\""
		Auxiliar = Inicio
		Indice = 0
		while(Auxiliar != None):
			Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + Auxiliar.dato + "\"];\n"
			Auxiliar = Auxiliar.siguiente
			Indice = Indice + 1
		Grafo_dot += "\n"
		Auxiliar = Inicio
		Indice = 0
		while(Auxiliar.siguiente != None):
			Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + "[label = \"Siguiente\"];\n"
			Auxiliar = Auxiliar.siguiente
			Indice = Indice + 1
		Grafo_dot += "}"
		Archivo.close()
		subprocess.call(['dot', 'Cola.dot', '-o', 'Cola.png', '-Tpng', '-Gcharset=utf8'], shell = True)

	Graficar()

class Pila:
	def __init__(self):
		self.Inicio = None
		self.Tamano = 0

	def Push(self, dato):
		if Tamano == 0:
			Inicio = NodoSimple(dato, None)
		else:
			Inicio = NodoSimple(dato, Inicio)
		Tamano = Tamano + 1

	def Pop(self):
		if Tamano != 0:
			Cabeza = Inicio
			Inicio = Inicio.siguiente
			Tamano = Tamano - 1
			return Cabeza.dato
		return -1996

	def Graficar(self):
		Archivo = open('Pila.dot', 'w')
		Archivo.close()
		Archivo = open('Pila.dot', 'a')
		Grafo_dot = "digraph Pila{\n label = \"Pila\""
		Auxiliar = Inicio
		Indice = 0
		while(Auxiliar != None):
			Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + Auxiliar.dato + "\"];\n"
			Auxiliar = Auxiliar.siguiente
			Indice = Indice + 1
		Grafo_dot += "\n"
		Auxiliar = Inicio
		Indice = 0
		while(Auxiliar.siguiente != None):
			Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + "[label = \"Siguiente\"];\n"
			Auxiliar = Auxiliar.siguiente
			Indice = Indice + 1
		Grafo_dot += "}"
		Archivo.close()
		subprocess.call(['dot', 'Pila.dot', '-o', 'Pila.png', '-Tpng', '-Gcharset=utf8'], shell = True)

	Graficar()

class NodoMatriz:
	def __init__(self, dato, adelante, atras):
		self.dato = dato
		self.adelante = adelante
		self.atras = atras

class Profundidad:
	def __init__ (self):
		self.inicio = None
		self.fin = None
		self.arriba = None
		self.abajo = None
		self.derecha = None
		self.izquierda = None
		self.tamano = 0

	def Insertar(self, dato):
		if tamano == 0:
			inicio = NodoMatriz(dato, None, None)