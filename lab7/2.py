import pygame
import os
pygame.init()
W, H = 500, 500
S = pygame.display.set_mode((W, H))
pygame.display.set_caption('Music Player')
FPS = 60
clock = pygame.time.Clock()
run = True
songs = ['wet.mp3', 'sweden.mp3', 'chris.mp3', 'excuse.mp3']
pygame.mixer.music.load(os.path.join('assets', 'wet.mp3'))
id = 0
VEL = 20

while run:
    clock.tick(FPS)
    S.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.play()
            if event.key == pygame.K_UP:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_DOWN:
                pygame.mixer.music.pause()
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.load(os.path.join('assets', songs[id+1]))
                id += 1
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.load(os.path.join('assets', songs[id-1]))
                id -= 1
                pygame.mixer.music.play()

    pygame.display.update()
pygame.quit()