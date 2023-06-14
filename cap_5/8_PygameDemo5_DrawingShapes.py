

import pygame
from pygame.locals import *
import sys
import random


#2 - definindo constantes 
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
TEAL = (0, 80, 80)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 
N_PIXELS_PER_FRAME = 3

#3 - inicia o mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 carregar recursos: imagens, sons, etc
ballImage = pygame.image.load('images/ball.png')
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)# o primeiro parametro é o numero de vezes que musica deve repetir (-1 = infinito), o segundo é em que parte a musica deve começar. 

#5 iniciando variaveis 
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

#6 - loop infinito
while True:

    #7 - check for and handle events
    for event in pygame.event.get():
        #clicked the close button? quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        

    # 8 do any "per frame" actions


    #update the ball's location, using the speed in two directions 
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed



    #9 clear the window
    window.fill(GRAY)

    #10 - Draw all window elements
    #draw a box
    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4) #TOP
    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4) #left
    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4) #right
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4) #bottom

    #draw a x in the box
    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 1)
    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 1)

    # Draw a filled circle and an empty circle
    pygame.draw.circle(window, GREEN, (250, 50), 30, 0) #filled
    pygame.draw.circle(window, GREEN, (400, 50), 30, 2) # 2 pixel edge

    # Draw a filled rectangle and an empty rectangle
    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0) #filled
    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1) # 1 pixel edge

    # Draw a filled ellipse and an empty ellipse
    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40),0) # filled
    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40),2) # 2 pixel edge
    
    # Draw a six-sided polygon
    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350), (410, 410), (350, 470),(240, 470), (170,410)))
    
    # Draw an arc
    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2,5)

    # Draw anti-aliased lines: a single line, then a list of points
    pygame.draw.aaline(window, RED, (500, 400), (540, 470), 1)
    pygame.draw.aalines(window, BLUE, True, ((580, 400), (587, 450), (595, 460), (600, 444)), 1)


    #11 - update the window
    pygame.display.update()

    #12 - slow things down a bit
    clock.tick(FRAMES_PER_SECOND) #make pygame wait

    