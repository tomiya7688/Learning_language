from pathlib import Path

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ゲームオーバー画面を作る")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
clear_font = pygame.font.Font(None, 72)
clear_sub_font = pygame.font.Font(None, 32)
button_font = pygame.font.Font(None, 40)
menu_font = pygame.font.Font(None, 64)

# この.pyと同じPg18フォルダから、同梱背景画像を読み込む
background_path = (
    Path(__file__).parent
    / "assets"
    / "space_background.png"
)
background_image = pygame.image.load(
    str(background_path)
).convert()

# 教材用素材は160x120なので、ゲーム画面の640x480へ拡大する
background_image = pygame.transform.scale(
    background_image,
    (640, 480)
)


# 自機・通常敵・ボスも同梱PNGから読み込む
assets_path = Path(__file__).parent / "assets"

player_image = pygame.image.load(
    str(assets_path / "player_ship.png")
).convert_alpha()

enemy_image = pygame.image.load(
    str(assets_path / "enemy_ship.png")
).convert_alpha()

boss_image = pygame.image.load(
    str(assets_path / "boss_ship.png")
).convert_alpha()

# 同じ背景を上下に2枚並べて、切れ目なく流す
background_y_1 = 0
background_y_2 = -480
background_speed = 2

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

boss_active = False
boss_x = 320
boss_y = 90
boss_hp = 50

boss_bullets = []
boss_bullet_speed = 4
boss_fire_interval = 120
boss_fire_timer = 0
boss_bullet_width = 48
boss_bullet_height = 48

game_state = "playing"

