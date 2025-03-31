import pygame
from random import randint

clock = pygame.time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__ (self, imagee, x, y, speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(imagee), (size1, size2))
        self.speedx = speed
        self.speedy = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def moveRIGHT(self):
        keypress = key.get_pressed()
        if keypress[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keypress[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.speed
    def moveLEFT(self):
        keypress = key.get_pressed()
        if keypress[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keypress[K_s] and self.rect.y < 490:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self, racket1, racket2):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if sprite.collide_rect(self, racket1) or sprite.collide_rect(self, racket2):
            self.speedx*= -1
        
        
        

window = display.set_mode((700, 500))
display.set_caption('ъъъ')
background = transform.scale(image.load('pingpong.jpg'), (700, 500))

game = True

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
