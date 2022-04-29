import time
import psycopg2
import pygame
import random
from config import config

pygame.init()

W, H = 700, 700
S = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
FPS = 60
clock = pygame.time.Clock()
run = True
b = pygame.Rect(0, 0, 700, 700)
font = pygame.font.SysFont("Verdana", 40)
EATEN = 0
LEVEL = 0
FOOD_VALUE = random.randrange(1, 4, 1)
TIMER = 0
username_input = True
name = ""
insert = "Insert username: "
conn = None
loaded = False

try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
except Exception as e:
    print(str(e))


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
        if self.size % 5 == 0:
            global LEVEL
            LEVEL += 1
            self.speed += 1.5


class Food:
    def __init__(self):
        self.x = random.randint(45, 655)
        self.y = random.randint(45, 655)

    def hit(self):
        self.x = random.randint(45, 655)
        self.y = random.randint(45, 655)

    def draw(self):
        pygame.draw.rect(S, (255, 0, 0), (self.x, self.y, 50, 50))


def save_game():
    sql = """
    SELECT username from game
    where username = %s ;
    """
    try:
        cur.execute(sql, [name])
        row = cur.fetchone()
        if row is None:
            i_rows = 0
        else:
            i_rows = 1
            username = row[0]
    except Exception as e:
        print(str(e))
    if i_rows == 0:
        sql = """
        INSERT INTO game(username, user_score, user_level)
        VALUES(%s, %s, %s);
        """
        try:
            cur.execute(sql, (name, EATEN, LEVEL))
        except Exception as e:
            print(str(e))
    else:
        sql = """
        UPDATE game
        set user_score = %s, user_level = %s
        where username = %s
        
        """
        try:
            cur.execute(sql, (EATEN, LEVEL, name))
        except Exception as e:
            print(str(e))
    conn.commit()
    cur.close()


def load_game():
    sql = """
    SELECT user_score, user_level from game
    where username = %s
    """
    global EATEN
    global LEVEL
    try:
        cur.execute(sql, [name])
        row = cur.fetchone()
        EATEN = int(row[0])

        LEVEL = int(row[1])

    except Exception as e:
        print(str(e))


snake = Snake(350, 350)
food = Food()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if username_input:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
                if event.key == pygame.K_RETURN:
                    username_input = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                save_game()
                run = False
    if username_input:
        S.fill((0, 0, 0))
        text = font.render(name, True, (255, 255, 255))
        insert = font.render("Insert username: ", True, (255, 255, 255))
        S.blit(insert, (0, 0))
        S.blit(text, (350, 0))
        pygame.display.update()

    else:
        if not loaded:
            load_game()
            loaded = True
            snake.speed += LEVEL * 1.5
        S.fill((110, 174, 0))
        score = font.render(str(EATEN), True, (255, 255, 255))
        LV = font.render(str(LEVEL), True, (255, 255, 255))
        S.blit(score, (600, 40))
        S.blit(LV, (600, 100))
        pygame.draw.rect(S, (0, 0, 0), b, 20)
        snake.draw()
        food.draw()
        TIMER += 1 / 60
        snake.move()

        if TIMER >= 5 and TIMER > 0:
            food.hit()
            TIMER = 0

        if snake.elements[0][0] <= 20 or snake.elements[0][0] >= 680:
            S.fill((255, 0, 0))
            pygame.display.update()
            time.sleep(2)
            EATEN = 0
            LEVEL = 0
            sql = """
                                            UPDATE game
                                            set user_score = %s, user_level = %s
                                            where username = %s

                                            """
            try:
                cur = conn.cursor()
                cur.execute(sql, (EATEN, LEVEL, name))
            except Exception as e:
                print(str(e))
            conn.commit()

            run = False
        if snake.elements[0][1] <= 20 or snake.elements[0][1] >= 680:
            S.fill((255, 0, 0))
            pygame.display.update()
            time.sleep(2)
            EATEN = 0
            LEVEL = 0
            sql = """
                                UPDATE game
                                set user_score = %s, user_level = %s
                                where username = %s

                                """
            try:
                cur = conn.cursor()
                cur.execute(sql, (EATEN, LEVEL, name))
                print("UPDATED")
            except Exception as e:
                print(str(e))
            conn.commit()

            run = False
        if food.x <= snake.elements[0][0] <= food.x + 65 and food.y <= snake.elements[0][1] <= food.y + 65:
            EATEN += FOOD_VALUE
            snake.add = True
            food.hit()
            TIMER = 0
            FOOD_VALUE = random.randrange(1, 4, 1)

        try:
            pygame.display.update()
        except Exception as e:
            print(str(e))

pygame.quit()
