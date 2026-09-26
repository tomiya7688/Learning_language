import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ボスを出す")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

player_x = 320
player_y = 400
player_speed = 5
player_hp = 3

bullets = []
bullet_speed = 8

enemy_speed = 1


class Enemy:
    # 敵1体ぶんの座標と発射タイマーをまとめて持つ
    def __init__(self, x, fire_interval):
        self.x = x
        self.y = -20
        self.fire_interval = fire_interval
        self.fire_timer = 0

    def move(self):
        self.y = self.y + enemy_speed

    def ready_to_fire(self):
        self.fire_timer = self.fire_timer + 1

        if self.fire_timer >= self.fire_interval:
            self.fire_timer = 0
            return True

        return False


enemies = []

spawn_positions_x = [120, 320, 520, 220, 420, 100, 540]
enemy_fire_intervals = [60, 90, 120, 75, 105, 80, 110]
spawn_interval = 90
spawn_timer = 0
spawn_index = 0
total_enemies = len(spawn_positions_x)

enemy_bullets = []
enemy_bullet_speed = 4

# ボスは最初はまだ画面に出ていません。
boss_active = False

# ボスの中心位置です。横320・縦90ピクセルに置きます。
boss_x = 320
boss_y = 90

# ボスの残りHPです。プレイヤー弾が当たるたびに1減ります。
boss_hp = 20

game_clear = False
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

    spawn_timer = spawn_timer + 1

    if spawn_timer >= spawn_interval:
        if spawn_index < len(spawn_positions_x):
            enemies.append(Enemy(spawn_positions_x[spawn_index], enemy_fire_intervals[spawn_index]))
            spawn_index = spawn_index + 1
            spawn_timer = 0

    for bullet in bullets:
        bullet[1] = bullet[1] - bullet_speed
    bullets = [bullet for bullet in bullets if bullet[1] > -20]

    for enemy in enemies:
        enemy.move()

    enemies = [enemy for enemy in enemies if enemy.y < 520]

    for enemy in enemies:
        if enemy.ready_to_fire():
            enemy_bullets.append([enemy.x, enemy.y + 20])

    for enemy_bullet in enemy_bullets:
        enemy_bullet[1] = enemy_bullet[1] + enemy_bullet_speed

    enemy_bullets = [
        enemy_bullet
        for enemy_bullet in enemy_bullets
        if enemy_bullet[1] < 500
    ]

    bullets_to_remove = []
    enemies_to_remove = []

    for bullet in bullets:
        bullet_rect = pygame.Rect(
            bullet[0] - 3,
            bullet[1] - 10,
            6,
            20
        )

        for enemy in enemies:
            enemy_rect = pygame.Rect(
                enemy.x - 20,
                enemy.y - 15,
                40,
                30
            )

            if bullet_rect.colliderect(enemy_rect):
                bullets_to_remove.append(bullet)
                enemies_to_remove.append(enemy)

        if boss_active:
            # pygame.Rect()は位置と大きさを持つ四角を用意するだけで、
            # この行だけでは画面には描きません。
            # 幅120・高さ60の半分である60・30を引いて、
            # 四角形の中心をboss_x・boss_yへ合わせます。
            boss_rect = pygame.Rect(
                boss_x - 60,
                boss_y - 30,
                120,
                60
            )

            if bullet_rect.colliderect(boss_rect):
                bullets_to_remove.append(bullet)
                boss_hp = boss_hp - 1

    for bullet in bullets_to_remove:
        if bullet in bullets:
            bullets.remove(bullet)

    for enemy in enemies_to_remove:
        if enemy in enemies:
            enemies.remove(enemy)

    if (
        spawn_index >= total_enemies
        and not enemies
        and not boss_active
    ):
        boss_active = True

    player_rect = pygame.Rect(
        player_x - 20,
        player_y - 20,
        40,
        40
    )
    enemy_bullets_to_remove = []

    for enemy_bullet in enemy_bullets:
        enemy_bullet_rect = pygame.Rect(
            enemy_bullet[0] - 4,
            enemy_bullet[1] - 8,
            8,
            16
        )

        if enemy_bullet_rect.colliderect(player_rect):
            enemy_bullets_to_remove.append(enemy_bullet)
            player_hp = player_hp - 1

    for enemy_bullet in enemy_bullets_to_remove:
        if enemy_bullet in enemy_bullets:
            enemy_bullets.remove(enemy_bullet)

    if player_hp <= 0:
        running = False

    if boss_active and boss_hp <= 0:
        game_clear = True
        running = False

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
        pygame.draw.rect(
            screen,
            (255, 100, 100),
            (enemy.x - 20, enemy.y - 15, 40, 30)
        )

    for enemy_bullet in enemy_bullets:
        pygame.draw.rect(
            screen,
            (255, 100, 180),
            (enemy_bullet[0] - 4, enemy_bullet[1] - 8, 8, 16)
        )

    if boss_active:
        # screenへ、RGB(180, 80, 255)の紫系の色でボスを描きます。
        # 左上を中心座標から60px左、30px上へずらし、
        # 幅120・高さ60の四角形の中心をboss_x・boss_yへ合わせます。
        pygame.draw.rect(
            screen,
            (180, 80, 255),
            (boss_x - 60, boss_y - 30, 120, 60)
        )

        # ボスHPの文章から白い文字画像を作ります。
        # Trueは文字の縁を滑らかにする指定です。
        boss_text = font.render(
            f"BOSS HP: {boss_hp}",
            True,
            (255, 255, 255)
        )

        # 作った文字画像の左上を、画面の左220・上10ピクセルへ置いて描きます。
        screen.blit(boss_text, (220, 10))

    hp_text = font.render(
        f"HP: {player_hp}",
        True,
        (255, 255, 255)
    )
    screen.blit(hp_text, (10, 10))

    # このフレームで描いたボスや文字を含む内容を画面へ反映します。
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

if game_clear:
    print("GAME CLEAR")
