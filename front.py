import pygame
import os
from pygame.color import THECOLORS
from pygame import font
pygame.init()
pygame.display.set_caption("Dino")
def splash_screen():
    font = pygame.font.Font(None, 45)
    screen = pygame.display.set_mode([1280, 720])
        
    front_image="menu_photo.png"
    zastavka=pygame.image.load(front_image)
    
    font = pygame.font.Font(None, 25)
    text = font.render("Press any key",True, THECOLORS ["red"])    
    screen.blit(zastavka, [0, 0])
    screen.blit(text, [550, 550])
    pygame.display.flip()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False