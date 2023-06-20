import pygame
import sys

class Window(pygame.surface.Surface):
    def __init__(self, width:int, height:int, title:str="Pygame Window", iconpath:str=None, FULLSCREEN:bool=False, RESIZABLE:bool=True):
        super().__init__((width, height))
        if RESIZABLE:
            self = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        else:
            if FULLSCREEN:
                self = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
            else:
                self = pygame.display.set_mode((width, height))

        pygame.display.set_caption(title)
        
        if iconpath != None:
            pygame.display.set_icon(pygame.image.load(iconpath).convert_alpha())

    def update(self):
        pygame.display.update()

    def quit(self):
        pygame.quit()
        sys.exit()