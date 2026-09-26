import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("敵を実装する")

clock = pygame.time.Clock()

player_x = 320
player_y = 400
player_speed = 5

bullets = []
bullet_speed = 8

enemies = [
    [160, 80],
    [320, 40],
    [480, 100]
]
enemy_speed = 1

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

    for enemy in enemies:
        enemy[1] = enemy[1] + enemy_speed

    bullets_to_remove = []
    enemies_to_remove = []

    for bullet in bullets:
        # Rectは画面へ描かず、弾の位置と大きさを持つ四角を用意します。
        # 幅6・高さ20の中心をbulletの座標へ合わせます。
        bullet_rect = pygame.Rect(
            bullet[0] - 3,
            bullet[1] - 10,
            6,
            20
        )

        for enemy in enemies:
            # enemyは敵1体です。幅40・高さ30の中心をenemyの座標へ合わせます。
            # pygame.Rect()は四角を用意するだけで、ここではまだ描画しません。
            enemy_rect = pygame.Rect(
                enemy[0] - 20,
                enemy[1] - 15,
                40,
                30
            )

            # 弾の四角と敵の四角が重なればTrueになり、ifの中を実行します。
            if bullet_rect.colliderect(enemy_rect):
                bullets_to_remove.append(bullet)
                enemies_to_remove.append(enemy)

    for bullet in bullets_to_remove:
        if bullet in bullets:
            bullets.remove(bullet)

    for enemy in enemies_to_remove:
        if enemy in enemies:
            enemies.remove(enemy)

    screen.fill((10, 10, 30))

    player_points = [
        (player_x, player_y - 20),
        (player_x - 20, player_y + 20),
        (player_x + 20, player_y + 20)
    ]

    pygame.draw.polygon(screen, (100, 200, 255), player_points)

    for bullet in bullets:
        pygame.draw.rect(
            screen,
            (255, 240, 100),
            (bullet[0] - 3, bullet[1] - 10, 6, 20)
        )

    for enemy in enemies:
        # RGB(255, 100, 100)の赤系の色で、幅40・高さ30の敵を描きます。
        # 左上を中心座標から20px左、15px上へずらして中心を合わせます。
        pygame.draw.rect(
            screen,
            (255, 100, 100),
            (enemy[0] - 20, enemy[1] - 15, 40, 30)
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
