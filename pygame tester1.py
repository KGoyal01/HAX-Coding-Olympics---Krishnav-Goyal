import pygame
import time
from pygame.locals import*
pygame.init()


size = 1200,900
width,height = size
canvas = pygame.display.set_mode(size)
pygame.display.set_caption('That Was Easy')
yellow = (255, 255, 0)
gray = (127,127,127)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

background = black



sound = pygame.mixer.Sound('that was easy.mp3')



button = pygame.image.load('buttonred4.png').convert_alpha()
button = pygame.transform.scale(button, (750, 375))
rect = button.get_rect()
rect.center = (1010, 520)

button1 = pygame.image.load('buttonredpressed4.png').convert_alpha()
button1 = pygame.transform.scale(button1, (750, 375))
rect1 = button1.get_rect()
rect1.center = (1010, 600)

earth = pygame.image.load('earth.png').convert_alpha()
earth = pygame.transform.scale(earth, (750, 700))
earthRect = earth.get_rect()
earthRect.center = (500, 1000)

rocket = pygame.image.load('rocketnofire.png').convert_alpha()
rocket = pygame.transform.scale(rocket, (700, 650))
rocketRect = rocket.get_rect()
rocketRect.center = (500, 500)

rocketfire = pygame.image.load('rocketfirenew.png').convert_alpha()
rocketfire = pygame.transform.scale(rocketfire, (700, 650))
rocketfireRect = rocketfire.get_rect()





font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('EASY', True, black)
textRect = text.get_rect()
textRect.center = ((width // 2 + width//3) -10, (height // 2)-20)

font1 = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render('That WAS Easy', True, black)
textRect1 = text1.get_rect()
textRect1.center = ((width // 2 + width//3) -10, (height // 2)+50)

font2 = pygame.font.Font('freesansbold.ttf', 92)
text2 = font.render('Relaunch', True, black)
textRect2 = text2.get_rect()
textRect2.center = ((width // 2 + width//3) -10, (height // 2)+240)


button2 = pygame.image.load('that1.png').convert_alpha()
button2 = pygame.transform.scale(button2, (750, 375))
rect2 = button2.get_rect()
rect2.center = (500, 550)
button3 = pygame.image.load('was1.png').convert_alpha()
button3 = pygame.transform.scale(button3, (750, 375))
rect3 = button3.get_rect()
rect3.center = (505, 350)
button4 = pygame.image.load('easy1.png').convert_alpha()
button4 = pygame.transform.scale(button4, (750, 375))
rect4 = button4.get_rect()
rect4.center = (535, 150)





pressed = False
running = True
running1 = True


while running1:
    


    if pressed:
        print("THIS")
        sound.play()

        canvas.fill(background)
        
        canvas.blit(button1,rect1)
        
        canvas.blit(text1, textRect1)        

        
        canvas.blit(earth,earthRect)
        
        
        canvas.blit(rocketfire,rocketfireRect)
        
        pygame.display.update()
        
        time.sleep(1)
        
        
        canvas.blit(button, rect)
        
        canvas.blit(text, textRect)
        pygame.display.update()

        notouch = True
        while notouch:
            canvas.fill(background)
            canvas.blit(button, rect)
        
            canvas.blit(text, textRect)        
        
            canvas.blit(earth,earthRect)
            rocketfireRect = rocketfireRect.move(0,-2)
            canvas.blit(rocketfire,rocketfireRect)

            if rocketfireRect.bottom < 550 and rocketfireRect.bottom > 0:
                canvas.blit(button2,rect2)
                

            if rocketfireRect.bottom < 350 and rocketfireRect.bottom > 0:
                canvas.blit(button3,rect3)
                
            
            if rocketfireRect.bottom < 150 and rocketfireRect.bottom > 0:
                canvas.blit(button4,rect4)
                

            
            pygame.display.update()
                
            if rocketfireRect.bottom<0:
                notouch= False
            
            
        pygame.draw.rect(canvas,white,textRect2,0)
        canvas.blit(text2,textRect2)
        pygame.display.update()

        pressed1 = False

        while pressed1 == False:
        
            for event in pygame.event.get():
                
                if event.type == MOUSEBUTTONDOWN:
                    if textRect2.collidepoint(event.pos):
                        pressed1 = True
                    
                        running = True
                        pressed = False

                elif event.type == pygame.QUIT:
                    running = False
                    running1 = False
                    pressed1 = True

                        
        

    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
            elif event.type == KEYDOWN:
                if event.key in key_dict:
                    background = key_dict[event.key]
                    
    while running:
        canvas.fill(background)
        caption = 'background color: '+ str(background)
        pygame.display.set_caption(caption)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                running1 = False
            
            elif event.type == MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    if pressed == True:
                        pressed = False
                        
                    else:
                        pressed = True
                
                    print(pressed)
            
        if pressed:
            running = False
            rocketfireRect.center = (511, 617)

        else:
            
            canvas.blit(button, rect)
            canvas.blit(text, textRect)
                    
        
        canvas.blit(earth,earthRect)
        
        
        canvas.blit(rocket,rocketRect)
        pygame.display.update()
        

    

pygame.quit()


