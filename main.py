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
        if keypress[K_w] and self.rect.y > 10:
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
background = transform.scale(image.load('pingponggim1.jpg'), (700, 500))

font1 = font.Font(None, 35)
lose1 = font1.render('о нет 1', True, (180, 0, 0))
lose2 = font1.render('о нет 2', True, (180, 0, 0))

ball = Ball('pingponggim2.jpg', 200, 200, 15, 25, 25)
racket1 = Player('pingponggim3', 30, 250, 15, 15, 50)
racket2 = Player('pingponggim3', 670, 250, 15, 15, 50)

game = True

while game == True:
    ball.update(racket1, racket2)
    racket1.moveRIGHT()
    racket2.moveLEFT()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))

    display.update()
    clock.tick(FPS)
