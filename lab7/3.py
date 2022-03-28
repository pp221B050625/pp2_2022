import pygame
pygame.init()
W, H = 1000, 1000
S = pygame.display.set_mode((W, H))
pygame.display.set_caption("Ball")
FPS = 60
run = True
clock = pygame.time.Clock()
VEL = 20
x, y = 500,500
while run:
    clock.tick(FPS)
    S.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and y-VEL>20:
        y -= VEL
    if keys_pressed[pygame.K_s] and y + VEL < 980:
        y += VEL
    if keys_pressed[pygame.K_d] and x + VEL < 980:
        x += VEL
    if keys_pressed[pygame.K_a] and x - VEL > 20:
        x -= VEL

    pygame.draw.circle(S, (255, 0, 0), (x, y), 25)
    pygame.display.update()

pygame.quit()
