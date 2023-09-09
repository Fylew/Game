import pygame

clock = pygame.time.Clock()

pygame.init() # инициализация игры


screen = pygame.display.set_mode((1000,561)) # создание разрешения экрана
pygame.display.set_caption("Звезда") # задаем название приложения
screen.fill((97, 178, 199))


icon = pygame.image.load('image/free-icon-abstract-shape-6604311.png') # подгружаем иконку
pygame.display.set_icon(icon)

bg = pygame.image.load('image/1641565350_33-www-funnyart-club-p-foni-dlya-platformerov-34.png')


walk_right = [
    pygame.image.load("image/move/right1.png"),
    pygame.image.load("image/move/right2.png"),
    pygame.image.load("image/move/right3.png"),
    pygame.image.load("image/move/right4.png"),
    pygame.image.load("image/move/right5.png"),
    pygame.image.load("image/move/right6.png"),

]
walk_left = [
    pygame.image.load("image/move/left1.png"),
    pygame.image.load("image/move/left2.png"),
    pygame.image.load("image/move/left3.png"),
    pygame.image.load("image/move/left4.png"),
    pygame.image.load("image/move/left5.png"),
    pygame.image.load("image/move/left6.png"),

]

player = pygame.image.load("image/move/Staite.png")
wk = 0
bg_x = 0
while True:
    clock.tick(10)
    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(bg_x+1000,0))

    screen.blit(walk_right[wk],(200,100))
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



