import os
from random import randint
from math import sqrt
from enum import Enum, unique
import pygame


@unique
class Color(Enum):
    """颜色"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """随机颜色"""
        r = randint(1, 220)
        g = randint(1, 220)
        b = randint(1, 220)
        return (r, g, b)


class Ball(object):

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self._x = x
        self._y = y
        self._radius = radius
        self._sx = sx
        self._sy = sy
        self._color = color
        self._alive = True

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive

    def move(self, screen):
        self._x += self._sx
        self._y += self._sy
        if self._x - self._radius <= 0 \
                or self._x + self._radius >= screen.get_width():
            self._sx = -self._sx
        if self._y - self._radius <= 0 \
                or self._y + self._radius >= screen.get_height():
            self._sy = -self._sy

    def draw(self, screen):
        if self._alive:
            pygame.draw.circle(screen, self._color,
                               (self._x, self._y), self._radius, 0)

    def eat(self, other):
        distance = sqrt((self._x - other._x) ** 2 + (self._y - other._y)**2)
        if distance < (self._radius + other._radius) and self._radius > other._radius:
            other.alive = False
            self._radius = self._radius + int(other._radius * 0.15)
            return True
        return False


class Game(object):

    def __init__(self):
        self._balls = []
        self._screen = None

    def create_ball(self, x, y):
        sx = randint(-10, 10)
        sy = randint(-10, 10)
        color = Color.random_color()
        radius = randint(20, 30)
        ball = Ball(x, y, radius, sx, sy, color)
        self._balls.append(ball)

    def draw_balls(self):
        for ball in self._balls:
            ball.draw(self._screen)

    def move_balls(self):
        for ball in self._balls:
            ball.move(self._screen)
            for other in self._balls:
                if ball.eat(other):
                    self._balls.remove(other)

    def start(self):
        pygame.init()
        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('大球吃小球')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    self.create_ball(x, y)
            
            self._screen.fill((255,255,255))
            self.draw_balls()
            pygame.display.flip()
            pygame.time.delay(20)
            self.move_balls()
             
def main_game():
    game = Game()
    game.start()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')

    # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # ball_image = pygame.image.load(
    #     os.path.split(__file__)[0] + '/res/ball.png')
    # screen.blit(ball_image, (50, 50))
    # pygame.display.flip()
    def draw_ball():
        ball_img = pygame.image.load(os.path.join(
            os.path.split(__file__)[0],
            './res/ball.png'
        )
        )
        screen.blit(ball_img, (x, y))

    x, y = 50, 50
    dx, dy = 5, 5
    bgcolor = (255, 255, 255)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(bgcolor)
        draw_ball()
        pygame.display.flip()
        pygame.time.delay(50)
        x = x + dx
        y = y + dy
        if x >= 800:
            dx = -5
        elif x <= 0:
            dx = 5

        if y >= 600:
            dy = -5
        elif y <= 0:
            dy = 5


if __name__ == '__main__':
    # main()
    main_game()
