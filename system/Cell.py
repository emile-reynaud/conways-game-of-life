import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, DISPLAY:pygame.Surface, size:int):
        pygame.sprite.Sprite.__init__(self)
        self.DISPLAY = DISPLAY

        self.group = pygame.sprite.Group()

        self.dead_img = pygame.image.load("assets/textures/cell/dead.png").convert_alpha()
        self.alive_img = pygame.image.load("assets/textures/cell/alive.png").convert_alpha()
        self.hovered_img = pygame.image.load("assets/textures/cell/hovered.png").convert_alpha()

        self.img = self.dead_img

        self.size = size

        self.rect = self.img.get_rect()
        self.rect.width, self.rect.height = self.size, self.size

        self.dead_img = pygame.transform.scale(self.dead_img, (self.size, self.size))
        self.alive_img = pygame.transform.scale(self.alive_img, (self.size, self.size))
        self.hovered_img = pygame.transform.scale(self.hovered_img, (self.size, self.size))

        self.clicked = False
        self.dead = True
        self.hovered = False

    def add(self, coords:tuple):
        self.rect.topleft = coords
        pygame.sprite.Sprite.add(self, self.group)

    def draw(self):
        self.update()
        pygame.sprite.Sprite.image = self.img
        self.group.draw(self.DISPLAY)

    def update(self):
        if self.is_hovered():
            if self.is_clicked():
                if self.dead:
                    self.dead = False
                    self.img = self.alive_img
                else:
                    self.dead = True
                    self.img = self.dead_img
            else:
                self.img = self.hovered_img
        else:
            if self.dead:
                self.img = self.dead_img
            else:
                self.img = self.alive_img
        
        # self.clicked = False

    def is_clicked(self):
        if pygame.mouse.get_pressed()[0] == 1:
            self.clicked = True
        else:
            self.clicked = False

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
