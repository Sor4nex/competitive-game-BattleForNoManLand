import pygame
import sys
import random


if (__name__ == '__main__'):
    pygame.init()
    size = 1000, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Battle for NoMansLand')
    app_state_running = True
    while (app_state_running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                app_state_running = False
        pygame.display.flip()
    pygame.quit()