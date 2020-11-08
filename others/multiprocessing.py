import pygame
import random


class Blob:
    
    def __init__(self,color):
        
        self.x = random.randrange(0,WIDTH)
        self.y = random.randrange(0,HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color
        
    def move(self):
        
        self.x_move = random.randrange(1,2)
        self.y_move = random.randrange(1,2)
        self.x += self.x_move
        self.y += self.y_move
        
    
    def draw_environemnt():
        pygame.display.fill(WHITE)
        pygame.display.update()
        
    def main():
        
        while True:
            for event in pygrame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        draw_environemnt()
        clock.tick(60)
        
if __name__ == '__main__':
    main()
    