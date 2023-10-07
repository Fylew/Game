import pygame
import random

WIDTH = 1000
HEIGHT = 561

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Звезда")
screen.fill((97, 178, 199))

icon = pygame.image.load('image/free-icon-abstract-shape-6604311.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('image/1641565350_33-www-funnyart-club-p-foni-dlya-platformerov-34.png')

# images for player animation
walk_right = [
    pygame.image.load("image/move/right1.png"),
    pygame.image.load("image/move/right2.png"),
    pygame.image.load("image/move/right3.png"),
    pygame.image.load("image/move/right4.png"),
    pygame.image.load("image/move/right5.png"),
]
walk_left = [
    pygame.image.load("image/move/left1.png"),
    pygame.image.load("image/move/left2.png"),
    pygame.image.load("image/move/left3.png"),
    pygame.image.load("image/move/left4.png"),
    pygame.image.load("image/move/left5.png"),
]

# images for enemy animation
enemy_images = [
    pygame.image.load("image/enemy/enemy1.png"),
    pygame.image.load("image/enemy/enemy2.png"),
    pygame.image.load("image/enemy/enemy3.png"),
    pygame.image.load("image/enemy/enemy4.png"),
    pygame.image.load("image/enemy/enemy5.png"),
]

player_speed = 50
player_x = 200
player_y = 100

enemy_speed = random.randint(3,30)
enemies = []
enemy_x = WIDTH  # start the enemy outside the screen for initial appearance
enemy_y = random.randint(0, HEIGHT - 50)
enemy_wk = random.randint(0, 4)

wk = 0
bg_x = 0


bullets = []

while True:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # shoot bullets when Space key is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append({'x': player_x + 50, 'y': player_y + 20, 'speed': 10})

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        screen.blit(walk_right[wk], (player_x, player_y))
    elif keys[pygame.K_a]:
        screen.blit(walk_left[wk], (player_x, player_y))
    else:
        screen.blit(walk_right[wk], (player_x, player_y))

    if keys[pygame.K_LSHIFT]:
        player_speed = 100
    else:
        player_speed = 50



    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_d] and player_x < WIDTH - 50:
        player_x += player_speed
    elif keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
    elif keys[pygame.K_s] and player_y < HEIGHT - 50:
        player_y += player_speed

    if wk == 4:
        wk = 0
    else:
        wk += 1

    # update and draw bullets
    for bullet in bullets:
        bullet['x'] += bullet['speed']
        pygame.draw.circle(screen, (0, 0, 255), (bullet['x'], bullet['y']), 5)

    # update and draw enemies
    for enemy in enemies:
        enemy['x'] -= enemy_speed
        screen.blit(enemy_images[enemy_wk], (enemy['x'], enemy['y']))

        # collision detection with bullets
        for bullet in bullets:
            if enemy['x'] < bullet['x'] < enemy['x'] + 50 and enemy['y'] < bullet['y'] < enemy['y'] + 50:
                enemies.remove(enemy)
                bullets.remove(bullet)

        # collision detection with player
        if enemy['x'] < player_x + 50 and enemy['x'] + 50 > player_x and enemy['y'] < player_y + 50 and enemy[
            'y'] + 50 > player_y:
            # do something when enemy collides with player
            pass

    # add new enemy
    if random.random() < 0.01:
        enemies.append({'x': WIDTH, 'y': random.randint(0, HEIGHT - 50), 'wk': random.randint(0, 4)})

    pygame.display.update()
    screen.blit(bg, (0, 0))


    if keys[pygame.K_a] and player_x > 0: # передвижение персонажа по экрану с ограничением движения
        player_x -= player_speed

    elif keys[pygame.K_d] and player_x < 800:
        player_x += player_speed

    elif keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
    elif keys[pygame.K_s] and player_y < 420:
        player_y += player_speed

    if wk == 4: # обновления анимации движения и обнуление если мы выходим за диапазон
        wk = 0
    else:
        wk += 1


    for event in pygame.event.get():# получаем список всех возможных событий
        if event.type == pygame.QUIT:# проверяем если тип переменной ивент == выходу из игры
            pygame.quit() # закрываем окно и выключаем цикл
            exit()



