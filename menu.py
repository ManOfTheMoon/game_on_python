import pygame, os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
import random, front, help, game_code
from pygame.color import THECOLORS
from pygame import font


front.splash_screen()
rect_play = pygame.Rect(80, 180, 100, 20)
rect_help = pygame.Rect(80, 240, 100, 20)
rect_exit = pygame.Rect(80, 300, 100, 20)
rect = [rect_play, rect_help, rect_exit]
top = [60, 120, 180, 240]
left = 100
width = 200
height = 80
menu_text=["Play", "Help","Exit"]
color = THECOLORS["blue"]

running = True
def init():
    global front, screen
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    front = pygame.font.Font(None, 40)
    pygame.display.set_caption("Main menu")
    screen = pygame.display.set_mode([800, 600])
init()
while running:
    front_menu = pygame.image.load('menu_image.png')
    screen.blit(front_menu, (0, 0))
    for i in range(0,3):
        text = front.render(menu_text[i],1, THECOLORS ["blue"])
        screen.blit(text, [left - 20, top[i] + 120])
    text = front.render("Menu", 1, THECOLORS ["red"])
    screen.blit(text, [80, 100] )
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            point = pygame.mouse.get_pos()
            for i in range(3):
                collide = rect[i].collidepoint(point)
                if collide:
                    break
            if collide:
                if i==2:
                    running = False
                if i==0:
                    pygame.display.quit()
                    game_code.game_cycle()
                    init()
                if i==1:
                    help.help()
