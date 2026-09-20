import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("プレイヤーを表示する")

clock = pygame.time.Clock()

player_x = 320
player_y = 400

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
