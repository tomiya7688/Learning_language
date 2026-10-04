# Path をインポートする
from pathlib import Path

# pygame をインポートする
import pygame

# pygame を初期化する
pygame.init()

# screen に640×480のpygame画面をセットする
screen = pygame.display.set_mode((640, 480))
# pygame画面のタイトルに「始めるボタンを作る」をセットする
pygame.display.set_caption("始めるボタンを作る")

# 画面更新の間隔を調整する時計を用意する（後でclock.tick(60)に使う）
clock = pygame.time.Clock()
# Noneで同梱のFreeSans Boldを選び、自機とボスのHP表示用にサイズ36（ピクセル単位）を指定する
font = pygame.font.Font(None, 36)

# Noneで同梱のFreeSans Boldを選び、クリア・ゲームオーバーの見出し用にサイズ72（ピクセル単位）を指定する
clear_font = pygame.font.Font(None, 72)

# Noneで同梱のFreeSans Boldを選び、画面の説明文用にサイズ32（ピクセル単位）を指定する
clear_sub_font = pygame.font.Font(None, 32)
# Noneで同梱のFreeSans Boldを選び、ボタンの文字用にサイズ40（ピクセル単位）を指定する
button_font = pygame.font.Font(None, 40)
# Noneで同梱のFreeSans Boldを選び、タイトルの見出し用にサイズ64（ピクセル単位）を指定する
menu_font = pygame.font.Font(None, 64)

# background_path に Path(__file__).parent / "assets" / "space_background.png" をセットする
background_path = (
    Path(__file__).parent
    / "assets"
    / "space_background.png"
)
# background_image に pygame.image.load(str(background_path)).convert() をセットする
background_image = pygame.image.load(
    str(background_path)
).convert()

# background_image に pygame.transform.scale(background_image, (640, 480)) をセットする
background_image = pygame.transform.scale(
    background_image,
    (640, 480)
)


# assets_path に Path(__file__).parent / "assets" をセットする
assets_path = Path(__file__).parent / "assets"

# player_image に pygame.image.load(str(assets_path / "player_ship.png")).convert_alpha() をセットする
player_image = pygame.image.load(
    str(assets_path / "player_ship.png")
).convert_alpha()

# enemy_image に pygame.image.load(str(assets_path / "enemy_ship.png")).convert_alpha() をセットする
enemy_image = pygame.image.load(
    str(assets_path / "enemy_ship.png")
).convert_alpha()

# boss_image に pygame.image.load(str(assets_path / "boss_ship.png")).convert_alpha() をセットする
boss_image = pygame.image.load(
    str(assets_path / "boss_ship.png")
).convert_alpha()

# background_y_1 に0を入れる
background_y_1 = 0
# background_y_2 に-480を入れる
background_y_2 = -480
# background_speed に2を入れる
background_speed = 2

# player_x に320を入れる
player_x = 320
# player_y に400を入れる
player_y = 400
# player_speed に5を入れる
player_speed = 5
# player_hp に3を入れる
player_hp = 3

# bullets に空のリストを入れる
bullets = []
# bullet_speed に8を入れる
bullet_speed = 8

# enemy_speed に1を入れる
enemy_speed = 1


# Enemy クラスを定義する
class Enemy:
    # __init__ を定義する
    def __init__(self, x, fire_interval):
        # self.x に x を入れる
        self.x = x
        # self.y に -20 を入れる
        self.y = -20
        # self.fire_interval に fire_interval を入れる
        self.fire_interval = fire_interval
        # self.fire_timer に0を入れる
        self.fire_timer = 0

    # move を定義する
    def move(self):
        # self.y に self.y と enemy_speed を足した値を入れる
        self.y = self.y + enemy_speed

    # ready_to_fire を定義する
    def ready_to_fire(self):
        # self.fire_timer に self.fire_timer と1を足した値を入れる
        self.fire_timer = self.fire_timer + 1

        # self.fire_timer が self.fire_interval 以上なら
        if self.fire_timer >= self.fire_interval:
            # self.fire_timer に0を入れる
            self.fire_timer = 0
            # True を返す
            return True

        # False を返す
        return False


# enemies に空のリストを入れる
enemies = []

