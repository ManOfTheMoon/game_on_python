#Неуправляемое и управляемое движение
import pygame, sys, random
from pygame import font
pygame.init()
from pygame.color import THECOLORS
font = pygame.font.Font(None, 24)
screenX=900
screenY=600
screen = pygame.display.set_mode([screenX,screenY])

n=0
color=THECOLORS['red']

gun = pygame.image.load('gun.png')
gun = pygame.transform.scale(gun, (200, 120)) 
bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (80, 40))
house_unbroken = pygame.image.load("house.png")
house_unbroken  = pygame.transform.scale(house_unbroken , (200, 200))
burst = pygame.image.load("blast.png")
burst = pygame.transform.scale(burst, (200, 200))
object = [house_unbroken , burst] # создаём список состояний дома
house = object[0]

def move_gun(xg,yg,step):#Движение пистолета
    if keys[pygame.K_UP]:
        yg=yg-step
    if keys[pygame.K_DOWN]:
        yg=yg+step
    if keys[pygame.K_LEFT]:
        xg-=step
    if keys[pygame.K_RIGHT]:
        xg+=step
    return xg, yg

def shoot(xg, yg, xb, yb, shot):
    global n
    if keys[pygame.K_SPACE]:
        if not shot:
            n += 1
            shot = True
            xb = xg + 200
            yb = yg 
        
    return xb, yb, shot

def blast():
    global house, xb, yb, shot
    if xb + 40 >= xh and yh <= yb <= yh + 240:
        print("Destroy house")
        house = object[1]
        yb, xb = 0, 0
        shot = False


delay = 50
interval = 25
pygame.key.set_repeat(delay, interval)
running = True
xs, ys = 0, 0
xg,yg = 200,100 # координаты пистолета
xh, yh = 700, 200 # координаты дома
step = 10
shot = False  
xb, yb = 0, 0 # задаём переменные
text = font.render(" Выстрелов "+str(n),True, THECOLORS ["blue"])

while running:
    screen.fill(THECOLORS['white'])
    screen.blit(text, [250, 50] )
                       
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            xb, yb, shot = shoot(xg, yg, xb, yb, shot) # при нажатии на пробел переменная shot становится True и мы запускаем движение пули 
            if keys[pygame.K_o]: # при нажатии клавиши "О" восстанавливаем дом
                xh, yh = 700, 200
                house = object[0]
                print("Recover house")
        xg, yg = move_gun(xg, yg, step)
          
        
    if shot: # когда выстрел сделан, мы постоянно рисуем пулю и перемещаем, до момента столкновения с границей экрана
        screen.blit(bullet, [xb,yb])
        xb+=step
        if xb >= screenX:
            shot = False
            xb, yb = 0, 0
            
    blast()            
    text = font.render(" Выстрелов "+str(n),True, THECOLORS ["blue"])
    screen.blit(gun, [xg,yg])
    screen.blit(house,[xh,yh])
    pygame.display.flip()
pygame.quit()