# pygameのボタンは、まず「クリックできる四角」をRectで用意する
back_button = pygame.Rect(220, 330, 200, 60)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if (
                event.key == pygame.K_SPACE
                and game_state == "playing"
            ):
                bullets.append([player_x, player_y - 20])

        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and game_state == "clear"
        ):
            if back_button.collidepoint(event.pos):
                game_state = "menu"

    # クリア中は、敵や弾の更新を止めて専用画面だけを描く
    if game_state == "clear":
        screen.fill((8, 8, 24))

        clear_text = clear_font.render(
            "GAME CLEAR!",
            True,
            (255, 240, 100)
        )
        clear_text_rect = clear_text.get_rect(
            center=(320, 210)
        )
        screen.blit(clear_text, clear_text_rect)

        clear_sub_text = clear_sub_font.render(
            "You defeated the boss!",
            True,
            (255, 255, 255)
        )
        clear_sub_text_rect = clear_sub_text.get_rect(
            center=(320, 275)
        )
        screen.blit(clear_sub_text, clear_sub_text_rect)

        # Rectを描いて、その上にBACKという文字を置く
        pygame.draw.rect(
            screen,
            (70, 90, 180),
            back_button,
            border_radius=8
        )

        back_text = button_font.render(
            "BACK",
            True,
            (255, 255, 255)
        )
        back_text_rect = back_text.get_rect(
            center=back_button.center
        )
        screen.blit(back_text, back_text_rect)

        pygame.display.flip()
        clock.tick(60)
        continue

    # HPが0になったら、敵や弾の更新を止めてゲームオーバー画面だけを描く
    if game_state == "game_over":
        screen.fill((28, 8, 12))

        game_over_text = clear_font.render(
            "GAME OVER",
            True,
            (255, 90, 90)
        )
        game_over_text_rect = game_over_text.get_rect(
            center=(320, 220)
        )
        screen.blit(game_over_text, game_over_text_rect)

        game_over_sub_text = clear_sub_font.render(
            "Your HP reached 0.",
            True,
            (255, 255, 255)
        )
        game_over_sub_text_rect = game_over_sub_text.get_rect(
            center=(320, 280)
        )
        screen.blit(
            game_over_sub_text,
            game_over_sub_text_rect
        )

        pygame.display.flip()
        clock.tick(60)
        continue

    # タイトル画面はまだ作っていないので、戻り先は仮のMENU画面
    if game_state == "menu":
        screen.fill((18, 18, 30))

        menu_text = menu_font.render(
            "MENU",
            True,
            (255, 255, 255)
        )
        menu_text_rect = menu_text.get_rect(
            center=(320, 220)
        )
        screen.blit(menu_text, menu_text_rect)

        menu_sub_text = clear_sub_font.render(
            "This is a temporary screen.",
            True,
            (190, 190, 210)
        )
        menu_sub_text_rect = menu_sub_text.get_rect(
            center=(320, 280)
        )
        screen.blit(menu_sub_text, menu_sub_text_rect)

        pygame.display.flip()
        clock.tick(60)
        continue

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

    # 背景画像2枚を毎フレーム下へ動かす
    background_y_1 = background_y_1 + background_speed
    background_y_2 = background_y_2 + background_speed

    # 画面下へ出た画像を、もう1枚の上へつなぎ直す
    if background_y_1 >= 480:
        background_y_1 = background_y_2 - 480

    if background_y_2 >= 480:
        background_y_2 = background_y_1 - 480

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
            enemy_rect = enemy_image.get_rect(
                center=(enemy.x, enemy.y)
            )

            if bullet_rect.colliderect(enemy_rect):
                bullets_to_remove.append(bullet)
                enemies_to_remove.append(enemy)

        if boss_active:
            boss_rect = boss_image.get_rect(
                center=(boss_x, boss_y)
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
        bullets.clear()

    if boss_active:
        boss_fire_timer = boss_fire_timer + 1

        if boss_fire_timer >= boss_fire_interval:
            boss_bullets.append([boss_x, boss_y + 40])
            boss_fire_timer = 0

    for boss_bullet in boss_bullets:
        boss_bullet[1] = boss_bullet[1] + boss_bullet_speed

    boss_bullets = [
        boss_bullet
        for boss_bullet in boss_bullets
        if boss_bullet[1] < 520
    ]

    player_rect = player_image.get_rect(
        center=(player_x, player_y)
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

    boss_bullets_to_remove = []

    for boss_bullet in boss_bullets:
        boss_bullet_rect = pygame.Rect(
            boss_bullet[0] - boss_bullet_width // 2,
            boss_bullet[1],
            boss_bullet_width,
            boss_bullet_height
        )

        if boss_bullet_rect.colliderect(player_rect):
            boss_bullets_to_remove.append(boss_bullet)
            player_hp = player_hp - 1

    for boss_bullet in boss_bullets_to_remove:
        if boss_bullet in boss_bullets:
            boss_bullets.remove(boss_bullet)

    if player_hp <= 0:
        game_state = "game_over"
    elif boss_active and boss_hp <= 0:
        game_state = "clear"

    # 背景画像はプレイヤーや敵より先に描く
    screen.blit(background_image, (0, background_y_1))
    screen.blit(background_image, (0, background_y_2))

    player_image_rect = player_image.get_rect(
        center=(player_x, player_y)
    )
    screen.blit(player_image, player_image_rect)

    for bullet in bullets:
        pygame.draw.rect(
            screen,
            (255, 240, 100),
            (bullet[0] - 3, bullet[1] - 10, 6, 20)
        )

    for enemy in enemies:
        enemy_image_rect = enemy_image.get_rect(
            center=(enemy.x, enemy.y)
        )
        screen.blit(enemy_image, enemy_image_rect)

    for enemy_bullet in enemy_bullets:
        pygame.draw.rect(
            screen,
            (255, 100, 180),
            (enemy_bullet[0] - 4, enemy_bullet[1] - 8, 8, 16)
        )

    if boss_active:
        boss_image_rect = boss_image.get_rect(
            center=(boss_x, boss_y)
        )
        screen.blit(boss_image, boss_image_rect)

        for boss_bullet in boss_bullets:
            pygame.draw.rect(
                screen,
                (255, 80, 80),
                (
                    boss_bullet[0] - boss_bullet_width // 2,
                    boss_bullet[1],
                    boss_bullet_width,
                    boss_bullet_height
                )
            )

        boss_text = font.render(
            f"BOSS HP: {boss_hp}",
            True,
            (255, 255, 255)
        )
        screen.blit(boss_text, (220, 10))

    hp_text = font.render(
        f"HP: {player_hp}",
        True,
        (255, 255, 255)
    )
    screen.blit(hp_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
