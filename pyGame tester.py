import pygame
from pygame.locals import*
pygame.init()

canvas = pygame.display.set_mode((800,600))
pygame.display.set_caption('That Was Easy')
yellow = (255, 255, 0)
gray = (127,127,127)
green = (0,255,0)
red = (255,0,0)
key_dict = {K_g:green, K_r:red, K_y:yellow}
background = gray
running = True
ball = pygame.image.load("ball.jpg")
rect = ball.get_rect
while running:
    canvas.fill(background)
    pygame.display.update()
    caption = 'background color: '+ str(background)
    pygame.display.set_caption(caption)
    for event in pygame.event.get():
        print(event)
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

        if event.type == pygame.QUIT:
            running = False

pygame.quit()

