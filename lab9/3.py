import pygame

pygame.init()
W, H = 700, 700
S = pygame.display.set_mode((W, H))
pygame.display.set_caption("paint")
FPS = 60
clock = pygame.time.Clock()
mode = 'green'
radius = 5
x = 0
y = 0
points = []
run = True
r = 0
S.fill((255, 255, 255))
RCT = 0
p1 = ()
p2 = ()
CENTER = ()
CRC = 0


def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    it = max(abs(dx), abs(dy))

    for i in range(it):
        progress = 1.0 * i / it
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'red'
            elif event.key == pygame.K_g:
                mode = 'green'
            elif event.key == pygame.K_b:
                mode = 'blue '
            elif event.key == pygame.K_e:
                mode = 'white'

        if event.type == pygame.MOUSEMOTION:
            position = event.pos
            points = points + [position]
            points = points[-256:]
        if pygame.mouse.get_pressed()[0]:
            p1 = pygame.mouse.get_pos()
            RCT += 1
        if pygame.mouse.get_pressed()[2]:
            p2 = pygame.mouse.get_pos()
            RCT += 1
        if pygame.key.get_pressed()[pygame.K_c]:
            CENTER = pygame.mouse.get_pos()
            pygame.draw.circle(S, mode, CENTER, 50)


    if RCT >= 2:
        try:
            RECTANGLE = pygame.Rect(p1[0], p1[1], abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
            pygame.draw.rect(S, mode, RECTANGLE, radius)
            p1 = ()
            p2 = ()
            RCT = 0
        except: IndexError
    if CRC >= 1:
        pygame.draw.circle(S, mode, CENTER, radius)
        CRC = 0
    i = 0
    while i < len(points) - 1:
        drawLineBetween(S, i, points[i], points[i + 1], radius, mode)
        i += 1

    pygame.display.update()

pygame.quit()
