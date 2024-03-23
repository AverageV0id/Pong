import random
import pygame as pg
from Entity.Player import Player
from Entity.ball import Ball

W, H = 700, 700

pg.font.init()
pg.mixer.init()
pg.init
font = pg.font.SysFont('None', 100)
screen = pg.display.set_mode((W, H))
run = True
score1, score2 = 0, 0
line = []
add_speed = 0
move_x, move_y = 3, 0
score1 = 0
score2 = 0
player1 = Player(15, 100, 'red', 20, H // 2 - 100)
player2 = Player(15, 100, 'blue', W - 40, H // 2 - 100)
ball = Ball(10, 'white', (W - 10) // 2, (H - 10) // 2)

all_sprites = pg.sprite.Group(player1, player2, ball)

clock = pg.time.Clock()
x = 0
y = 30

while run:

    clock.tick(60)

    screen.fill("black")

    for i in range(1, 20, 1):
        if i % 2 == 0:
            x += 50
            y += 50
        else:
            line = pg.draw.line(screen, 'white', (400, x), (400, y), width=7)
            x += 15
            y += 15

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        player1.rect.y -= 3
    if player1.rect.y < 0:
        player1.rect.y = 0

    if keys[pg.K_d]:
        player1.rect.x += 3
    if player1.rect.x > 100:
        player1.rect.x = 100

    if keys[pg.K_a]:
        player1.rect.x -= 3
    if player1.rect.x < 10:
        player1.rect.x = 10

    if keys[pg.K_s]:
        player1.rect.y += 3
    if player1.rect.y > 600:
        player1.rect.y = 600

    if keys[pg.K_UP]:
        player2.rect.y -= 3
    if player2.rect.y < 0:
        player2.rect.y = 0

    if keys[pg.K_RIGHT]:
        if player2.rect.x > 670:
            pass
        else:
            player2.rect.x += 3

    if keys[pg.K_LEFT]:
        if player2.rect.x < 600:
            pass
        else:
            player2.rect.x -= 3

    if keys[pg.K_DOWN]:
        player2.rect.y += 3
    if player2.rect.y > 600:
        player2.rect.y = 600

    ball.rect.x += move_x
    ball.rect.y += move_y
    if pg.sprite.spritecollide(player1, [ball], False):
        move_x = 2 + add_speed
        move_y = random.randint(-2, 2)
        add_speed += 0.8

    if pg.sprite.spritecollide(player2, [ball], False):
        move_x = -(2 + add_speed)
        move_y = random.randint(-2, 2)
        add_speed += 0.8

    if ball.rect.y > 700:
        move_y = -3
    if ball.rect.y < 5:
        move_y = 3

    if ball.rect.x < 0:
        move_x = 2
        add_speed = 0
        ball.rect.x = 400
        ball.rect.y = 400
        score2 += 1
    if ball.rect.x > 700:
        move_x = 2
        add_speed = 0
        ball.rect.x = 400
        ball.rect.y = 400
        score1 += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    if ball.rect.y < 0:
        move_y = -3

    text1 = font.render(f'{score1}', False, 'white')
    text2 = font.render(f'{score2}', False, 'white')

    screen.blit(text1, (0 + 200, H - 100))
    screen.blit(text2, (W - 200, H - 100))

    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.update()
pg.quit()
