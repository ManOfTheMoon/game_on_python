import pygame, random
import os 
from pygame import font

dino1 = pygame.image.load('dino1.png')
dino2 = pygame.image.load('dino2.png')
dino3 = pygame.image.load('dino3.png')
dino4 = pygame.image.load('dino4.png')
dino5 = pygame.image.load('dino5.png')
dino6 = pygame.image.load('dino6.png')
dino7 = pygame.image.load('dino7.png')
dino8 = pygame.image.load('dino8.png')

bird1 = pygame.image.load('bird1.png')
bird2 = pygame.image.load('bird2.png')
bird3 = pygame.image.load('bird3.png')
bird4 = pygame.image.load('bird4.png')

front = pygame.image.load('background.jpg')
ground = pygame.image.load('ground.jpg')
front_flip = pygame.transform.flip(front, True, False)

dino_moved = [dino1, dino2, dino3, dino4, dino5, dino6, dino7, dino8]
draw_cactus = [pygame.image.load('cactus2.png'), pygame.image.load('cactus3.png')]
flying_bird = [bird1, bird2, bird3, bird4]
dino_sound = pygame.mixer.Sound("scream.wav")
#cadillac = pygame.mixer.music.load("slava.mp3")

random_cactus = 0

score = 0


xg = 100
yg = 850

xt = 0
yt = -75
xt2 = xt + 1920

xp = 200
yp = 675
img_counter = 0
jump_counter = 30

xc = 1000
yc = 620

xbird = -400
ybird = 200
img_bird_counter = 0

clock = pygame.time.Clock()

dino_make_jump = False

def bird_flying(xbird, ybird):
    global img_bird_counter
    if img_bird_counter == 16:
        img_bird_counter = 0
    screen.blit(flying_bird[img_bird_counter // 4], (xbird, ybird))
    img_bird_counter += 1

def dino_run(xp, yp):
    global img_counter
    if img_counter == 25:
        img_counter = 0
    screen.blit(dino_moved[img_counter // 5], (xp, yp))
    img_counter += 1


def jump():
    global yp, dino_make_jump, jump_counter
    if jump_counter >= -30:
        yp -= jump_counter / 1.8
        jump_counter -= 1
    else:
        jump_counter = 30
        dino_make_jump = False


def front_moved(xt, xt2, yt):
    screen.blit(front, (xt, yt))
    screen.blit(front_flip, (xt2, yt))
    screen.blit(front, (xt - 3840, yt))
    screen.blit(front_flip, (xt2 - 3840, yt))


def ground_moved(xg, yg):
    screen.blit(ground, (xg, yg))
    screen.blit(ground, (xg + 1917, yg))

def game_over():
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(game_over_text, (400, 500))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            pygame.display.quit()
            initialization()
            return True
        pygame.display.flip()
        clock.tick(15)

def initialization():
    global xp, yp, xt, yt, xg, yg, xt2, img_counter, jump_counter, xc, yc, xbird, ybird, img_bird_counter, score, random_cactus, dino_make_jump
    xg = 100
    yg = 850
    xt = 0
    yt = -75
    xt2 = xt + 1920
    xp = 200
    yp = 675
    img_counter = 0
    jump_counter = 30
    xc = 1300
    yc = 620
    xbird = -400
    ybird = 200
    img_bird_counter = 0
    score = 0
    random_cactus = 0
    dino_make_jump = False

def game_cycle():
    global dino_make_jump, xg, xt, xp, yp, yc, xt2, xc, random_cactus, score, img_counter, xbird, ybird, screen, game_over_text
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    font = pygame.font.Font(None, 40)
    game_over_text = font.render(
        'The cactus attracted you with its beauty. Press L to return to the game menu.', True,
        [30, 144, 255])
    pygame.display.set_caption("Run, Dino, Run!")
    game = True
    #pygame.mixer.music.play(-1)

    while game:
        score_text = font.render('Score:' + str(score), True, [30,144,255])
        score += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            dino_sound.play()
            dino_make_jump = True
        if dino_make_jump:
            jump()

        clock.tick(60)

        xbird += 3
        xc -= 8
        screen.blit(front, (0, -75))

        if xc < 0:
            xc = random.randint(1920, 2200)
            random_cactus = random.randint(0, 1)

        if xg < -1817:
            xg += 1917
        xg -= 8

        if xt <= -1920:
            xt += 3840
        xt -= 3

        if xt2 <= 0:
            xt2 += 3840
        xt2 -= 3
        
        if 200 < xc < 460:
            if yp + 90 > yc + 20:
                game = False

        if xbird >= 1920:
            xbird = random.randint(-400, -100)
            ybird = random.randint(100, 400)

        front_moved(xt, xt2, yt)
        ground_moved(xg, yg)
        screen.blit(draw_cactus[random_cactus], (xc, yc))
        dino_run(xp, yp)
        bird_flying(xbird, ybird)
        screen.blit(score_text, [255, 150])
        pygame.display.flip()

    return game_over()
