import pygame

class Tablero:
	def __init__(self, tam = None, tab = None, matriz = None):
		if tam:
			self.tam = tam
			self.tablero = [0] * self.tam
			for i in range(self.tam):
				self.tablero[i] = [0] * self.tam
		elif tab:
			self.tam = tab.tam
			self.tablero = tab.tablero
		elif matriz:
			self.tam = len(matriz)
			self.tablero = matriz

	def getPosicion(self, x, y):
		if x >= 0 and x < self.tam and y >= 0 and y < self.tam:
			return self.tablero[y][x]

	def setPosicion(self, x, y, valor):
		if x >= 0 and x < self.tam and y >= 0 and y < self.tam:
			self.tablero[y][x] = valor

	def cambiarPosicion(self, x, y):
		if x >= 0 and x < self.tam and y >= 0 and y < self.tam:
			self.tablero[y][x] = 1 if self.tablero[y][x] == 0 else 0

	def dibujar(self, scrn, colorLinea = (0,0,0), colorCelda = (0,255,0)):
		#Dibuja las lineas del tablero
		for y in range(self.tam):
			pygame.draw.line(scrn, colorLinea, (0,scrn.get_size()[1] / self.tam * y), (scrn.get_size()[0], scrn.get_size()[1] / self.tam * y))
		for x in range(self.tam):
			pygame.draw.line(scrn, colorLinea, (scrn.get_size()[0] / self.tam * x,0), (scrn.get_size()[0] / self.tam * x, scrn.get_size()[1]))

		#Dibuja los datos del tablero

		for y in range(self.tam):
			for x in range(self.tam):
				if self.tablero[y][x] == 1:
					xi = scrn.get_size()[0] / self.tam * x
					yi = scrn.get_size()[1] / self.tam * y
					xf = scrn.get_size()[0] / self.tam
					yf = scrn.get_size()[1] / self.tam
					pygame.draw.rect(scrn, colorCelda, (xi, yi, xf, yf))