import random, sys, time, math, pygame
from pygame.locals import *
FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
HALF_WINHEIGHT = int(WINHEIGHT / 2)
HALF_WINWIDTH = int(WINWIDTH / 2)
GRASSCOLOR = (24, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CAMERASLACK = 90
MOVERATE = 9
BOUNCERATE = 6
BOUNCEHEIGHT = 30
STARTSIZE = 25
WINSIZE = 300
INVULNTIME = 2
