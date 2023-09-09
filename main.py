import pygame

clock = pygame.time.Clock()

pygame.init() # инициализация игры


screen = pygame.display.set_mode((1000,561)) # создание разрешения экрана
pygame.display.set_caption("Звезда") # задаем название приложения
screen.fill((97, 178, 199))


icon = pygame.image.load('image/free-icon-abstract-shape-6604311.png') # подгружаем иконку
pygame.display.set_icon(icon)

bg = pygame.image.load('image/1641565350_33-www-funnyart-club-p-foni-dlya-platformerov-34.png') # создаем зандий фон

player_speed = 50
player_x = 200
player_y = 100

walk_right = [
    pygame.image.load("image/move/right1.png"),
    pygame.image.load("image/move/right2.png"),
    pygame.image.load("image/move/right3.png"), # движение игрока вправо
    pygame.image.load("image/move/right4.png"),
    pygame.image.load("image/move/right5.png"),
    pygame.image.load("image/move/right6.png"),

]
walk_left = [
    pygame.image.load("image/move/left1.png"),
    pygame.image.load("image/move/left2.png"),
    pygame.image.load("image/move/left3.png"),
    pygame.image.load("image/move/left4.png"),# движение игрока влево
    pygame.image.load("image/move/left5.png"),
    pygame.image.load("image/move/left6.png"),

]

player = pygame.image.load("image/move/Staite.png")
wk = 0
bg_x = 0
is_jump = False
up_jump = 7

while True:
    clock.tick(10)
    screen.blit(bg,(0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        screen.blit(walk_right[wk],(player_x,player_y))
    elif keys[pygame.K_a]:
        screen.blit(walk_left[wk], (player_x, player_y))
    else:
        screen.blit(player, (player_x, 100))

    if keys[pygame.K_LSHIFT]:
        player_speed = 100
    else:
        player_speed = 50
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True



    else:
        if up_jump >= -7:
            if up_jump > 0:
                player_y -= (up_jump ** 2 )/2

            else:
                player_y += (up_jump ** 2 )/2
            up_jump -= 1
        else:
            is_jump = False
            up_jump = 7


    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed

    elif keys[pygame.K_d] and player_x < 800:
        player_x += player_speed

    if wk == 5:
        wk = 0
    else:
        wk += 1
    pygame.display.update()


    bg_x -= 10
    for event in pygame.event.get():# получаем список всех возможных событий
        if event.type == pygame.QUIT:# проверяем если тип переменной ивент == выходу из игры
            pygame.quit() # закрываем окно и выключаем цикл
            exit()



