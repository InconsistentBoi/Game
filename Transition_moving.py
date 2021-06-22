import pygame,os
from pygame.locals import *
import constants

pygame.init()



def fadetoblack(Width,Height): 
    fade = pygame.Surface((Width, Height))
    fade.fill((0,0,0))
    for alpha in range(0, 200,2):
        fade.set_alpha(alpha)
        constants.WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def fadetoscreen(Width,Height): 
    fade = pygame.Surface((Width, Height))
    fade.fill((0,0,0))
    for alpha in range(200, 0,-5):
        fade.set_alpha(alpha)
        constants.WIN.blit(fade, (0,0))
        pygame.display.update()
        constants.WIN.blit(constants.Background2,(0,0))
        pygame.time.delay(1)