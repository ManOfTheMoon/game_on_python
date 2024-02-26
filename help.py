import pygame, sys, random, front
from pygame.color import THECOLORS
from pygame import font

def help():
    pygame.display.set_caption("My game")
    screen = pygame.display.set_mode([800, 600])
    
    screen.fill([0,0,0])
    color = THECOLORS["white"]
    top=10
    left=20
    font = pygame.font.Font(None, 20)
    my_file = open('help.txt', 'r', encoding='utf-8')#Открываем файл для чтения
    lines = my_file.readlines()# Записываем строки из файла в список lines
    my_file.close()
    dlina=len(lines)#Это количество строк
    for i in range(0,dlina):
        ln=lines[i]
        ln=ln[0:-1]#Копируем из исходной строки все, кроме символа конца строки
        text = font.render(ln,1, color)
        screen.blit(text, [left, top] )
        top=top+20# Следующая строка выводится ниже на 20 пикселей
    text = font.render("Press any key", True, color)
    screen.blit(text, [150, 550])
    
    pygame.display.flip()
    running=True
    while running:
         for event in pygame.event.get():
             if event.type == pygame.KEYDOWN:
                 running = False