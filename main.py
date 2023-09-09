import pygame

clock = pygame.time.Clock() # инициализируем часы

pygame.init() # инициализация игры


screen = pygame.display.set_mode((1000,561)) # создание разрешения экрана
pygame.display.set_caption("Звезда") # задаем название приложения
screen.fill((97, 178, 199))


icon = pygame.image.load('image/free-icon-abstract-shape-6604311.png') # подгружаем иконку
pygame.display.set_icon(icon) # устанавливаем эту иконку для игры

bg = pygame.image.load('image/1641565350_33-www-funnyart-club-p-foni-dlya-platformerov-34.png') # создаем зандий фон

player_speed = 50 # скорость движения персонажа
player_x = 200 # координаты по x
player_y = 100 # координаты по Y

walk_right = [
    pygame.image.load("image/move/right1.png"),
    pygame.image.load("image/move/right2.png"),
    pygame.image.load("image/move/right3.png"), # движение игрока вправо
    pygame.image.load("image/move/right4.png"),
    pygame.image.load("image/move/right5.png"),


]
walk_left = [
    pygame.image.load("image/move/left1.png"),
    pygame.image.load("image/move/left2.png"),
    pygame.image.load("image/move/left3.png"),
    pygame.image.load("image/move/left4.png"),# движение игрока влево
    pygame.image.load("image/move/left5.png"),


]


wk = 0 # счетчик для движения персонажа , он меняется на 1 за тик и сменяет картинки
bg_x = 0 # движение заднего фона
is_jump = False # переменная для отслеживания прыжка
up_jump = 7 # высота прыжка

while True: # цикл для основной игры
    clock.tick(15) # обмен кадров
    screen.blit(bg,(0,0)) # создание заднего фона в координатах 0
    keys = pygame.key.get_pressed() # отслеживание нажатия
    if keys[pygame.K_d]: # проверка если нажали d то запускаем анимацию движения вправо
        screen.blit(walk_right[wk],(player_x,player_y))
    elif keys[pygame.K_a]: # если нажали А то запускаем движение анимации влево
        screen.blit(walk_left[wk], (player_x, player_y))
    else: # в противном случае анимация остановки
        screen.blit(walk_right[wk], (player_x, player_y))

    if keys[pygame.K_LSHIFT]: # если нажали шифт то ускорение в 2 раза
        player_speed = 100
    else:
        player_speed = 50


    if not is_jump: # прописывание логики работы прыжка
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
    pygame.display.update() # обновление событий на экране

    for event in pygame.event.get():# получаем список всех возможных событий
        if event.type == pygame.QUIT:# проверяем если тип переменной ивент == выходу из игры
            pygame.quit() # закрываем окно и выключаем цикл
            exit()



