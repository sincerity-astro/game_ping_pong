import pygame
from random import randint

clock = pygame.time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__ (self, imagee, x, y, speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(imagee), (size1, size2))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keypress = key.get_pressed()
        if keypress[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keypress[K_RIGHT] and self.rect.x < 610:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 15, 20)
        bullets.add(bullet)

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
