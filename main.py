import pygame, sys, player, enemy
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock() 
display = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Hello World!')
def gen_player():
    user = player.Player(250,250)
    return user
user = gen_player()

print(user.x,user.y)

user.draw(display)

while True: # main game loop
    clock.tick()
    display.fill((0,0,0))
    user.draw(display)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type != KEYDOWN:
                pass
            input = event.unicode
            user.update(input)
        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()

