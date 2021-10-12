import pygame, sys
import serial

ser = serial.Serial('COM3',9600)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
base_font = pygame.font.Font(None,32)

while True:
    x = ser.readline()
    y = float(x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    text_surface = base_font.render(x, True, (255,255,255))
    screen.blit(text_surface,(0,0))

    if y < 6:
        screen.fill((100,100,100))
        text_surface = base_font.render(x, True, (255,255,255))
        screen.blit(text_surface,(0,0))


    pygame.display.flip()
    clock.tick(60)

    
    


