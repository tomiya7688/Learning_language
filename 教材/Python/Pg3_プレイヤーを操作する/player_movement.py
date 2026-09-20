import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("プレイヤーを操作する")

clock = pygame.time.Clock()

player_x = 320
player_y = 400
player_speed = 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x = player_x - player_speed

    if keys[pygame.K_RIGHT]:
        player_x = player_x + player_speed

    if keys[pygame.K_UP]:
        player_y = player_y - player_speed

    if keys[pygame.K_DOWN]:
        player_y = player_y + player_speed

    player_x = max(20, min(620, player_x))
    player_y = max(20, min(460, player_y))

    screen.fill((10, 10, 30))

    player_points = [
        (player_x, player_y - 20),
        (player_x - 20, player_y + 20),
        (player_x + 20, player_y + 20)
    ]

    pygame.draw.polygon(screen, (100, 200, 255), player_points)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