# spawn_positions_x に120、320、520、220、420、100、540を入れる
spawn_positions_x = [120, 320, 520, 220, 420, 100, 540]
# enemy_fire_intervals に60、90、120、75、105、80、110を入れる
enemy_fire_intervals = [60, 90, 120, 75, 105, 80, 110]
# spawn_interval に90を入れる
spawn_interval = 90
# spawn_timer に0を入れる
spawn_timer = 0
# spawn_index に0を入れる
spawn_index = 0
# total_enemies に len(spawn_positions_x) をセットする
total_enemies = len(spawn_positions_x)

# enemy_bullets に空のリストを入れる
enemy_bullets = []
# enemy_bullet_speed に4を入れる
enemy_bullet_speed = 4

# boss_active に False を入れる
boss_active = False
# boss_x に320を入れる
boss_x = 320
# boss_y に90を入れる
boss_y = 90
# boss_hp に50を入れる
boss_hp = 50

# boss_bullets に空のリストを入れる
boss_bullets = []
# boss_bullet_speed に4を入れる
boss_bullet_speed = 4
# boss_fire_interval に120を入れる
boss_fire_interval = 120
# boss_fire_timer に0を入れる
boss_fire_timer = 0
# boss_bullet_width に48を入れる
boss_bullet_width = 48
# boss_bullet_height に48を入れる
boss_bullet_height = 48

# game_state に "title" をセットする
game_state = "title"

# back_button に pygame.Rect(220, 330, 200, 60) をセットする
back_button = pygame.Rect(220, 330, 200, 60)
# restart_button に pygame.Rect(220, 330, 200, 60) をセットする
restart_button = pygame.Rect(220, 330, 200, 60)
# start_button に pygame.Rect(220, 330, 200, 60) をセットする
start_button = pygame.Rect(220, 330, 200, 60)

# running に True を入れる
running = True

