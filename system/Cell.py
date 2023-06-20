import pygame

from lib.Color import *

class Cell(pygame.sprite.Sprite):
    def __init__(self, DISPLAY:pygame.Surface, coords:tuple, size:int):
        pygame.sprite.Sprite.__init__(self)
        self.DISPLAY = DISPLAY

        self.coords = coords
        self.size = size

        self.rect = pygame.Rect(coords[0], coords[1], self.size, self.size)

        self.color = Color().DARK_GREY

        self.dead = True

    def update(self):
        self.check_cell_click()
        self.change_color()
        self.draw()

    def draw(self):
        pygame.draw.rect(self.DISPLAY, self.color, self.rect)

    def check_cell_click(self):
        if self.is_hovered():
            if self.is_clicked():
                if self.dead:
                    self.dead = False
                else:
                    self.dead = True
    
    def change_color(self):
        if self.dead:
            self.color = Color().DARK_GREY
        else:
            self.color = Color().WHITE

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0]
    
    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
