import pygame
import os
import datetime

pygame.init()
WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
A = (700, 500)
FPS = 1

MICKEY_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'mickeynohands.jpg')), A)
MICKEY_RIGHTARM = pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'mickeyrightarm2.png')), A), -54)
MICKEY_LEFTARM = pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'mickeyleftarm2.png')), A), 60)

now = datetime.datetime.now()
print(now.minute, now.second)
langle = now.second * -6
rangle = now.minute * -6
clock = pygame.time.Clock()
cnt = 0
run = True
while run:
    cnt += 1
    if cnt % 60 == 0:
        rangle -= 6
    langle -= 6
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MICKEY_IMG, (150, 250))
    right_copy = pygame.transform.rotate(MICKEY_RIGHTARM, rangle)
    left_copy = pygame.transform.rotate(MICKEY_LEFTARM, langle)
    SCREEN.blit(right_copy, (500 - int(right_copy.get_width() / 2), 500 - int(right_copy.get_height() / 2)))
    SCREEN.blit(left_copy, (500 - int(left_copy.get_width() / 2), 500 - int(left_copy.get_height() / 2)))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