# running が True の間、繰り返す
while running:
    # pygameで起きたイベントを1つずつ event に入れて繰り返す
    for event in pygame.event.get():
        # event.type が pygame.QUIT なら
        if event.type == pygame.QUIT:
            # running に False を入れる
            running = False

        # event.type が pygame.KEYDOWN なら
        if event.type == pygame.KEYDOWN:
            # event.key が pygame.K_SPACE で game_state が "playing" なら
            if (
                event.key == pygame.K_SPACE
                and game_state == "playing"
            ):
                # bullets に [player_x, player_y - 20] を追加する
                bullets.append([player_x, player_y - 20])

        # 左クリックでタイトル画面の start_button を押したなら
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and game_state == "title"
        ):
            # start_button.collidepoint(event.pos) が True なら
            if start_button.collidepoint(event.pos):
                # background_y_1 に0を入れる
                background_y_1 = 0
                # background_y_2 に-480を入れる
                background_y_2 = -480
                # player_x に320を入れる
                player_x = 320
                # player_y に400を入れる
                player_y = 400
                # player_hp に3を入れる
                player_hp = 3
                # bullets に空のリストを入れる
                bullets = []
                # enemies に空のリストを入れる
                enemies = []
                # spawn_timer に0を入れる
                spawn_timer = 0
                # spawn_index に0を入れる
                spawn_index = 0
                # enemy_bullets に空のリストを入れる
                enemy_bullets = []
                # boss_active に False を入れる
                boss_active = False
                # boss_hp に50を入れる
                boss_hp = 50
                # boss_bullets に空のリストを入れる
                boss_bullets = []
                # boss_fire_timer に0を入れる
                boss_fire_timer = 0
                # game_state に "playing" をセットする
                game_state = "playing"

        # event.type が pygame.MOUSEBUTTONDOWN で event.button が1で game_state が "clear" なら
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and game_state == "clear"
        ):
            # back_button.collidepoint(event.pos) が True なら
            if back_button.collidepoint(event.pos):
                # game_state に "title" をセットする
                game_state = "title"

        # event.type が pygame.MOUSEBUTTONDOWN で event.button が1で game_state が "game_over" なら
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and game_state == "game_over"
        ):
            # restart_button.collidepoint(event.pos) が True なら
            if restart_button.collidepoint(event.pos):
                # background_y_1 に0を入れる
                background_y_1 = 0
                # background_y_2 に-480を入れる
                background_y_2 = -480
                # player_x に320を入れる
                player_x = 320
                # player_y に400を入れる
                player_y = 400
                # player_hp に3を入れる
                player_hp = 3
                # bullets に空のリストを入れる
                bullets = []
                # enemies に空のリストを入れる
                enemies = []
                # spawn_timer に0を入れる
                spawn_timer = 0
                # spawn_index に0を入れる
                spawn_index = 0
                # enemy_bullets に空のリストを入れる
                enemy_bullets = []
                # boss_active に False を入れる
                boss_active = False
                # boss_hp に50を入れる
                boss_hp = 50
                # boss_bullets に空のリストを入れる
                boss_bullets = []
                # boss_fire_timer に0を入れる
                boss_fire_timer = 0
                # game_state に "playing" をセットする
                game_state = "playing"

    # game_state が "clear" なら
    if game_state == "clear":
        # screen に (8, 8, 24) を使った色を塗る
        screen.fill((8, 8, 24))

        # clear_text に clear_font.render("GAME CLEAR!", True, (255, 240, 100)) をセットする
        clear_text = clear_font.render(
            "GAME CLEAR!",
            True,
            (255, 240, 100)
        )
        # clear_text_rect に clear_text.get_rect(center=(320, 210)) をセットする
        clear_text_rect = clear_text.get_rect(
            center=(320, 210)
        )
        # screen.blit(clear_text, clear_text_rect) を実行する
        screen.blit(clear_text, clear_text_rect)

        # clear_sub_text に clear_sub_font.render("You defeated the boss!", True, (255, 255, 255)) をセットする
        clear_sub_text = clear_sub_font.render(
            "You defeated the boss!",
            True,
            (255, 255, 255)
        )
        # clear_sub_text_rect に clear_sub_text.get_rect(center=(320, 275)) をセットする
        clear_sub_text_rect = clear_sub_text.get_rect(
            center=(320, 275)
        )
        # screen.blit(clear_sub_text, clear_sub_text_rect) を実行する
        screen.blit(clear_sub_text, clear_sub_text_rect)

        # screen に (70, 90, 180) の back_button を角の半径8で描く
        pygame.draw.rect(
            screen,
            (70, 90, 180),
            back_button,
            border_radius=8
        )

        # back_text に button_font.render("BACK", True, (255, 255, 255)) をセットする
        back_text = button_font.render(
            "BACK",
            True,
            (255, 255, 255)
        )
        # back_text_rect に back_text.get_rect(center=back_button.center) をセットする
        back_text_rect = back_text.get_rect(
            center=back_button.center
        )
        # screen.blit(back_text, back_text_rect) を実行する
        screen.blit(back_text, back_text_rect)

        # このフレームの描画内容を画面に反映する
        pygame.display.flip()
        # 1秒間に60回を上限にして clock を進める
        clock.tick(60)
        # 次のループへ進む
        continue

    # game_state が "game_over" なら
    if game_state == "game_over":
        # screen に (28, 8, 12) を使った色を塗る
        screen.fill((28, 8, 12))

        # game_over_text に clear_font.render("GAME OVER", True, (255, 90, 90)) をセットする
        game_over_text = clear_font.render(
            "GAME OVER",
            True,
            (255, 90, 90)
        )

        # game_over_text_rect に game_over_text.get_rect(center=(320, 220)) をセットする
        game_over_text_rect = game_over_text.get_rect(
            center=(320, 220)
        )

        # screen.blit(game_over_text, game_over_text_rect) を実行する
        screen.blit(game_over_text, game_over_text_rect)

        # game_over_sub_text に clear_sub_font.render("Your HP reached 0.", True, (255, 255, 255)) をセットする
        game_over_sub_text = clear_sub_font.render(
            "Your HP reached 0.",
            True,
            (255, 255, 255)
        )
        # game_over_sub_text_rect に game_over_sub_text.get_rect(center=(320, 280)) をセットする
        game_over_sub_text_rect = game_over_sub_text.get_rect(
            center=(320, 280)
        )
        # screen.blit(game_over_sub_text, game_over_sub_text_rect) を実行する
        screen.blit(
            game_over_sub_text,
            game_over_sub_text_rect
        )

        # screen に (70, 150, 90) の restart_button を角の半径8で描く
        pygame.draw.rect(
            screen,
            (70, 150, 90),
            restart_button,
            border_radius=8
        )

        # restart_text に button_font.render("RESTART", True, (255, 255, 255)) をセットする
        restart_text = button_font.render(
            "RESTART",
            True,
            (255, 255, 255)
        )
        # restart_text_rect に restart_text.get_rect(center=restart_button.center) をセットする
        restart_text_rect = restart_text.get_rect(
            center=restart_button.center
        )
        # screen.blit(restart_text, restart_text_rect) を実行する
        screen.blit(restart_text, restart_text_rect)

        # このフレームの描画内容を画面に反映する
        pygame.display.flip()
        # 1秒間に60回を上限にして clock を進める
        clock.tick(60)
        # 次のループへ進む
        continue

    # game_state が "title" なら
    if game_state == "title":
        # screen に (18, 18, 30) を使った色を塗る
        screen.fill((18, 18, 30))

        # title_text に menu_font.render("SPACE SHOOTER", True, (255, 255, 255)) をセットする
        title_text = menu_font.render(
            "SPACE SHOOTER",
            True,
            (255, 255, 255)
        )
        # title_text_rect に title_text.get_rect(center=(320, 220)) をセットする
        title_text_rect = title_text.get_rect(
            center=(320, 220)
        )
        # screen.blit(title_text, title_text_rect) を実行する
        screen.blit(title_text, title_text_rect)

        # title_sub_text に clear_sub_font.render("Defeat the boss!", True, (190, 190, 210)) をセットする
        title_sub_text = clear_sub_font.render(
            "Defeat the boss!",
            True,
            (190, 190, 210)
        )
        # title_sub_text_rect に title_sub_text.get_rect(center=(320, 280)) をセットする
        title_sub_text_rect = title_sub_text.get_rect(
            center=(320, 280)
        )
        # screen.blit(title_sub_text, title_sub_text_rect) を実行する
        screen.blit(title_sub_text, title_sub_text_rect)

        # screen に (70, 110, 190) の start_button を角の半径8で描く
        pygame.draw.rect(
            screen,
            (70, 110, 190),
            start_button,
            border_radius=8
        )

        # start_text に button_font.render("START", True, (255, 255, 255)) をセットする
        start_text = button_font.render(
            "START",
            True,
            (255, 255, 255)
        )
        # start_text_rect に start_text.get_rect(center=start_button.center) をセットする
        start_text_rect = start_text.get_rect(
            center=start_button.center
        )
        # screen.blit(start_text, start_text_rect) を実行する
        screen.blit(start_text, start_text_rect)

    # このフレームの描画内容を画面に反映する
        pygame.display.flip()
    # 1秒間に60回を上限にして clock を進める
        clock.tick(60)
        # 次のループへ進む
        continue

    # keys に pygame.key.get_pressed() の戻り値を入れる
    keys = pygame.key.get_pressed()

    # keys[pygame.K_LEFT] が True なら
    if keys[pygame.K_LEFT]:
        # player_x に player_x から player_speed を引いた値を入れる
        player_x = player_x - player_speed
    # keys[pygame.K_RIGHT] が True なら
    if keys[pygame.K_RIGHT]:
        # player_x に player_x と player_speed を足した値を入れる
        player_x = player_x + player_speed
    # keys[pygame.K_UP] が True なら
    if keys[pygame.K_UP]:
        # player_y に player_y から player_speed を引いた値を入れる
        player_y = player_y - player_speed
    # keys[pygame.K_DOWN] が True なら
    if keys[pygame.K_DOWN]:
        # player_y に player_y と player_speed を足した値を入れる
        player_y = player_y + player_speed

    # player_x に max(20, min(620, player_x)) の値を入れる
    player_x = max(20, min(620, player_x))
    # player_y に max(20, min(460, player_y)) の値を入れる
    player_y = max(20, min(460, player_y))

    # background_y_1 に background_y_1 と background_speed を足した値を入れる
    background_y_1 = background_y_1 + background_speed
    # background_y_2 に background_y_2 と background_speed を足した値を入れる
    background_y_2 = background_y_2 + background_speed

    # background_y_1 が480以上なら
    if background_y_1 >= 480:
        # background_y_1 に background_y_2 から480を引いた値を入れる
        background_y_1 = background_y_2 - 480

    # background_y_2 が480以上なら
    if background_y_2 >= 480:
        # background_y_2 に background_y_1 から480を引いた値を入れる
        background_y_2 = background_y_1 - 480

    # spawn_timer に spawn_timer と1を足した値を入れる
    spawn_timer = spawn_timer + 1
    # spawn_timer が spawn_interval 以上なら
    if spawn_timer >= spawn_interval:
        # spawn_index が len(spawn_positions_x) より小さいなら
        if spawn_index < len(spawn_positions_x):
            # enemies に Enemy(spawn_positions_x[spawn_index], enemy_fire_intervals[spawn_index]) を追加する
            enemies.append(Enemy(spawn_positions_x[spawn_index], enemy_fire_intervals[spawn_index]))
            # spawn_index に spawn_index と1を足した値を入れる
            spawn_index = spawn_index + 1
            # spawn_timer に0を入れる
            spawn_timer = 0

    # bullets から bullet を1つずつ取り出して繰り返す
    for bullet in bullets:
        # bullet[1] に bullet[1] から bullet_speed を引いた値を入れる
        bullet[1] = bullet[1] - bullet_speed
    # bullets に bullet[1] > -20 の bullet だけを入れる
    bullets = [bullet for bullet in bullets if bullet[1] > -20]

    # enemies から enemy を1つずつ取り出して繰り返す
    for enemy in enemies:
        # enemy.move() を実行する
        enemy.move()
    # enemies に enemy.y < 520 の enemy だけを入れる
    enemies = [enemy for enemy in enemies if enemy.y < 520]

    # enemies から enemy を1つずつ取り出して繰り返す
    for enemy in enemies:
        # enemy.ready_to_fire() が True なら
        if enemy.ready_to_fire():
            # enemy_bullets に [enemy.x, enemy.y + 20] を追加する
            enemy_bullets.append([enemy.x, enemy.y + 20])

    # enemy_bullets から enemy_bullet を1つずつ取り出して繰り返す
    for enemy_bullet in enemy_bullets:
        # enemy_bullet[1] に enemy_bullet[1] と enemy_bullet_speed を足した値を入れる
        enemy_bullet[1] = enemy_bullet[1] + enemy_bullet_speed

    # enemy_bullets に enemy_bullet[1] < 500 の enemy_bullet だけを入れる
    enemy_bullets = [
        enemy_bullet
        for enemy_bullet in enemy_bullets
        if enemy_bullet[1] < 500
    ]

    # bullets_to_remove に空のリストを入れる
    bullets_to_remove = []
    # enemies_to_remove に空のリストを入れる
    enemies_to_remove = []

    # bullets から bullet を1つずつ取り出して繰り返す
    for bullet in bullets:
        # bullet_rect に pygame.Rect(bullet[0] - 3, bullet[1] - 10, 6, 20) をセットする
        bullet_rect = pygame.Rect(
            bullet[0] - 3,
            bullet[1] - 10,
            6,
            20
        )

        # enemies から enemy を1つずつ取り出して繰り返す
        for enemy in enemies:
            # enemy_rect に enemy_image.get_rect(center=(enemy.x, enemy.y)) をセットする
            enemy_rect = enemy_image.get_rect(
                center=(enemy.x, enemy.y)
            )

            # bullet_rect.colliderect(enemy_rect) が True なら
            if bullet_rect.colliderect(enemy_rect):
                # bullets_to_remove に bullet を追加する
                bullets_to_remove.append(bullet)
                # enemies_to_remove に enemy を追加する
                enemies_to_remove.append(enemy)

        # boss_active が True なら
        if boss_active:
            # boss_rect に boss_image.get_rect(center=(boss_x, boss_y)) をセットする
            boss_rect = boss_image.get_rect(
                center=(boss_x, boss_y)
            )

            # bullet_rect.colliderect(boss_rect) が True なら
            if bullet_rect.colliderect(boss_rect):
                # bullets_to_remove に bullet を追加する
                bullets_to_remove.append(bullet)
                # boss_hp に boss_hp から1を引いた値を入れる
                boss_hp = boss_hp - 1

    # bullets_to_remove から bullet を1つずつ取り出して繰り返す
    for bullet in bullets_to_remove:
        # bullet が bullets に含まれているなら
        if bullet in bullets:
            # bullets から bullet を削除する
            bullets.remove(bullet)

    # enemies_to_remove から enemy を1つずつ取り出して繰り返す
    for enemy in enemies_to_remove:
        # enemy が enemies に含まれているなら
        if enemy in enemies:
            # enemies から enemy を削除する
            enemies.remove(enemy)

    # spawn_index が total_enemies 以上で、enemies が空で、boss_active が False なら
    if (
        spawn_index >= total_enemies
        and not enemies
        and not boss_active
    ):
        # boss_active に True を入れる
        boss_active = True
        # bullets を空にする
        bullets.clear()

    # boss_active が True なら
    if boss_active:
        # boss_fire_timer に boss_fire_timer と1を足した値を入れる
        boss_fire_timer = boss_fire_timer + 1

        # boss_fire_timer が boss_fire_interval 以上なら
        if boss_fire_timer >= boss_fire_interval:
            # boss_bullets に [boss_x, boss_y + 40] を追加する
            boss_bullets.append([boss_x, boss_y + 40])
            # boss_fire_timer に0を入れる
            boss_fire_timer = 0

    # boss_bullets から boss_bullet を1つずつ取り出して繰り返す
    for boss_bullet in boss_bullets:
        # boss_bullet[1] に boss_bullet[1] と boss_bullet_speed を足した値を入れる
        boss_bullet[1] = boss_bullet[1] + boss_bullet_speed

    # boss_bullets に boss_bullet[1] < 520 の boss_bullet だけを入れる
    boss_bullets = [
        boss_bullet
        for boss_bullet in boss_bullets
        if boss_bullet[1] < 520
    ]

    # player_rect に player_image.get_rect(center=(player_x, player_y)) をセットする
    player_rect = player_image.get_rect(
        center=(player_x, player_y)
    )

    # enemy_bullets_to_remove に空のリストを入れる
    enemy_bullets_to_remove = []

    # enemy_bullets から enemy_bullet を1つずつ取り出して繰り返す
    for enemy_bullet in enemy_bullets:
        # enemy_bullet_rect に pygame.Rect(enemy_bullet[0] - 4, enemy_bullet[1] - 8, 8, 16) をセットする
        enemy_bullet_rect = pygame.Rect(
            enemy_bullet[0] - 4,
            enemy_bullet[1] - 8,
            8,
            16
        )

        # enemy_bullet_rect.colliderect(player_rect) が True なら
        if enemy_bullet_rect.colliderect(player_rect):
            # enemy_bullets_to_remove に enemy_bullet を追加する
            enemy_bullets_to_remove.append(enemy_bullet)
            # player_hp に player_hp から1を引いた値を入れる
            player_hp = player_hp - 1

    # enemy_bullets_to_remove から enemy_bullet を1つずつ取り出して繰り返す
    for enemy_bullet in enemy_bullets_to_remove:
        # enemy_bullet が enemy_bullets に含まれているなら
        if enemy_bullet in enemy_bullets:
            # enemy_bullets から enemy_bullet を削除する
            enemy_bullets.remove(enemy_bullet)

    # boss_bullets_to_remove に空のリストを入れる
    boss_bullets_to_remove = []

    # boss_bullets から boss_bullet を1つずつ取り出して繰り返す
    for boss_bullet in boss_bullets:
        # boss_bullet_rect に pygame.Rect(boss_bullet[0] - boss_bullet_width // 2, boss_bullet[1], boss_bullet_width, boss_bullet_height) をセットする
        boss_bullet_rect = pygame.Rect(
            boss_bullet[0] - boss_bullet_width // 2,
            boss_bullet[1],
            boss_bullet_width,
            boss_bullet_height
        )

        # boss_bullet_rect.colliderect(player_rect) が True なら
        if boss_bullet_rect.colliderect(player_rect):
            # boss_bullets_to_remove に boss_bullet を追加する
            boss_bullets_to_remove.append(boss_bullet)
            # player_hp に player_hp から1を引いた値を入れる
            player_hp = player_hp - 1

    # boss_bullets_to_remove から boss_bullet を1つずつ取り出して繰り返す
    for boss_bullet in boss_bullets_to_remove:
        # boss_bullet が boss_bullets に含まれているなら
        if boss_bullet in boss_bullets:
            # boss_bullets から boss_bullet を削除する
            boss_bullets.remove(boss_bullet)

    # player_hp が0以下なら
    if player_hp <= 0:
        # game_state に "game_over" をセットする
        game_state = "game_over"
    # boss_active が True で boss_hp が0以下なら
    elif boss_active and boss_hp <= 0:
        # game_state に "clear" をセットする
        game_state = "clear"

    # screen に background_image を (0, background_y_1) の位置へ描く
    screen.blit(background_image, (0, background_y_1))
    # screen に background_image を (0, background_y_2) の位置へ描く
    screen.blit(background_image, (0, background_y_2))

    # player_image_rect に player_image.get_rect(center=(player_x, player_y)) をセットする
    player_image_rect = player_image.get_rect(
        center=(player_x, player_y)
    )
    # screen.blit(player_image, player_image_rect) を実行する
    screen.blit(player_image, player_image_rect)

    # bullets から bullet を1つずつ取り出して繰り返す
    for bullet in bullets:
        # screen に (255, 240, 100) と (bullet[0] - 3, bullet[1] - 10, 6, 20) を使った四角形を描く
        pygame.draw.rect(
            screen,
            (255, 240, 100),
            (bullet[0] - 3, bullet[1] - 10, 6, 20)
        )

    # enemies から enemy を1つずつ取り出して繰り返す
    for enemy in enemies:
        # enemy_image_rect に enemy_image.get_rect(center=(enemy.x, enemy.y)) をセットする
        enemy_image_rect = enemy_image.get_rect(
            center=(enemy.x, enemy.y)
        )
        # screen.blit(enemy_image, enemy_image_rect) を実行する
        screen.blit(enemy_image, enemy_image_rect)

    # enemy_bullets から enemy_bullet を1つずつ取り出して繰り返す
    for enemy_bullet in enemy_bullets:
        # screen に (255, 100, 180) と (enemy_bullet[0] - 4, enemy_bullet[1] - 8, 8, 16) を使った四角形を描く
        pygame.draw.rect(
            screen,
            (255, 100, 180),
            (enemy_bullet[0] - 4, enemy_bullet[1] - 8, 8, 16)
        )

    # boss_active が True なら
    if boss_active:
        # boss_image_rect に boss_image.get_rect(center=(boss_x, boss_y)) をセットする
        boss_image_rect = boss_image.get_rect(
            center=(boss_x, boss_y)
        )
        # screen.blit(boss_image, boss_image_rect) を実行する
        screen.blit(boss_image, boss_image_rect)

        # boss_bullets から boss_bullet を1つずつ取り出して繰り返す
        for boss_bullet in boss_bullets:
            # screen に (255, 80, 80) と (boss_bullet[0] - boss_bullet_width // 2, boss_bullet[1], boss_bullet_width, boss_bullet_height) を使った四角形を描く
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

        # boss_text に font.render(f"BOSS HP: {boss_hp}", True, (255, 255, 255)) をセットする
        boss_text = font.render(
            f"BOSS HP: {boss_hp}",
            True,
            (255, 255, 255)
        )
        # screen に boss_text を (220, 10) の位置へ描く
        screen.blit(boss_text, (220, 10))

    # hp_text に font.render(f"HP: {player_hp}", True, (255, 255, 255)) をセットする
    hp_text = font.render(
        f"HP: {player_hp}",
        True,
        (255, 255, 255)
    )
    # screen に hp_text を (10, 10) の位置へ描く
    screen.blit(hp_text, (10, 10))

    # このフレームの描画内容を画面に反映する
    pygame.display.flip()
    # 1秒間に60回を上限にして clock を進める
    clock.tick(60)

# pygame を終了する
pygame.quit()
