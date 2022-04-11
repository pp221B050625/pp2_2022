import time

import pygame
import os
import random

pygame.init()
W, H = 700, 700
S = pygame.display.set_mode((W, H))
pygame.display.set_caption("Racer")
CN = 0
FPS = 60
clock = pygame.time.Clock()
SPD = 10
font = pygame.font.SysFont("Verdana", 60)
font_s = pygame.font.SysFont("Verdana", 20)
gameover = font.render("GAME OVER", True, (0, 0, 0))
PTS = 0
bg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'AnimatedStreet.png')), (700, 700))
COIN_VALUE = random.randrange(1, 4, 1)
CN_COLLECTED = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'Enemy.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global PTS
        self.rect.move_ip(0, SPD)
        if self.rect.bottom > 700:
            PTS += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 670), 0)

    def draw(self, sur):
        sur.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'Player.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (310, 620)

    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed[pygame.K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < W:
            if pressed[pygame.K_d]:
                self.rect.move_ip(5, 0)

    def draw(self, s):
        s.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'coin.png')), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.bottom > H:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 670), 0)

    def hit(self):
        self.rect.top = 0
        self.rect.center = (random.randint(30, 670), 0)


P1 = Player()
E1 = Enemy()
C = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)
coins = pygame.sprite.Group()
coins.add(C)

VEL = pygame.USEREVENT + 1
pygame.time.set_timer(VEL, 1500)

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == VEL:
            SPD += 1
    if CN_COLLECTED % 3 == 0 and CN_COLLECTED > 0:
        SPD +=2
        CN_COLLECTED = 0

    S.blit(bg, (0, 0))
    score = font.render(str(PTS), True, (0, 0, 0))
    S.blit(score, (600, 10))
    coins_text = font.render(str(CN), True, (255, 255, 0))
    S.blit(coins_text, (600, 80))
    for a in all_sprites:
        S.blit(a.image, a.rect)
        a.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        S.fill((255, 0, 0))
        S.blit(gameover, (175, 300))
        pygame.display.update()
        for a in all_sprites:
            a.kill()
        time.sleep(2)
        pygame.quit()
    if pygame.sprite.spritecollideany(P1, coins):
        CN += COIN_VALUE
        CN_COLLECTED += 1
        C.hit()
        COIN_VALUE = random.randrange(1, 4, 1)


    pygame.display.update()
pygame.quit()
