
import pygame
from pygame.locals import *
import time
import random


SIZE = 40
BACKGROUND_COLOR = (100, 150, 10)

class minibox:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("box-2.png").convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 20) * SIZE
        self.y = random.randint(1, 15) * SIZE


class Snake: 
    def __init__ (self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("box.png").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        #update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]


        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Basic Snake Game")
        self.surface = pygame.display.set_mode((900, 700))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.minibox = minibox(self.surface)
        self.minibox.draw()

    def reset(self):
        self.snake = Snake(self.surface)
        self.minibox = minibox(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False


    def play(self):
        self.snake.walk()
        self.minibox.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating small square
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.minibox.x, self.minibox.y):
            sound = pygame.mixer.Sound("retrosound.wav")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.minibox.move()

        # snake hitting its tail
        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise ("Collision")

    def display_score(self):
        font = pygame.font.SysFont('timesnewroman',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(400,10))

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('timesnewroman', 30)
        line1 = font.render(f"Game Over! You Loose! Score {self.snake.length}", True, (255,255,255))
        self.surface.blit(line1, (200,300))
        line2 = font.render("To Play Again, Press Enter or Press Escape to Leave", True, (255,255,255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def run(self):
        running = True
        pause = False
    
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False 

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left() 

                        if event.key == K_RIGHT:
                            self.snake.move_right()                 
                    
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False 

            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.3)

if __name__ == "__main__":
    game = Game()
    game.run()

