import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1820,980))
done = False

#player cords:
x=60
y=60
x1=130
y1=60
timer1 = time.time()
stopwatch1 = time.time()
timerUpdated = 0

timer2 = time.time()
stopwatch2 = time.time()
timer2Updated = 0

clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    screen.fill((0,0,0))
    Font = pygame.font.SysFont("comicsansms", 70, True, True)
    Title = Font.render("Blancaca", True, (255,255,255))
    screen.blit(Title, (710,390))


    pressed = pygame.key.get_pressed()



    if pressed[pygame.K_UP]: y=y-5
    if pressed[pygame.K_DOWN]: y=y+5
    if pressed[pygame.K_RIGHT]: x=x+5
    if pressed[pygame.K_LEFT]: x=x+5

    if pressed[pygame.K_w]: y1=y1-5
    if pressed[pygame.K_s]: y1=y1+5
    if pressed[pygame.K_d]: x1=x1+5
    if pressed[pygame.K_a]: x1=x1-5




    player1 = pygame.draw.rect(screen, (101,205,205), pygame.Rect(x, y, 50, 50))
    player2 = pygame.draw.rect(screen, (101,205,205), pygame.Rect(x1, y1, 50, 50))

    wall1 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(0,0, 1820,50))
    wall2 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(0, 0, 50, 980))
    wall3 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(0, 930, 1820, 50))
    wall4 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(1770, 0, 50, 980))

    wall5 = pygame.draw.rect(screen, (0,129,0), pygame.Rect(300, 50, 80, 740))
    wall6 = pygame.draw.rect(screen, (0, 129, 0), pygame.Rect(370, 700, 500, 90))
    wall7 = pygame.draw.rect(screen, (0, 129, 0), pygame.Rect(1000, 230, 80, 700))
    wall8 = pygame.draw.rect(screen, (0, 129, 0), pygame.Rect(1400, 50, 80, 700))
    final = pygame.draw.rect(screen, (0,129, 0),pygame.Rect(1600, 60,70, 70))

    if player1.colliderect(wall1) or player1.colliderect(wall2) or player1.colliderect(wall3) or player1.colliderect(wall4) or player1.colliderect(wall5) or player1.colliderect(wall6) or player1.colliderect(wall7) or player1.colliderect(wall8):
        if pressed[pygame.K_UP]: y = y + 5
        if pressed[pygame.K_DOWN]: y = y - 5
        if pressed[pygame.K_LEFT]: x = x + 5
        if pressed[pygame.K_RIGHT]: x = x - 5

    if player2.colliderect(wall1) or player2.colliderect(wall2) or player2.colliderect(wall3) or player2.colliderect(wall4) or player2.colliderect(wall5) or player2.colliderect(wall6) or player2.colliderect(wall7) or player2.colliderect(wall8):
        if pressed[pygame.K_w]: y1 = y1 + 10
        if pressed[pygame.K_s]: y1 = y1 - 10
        if pressed[pygame.K_a]: x1 = x1 + 10
        if pressed[pygame.K_d]: x1 = x1 - 10


    if player1.colliderect(final):
        x = 60
        y = 60
        timer1 = time.time()
        timerUpdated = round(timer1 - stopwatch1,2)
        stopwatch1 = time.time()

    if player2.colliderect(final):
        x1 = 130
        y1 = 60
        timer2 = time.time()
        timer2Updated = round(timer2 - stopwatch2, 2)
        stopwatch2= time.time()


    Font1 = pygame.font.SysFont("comicsansms", 70, True, True)
    Time1 = Font1.render("Ur time player 1:" + str(timerUpdated), True, (0,0,255))
    screen.blit(Time1, (50,650))

    Font2 = pygame.font.SysFont("comicsansms", 70, True, True)
    Time2 = Font1.render("Ur time player 2:" + str(timer2Updated), True, (0,0,255))
    screen.blit(Time1, (1100,650))

    pygame.display.flip()
    clock.tick(60)