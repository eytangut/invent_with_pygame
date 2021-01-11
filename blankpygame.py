import pygame
import sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Hello World!")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
