from copy import deepcopy

class Juego:
	def __init__(self, tab):
		self.tab = tab
		self.memoria = []

	def update(self):
		self.guardarPosicion()
		tableroNuevo = deepcopy(self.tab.tablero)

		for y in range(0, self.tab.tam):
			for x in range(0, self.tab.tam):
				vecinos = 0

				try:
					if self.tab.tablero[x][y - 1] == 1:
						vecinos += 1
					if self.tab.tablero[x][y + 1] == 1:
						vecinos += 1
					if self.tab.tablero[x - 1][y] == 1:
						vecinos += 1
					if self.tab.tablero[x + 1][y] == 1:
						vecinos += 1
					if self.tab.tablero[x + 1][y - 1] == 1:
						vecinos += 1
					if self.tab.tablero[x - 1][y - 1] == 1:
						vecinos += 1
					if self.tab.tablero[x + 1][y + 1] == 1:
						vecinos += 1
					if self.tab.tablero[x - 1][y + 1] == 1:
						vecinos += 1
				except:
					pass

				if self.tab.tablero[x][y] == 0 and vecinos == 3:
					tableroNuevo[x][y] = 1
				else:
					if vecinos > 3 or vecinos < 2:
						tableroNuevo[x][y] = 0

		self.tab.tablero = tableroNuevo

	def guardarPosicion(self):
		if len(self.memoria) > 100:
			del(self.memoria[0])
		self.memoria.append(deepcopy(self.tab.tablero))

	def getMemoria(self):
		if len(self.memoria) > 0:
			self.tab.tablero = deepcopy(self.memoria[-1])
			del(self.memoria[-1])
