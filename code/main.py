import pygame 
import time
from pygame.locals import *

SIZE = 30 #since snake block image is SIZExSIZE pixels

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("../resources/snake_body.jpeg").convert()
        self.x = 100
        self.y = 100
    
    def draw_block(self):
        
        self.parent_screen.fill((0,0,0)) #RGB 0,0,0 is black
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()
    
    def move_up(self):
        self.y -= SIZE 
        self.draw_block()
    def move_down(self):
        self.y += SIZE 
        self.draw_block()
    def move_right(self):
        self.x += SIZE 
        self.draw_block()
    def move_left(self):
        self.x -= SIZE 
        self.draw_block()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Akshay's Snake Game")
        self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.surface.fill((0,0,0)) #RGB 0,0,0 is black

        self.snake = Snake(self.surface)
        self.snake.draw_block()
  
    def run(self):
        #event loop
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            


if __name__ == '__main__':

    game = Game()
    game.run()