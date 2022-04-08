import time

import pygame
import os
import random

pygame.init()

W, H = 700, 700
S = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
FPS = 60
clock = pygame.time.Clock()
run = True
b = pygame.Rect(0, 0, 700, 700)
font = pygame.font.SysFont("Verdana", 60)
EATEN = 0
LEVEL = 0

class Snake:
    def __init__(self, x, y):

        self.size = 1
        self.elements = [[x, y]]
        self.radius = 30
        self.mx = 0
        self.my = 0
        self.add = False
        self.speed = 3

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(S, (0, 0, 255), element, self.radius)

    def move(self):
        if self.add:
            self.add_one()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.mx
        self.elements[0][1] += self.my
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.mx = self.speed
            self.my = 0
        if pressed[pygame.K_LEFT]:
            self.mx = -self.speed
            self.my = 0
        if pressed[pygame.K_UP]:
            self.mx = 0
            self.my = -self.speed
        if pressed[pygame.K_DOWN]:
            self.mx = 0
            self.my = self.speed

    def add_one(self):
        self.size += 1
        self.elements.append([0, 0])
        self.add = False
        if self.size % 5 ==0:
            global LEVEL
            LEVEL += 1
            self.speed += 2


class Food:
    def __init__(self):
        self.x = random.randint(45, 655)
        self.y = random.randint(45, 655)

    def hit(self):
        self.x = random.randint(45, 655)
        self.y = random.randint(45, 655)

    def draw(self):
        pygame.draw.rect(S, (255, 0, 0), (self.x, self.y, 50, 50))


snake = Snake(350, 350)
food = Food()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    S.fill((110, 174, 0))
    score = font.render(str(EATEN), True , (255,255,255))
    LV = font.render(str(LEVEL), True , (255,255,255))
    S.blit(score, (600, 40))
    S.blit(LV, (600, 100))
    pygame.draw.rect(S, (0, 0, 0), b, 20)
    snake.draw()
    food.draw()
    snake.move()
    if snake.elements[0][0] <= 20 or snake.elements[0][0] >= 680:
        S.fill((255, 0, 0))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
    if snake.elements[0][1] <= 20 or snake.elements[0][1] >= 680:
        S.fill((255, 0, 0))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
    if food.x <= snake.elements[0][0] <= food.x + 55 and food.y <= snake.elements[0][1] <= food.y + 55:
        EATEN += 1
        snake.add = True
        food.hit()

    pygame.display.update()
pygame.quit()
