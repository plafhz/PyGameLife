import pygame
from pygame.locals import *
import sys
from Juego import Juego
from Tablero import Tablero

def main():
	tam = 100
	pause_icon = pygame.image.load("img/pause.png")
	play_icon  = pygame.image.load("img/play.png")
	clock = pygame.time.Clock()
	scrn = pygame.display.set_mode((800,600))
	pygame.display.set_caption("GameOfLife")
	pygame.display.set_icon(pygame.image.load("img/icon.png"))
	game = Juego(Tablero(tam))
	pausa = True
	colorLineas = (0,0,0)
	while True:
		clock.tick(30)
		for evento in pygame.event.get():
			if evento.type == QUIT:
				sys.exit()
			if evento.type == KEYDOWN:
				if pygame.key.get_pressed()[K_SPACE]:
					pausa = not pausa
				if pygame.key.get_pressed()[K_r]:
					game = Juego(Tablero(tam))
				if pygame.key.get_pressed()[K_v]:
					colorLineas = (50,50,50) if colorLineas == (0,0,0) else (0,0,0)
				if pygame.key.get_pressed()[K_RIGHT] and pausa:
					game.update()
				if pygame.key.get_pressed()[K_LEFT] and pausa:
					game.getMemoria()
			if evento.type == MOUSEMOTION or evento.type == MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0] == 1:
					x = int(pygame.mouse.get_pos()[0] * tam / scrn.get_size()[0])
					y = int(pygame.mouse.get_pos()[1] * tam / scrn.get_size()[1])
					game.tab.setPosicion(x,y,1)
				elif pygame.mouse.get_pressed()[2] == 1:
					x = int(pygame.mouse.get_pos()[0] * tam / scrn.get_size()[0])
					y = int(pygame.mouse.get_pos()[1] * tam / scrn.get_size()[1])
					game.tab.setPosicion(x,y,0)

		scrn.fill((0,0,0))
		game.tab.dibujar(scrn, colorLineas, (0,240,0))
		if not pausa:
			game.update()
			scrn.blit(play_icon, (400, 0))
		else:
			scrn.blit(pause_icon, (400,0))
		pygame.display.flip()


if __name__ == '__main__':
	main()
