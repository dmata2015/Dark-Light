import pygame,sys
from pygame.locals import *


class Player(pygame.Rect):
    def __init__(self,x,y):
        super().__init__(x,y,20,20)
        self.x = x
        self.y = y
        print(self)
    
    def draw(self,surface):
        pygame.draw.rect(surface,(255,255,255),self) 

    def update(self,input):
        print(input)
        
        if input == 's':
            self.y += 5
        if input == 'w':
            self.y -= 5
        if input == 'a':
            self.x -= 5
        if input == 'd':
            self.x += 5
    