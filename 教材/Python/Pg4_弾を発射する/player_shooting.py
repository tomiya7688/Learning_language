import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("弾を発射する")

clock = pygame.time.Clock()

player_x = 320
player_y = 400
player_speed = 5

bullets = []
bullet_speed = 8

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x, player_y - 20])

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

    for bullet in bullets:
        bullet[1] = bullet[1] - bullet_speed

    bullets = [bullet for bullet in bullets if bullet[1] > -20]

    # ゲーム画面全体を暗く青みのある色で塗ります。
    screen.fill((10, 10, 30))

    player_points = [
        (player_x, player_y - 20),
        (player_x - 20, player_y + 20),
        (player_x + 20, player_y + 20)
    ]

    pygame.draw.polygon(screen, (100, 200, 255), player_points)

    for bullet in bullets:
        # bullet[0]は弾の横位置、bullet[1]は縦位置です。
        # 幅6・高さ20の中心を弾の座標へ合わせて四角形を描きます。
        pygame.draw.rect(
            screen,
            (255, 240, 100),
            (bullet[0] - 3, bullet[1] - 10, 6, 20)
        )

    # このフレームで描いた内容を画面へ反映します。
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
