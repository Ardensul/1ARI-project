import pygame, sys, random
from pygame.locals import *
from JeffersonShell import*






screen = pygame.display.set_mode((940,700))
pygame.display.set_caption('gui JeffersonShell')
inProgress = True
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False

    pygame.display.update()
pygame.quit()