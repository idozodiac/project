import pygame, sys
import serial

ser = serial.Serial('COM3',9600)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
base_font = pygame.font.Font(None,32)
warning = "You are too close!"
a = 'u good'


while True:
    x = ser.readline()
    t = str(x.decode().strip())
    d = ('Distance is: ' + t + 'cm')
    y = float(x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    text_surface = base_font.render(d, True, (255,255,255))
    screen.blit(text_surface,(0,0))

    if y < 15:
        screen.fill((255,0,0))
        text_surface = base_font.render(d, True, (255,255,255))
        text2 = base_font.render(warning, True, (255,255,255))
        screen.blit(text_surface,(0,0))
        screen.blit(text2,(300,300))
    else:
        text3 = base_font.render(a, True, (255,255,255))
        screen.blit(text3,(300,300))
        
        
        
        
        
   


    pygame.display.flip()
    clock.tick(60)


