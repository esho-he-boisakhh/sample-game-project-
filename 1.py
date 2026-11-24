import pygame
from sys import exit

#initializing pygame
pygame.init()

WIDTH = 800
HEIGHT = 800
#display (screen user is going to see)
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #args are tuples
pygame.display.set_caption("Sample Game")  #to give the game a name

while True:     #game runs inside True
    for event in pygame.event.get():    #basically event loop to check if any event is happening
        if event.type == pygame.QUIT:
            pygame.quit()
            #  File "..\practice game\1.py", line 17, in <module> pygame.display.update()         #to update display with above stuff ^^^^^^^^^^^^^^^^^^^^^^^   pygame.error: video system not initialized
            #this is because we have not closed upper while loop but system has quit, avoid this using sys module
            exit()
    #draw elements here
    #update whatever needs updating
    pygame.display.update()         #to update display with above stuff
    #IMPORTANT: DO NOT RUN WITHOUT ADDING CLOSE OPTION!!! PLAYER NEEDS TO CLOSE GAME!!!!
    