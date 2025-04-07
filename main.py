from pygame import *
from random import randint

clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, imagee, x, y, speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(imagee), (size1, size2))
        self.speedx = speed
        self.speedy = speed
        self.speed = speed
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
            self.speedx *= -1
        if self.rect.y > 490:
            self.speedy *= -1
        if self.rect.y < 10:
            self.speedy *= -1


window = display.set_mode((700, 500))
display.set_caption('ъъъ')
background = transform.scale(image.load('pingpingim1.jpg'), (700, 500))
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('о нет 1', True, (180, 0, 0))
font2 = font.Font(None, 35)
lose2 = font2.render('о нет 2', True, (180, 0, 0))

sharik = Ball('pingpongim2.jpg', 200, 200, 5, 100, 100)
racket1 = Player('pingpongim3.png', 25, 250, 10, 60, 200)
racket2 = Player('pingpongim3.png', 640, 250, 10, 60, 200)

game = True

while game == True:
    window.blit(background, (0, 0,))
    sharik.reset()
    racket1.reset()
    racket2.reset()
    sharik.update(racket1, racket2)
    racket1.moveRIGHT()
    racket2.moveLEFT()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sharik.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if sharik.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))

    display.update()
    clock.tick(FPS)
