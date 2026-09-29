# Path をインポートする
from pathlib import Path

# pygame をインポートする
import pygame

# pygame を初期化する
pygame.init()

# screen に640×480のpygame画面をセットする
screen = pygame.display.set_mode((640, 480))
# pygame画面のタイトルに「同梱背景素材を使う」をセットする
pygame.display.set_caption("同梱背景素材を使う")

# clock に pygame.time.Clock() をセットする
clock = pygame.time.Clock()
# font に pygame.font.Font(None, 36) をセットする
font = pygame.font.Font(None, 36)

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

# game_clear に False を入れる
game_clear = False
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
            # event.key が pygame.K_SPACE なら
            if event.key == pygame.K_SPACE:
                # bullets に [player_x, player_y - 20] を追加する
                bullets.append([player_x, player_y - 20])

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
            # enemy_rect に pygame.Rect(enemy.x - 20, enemy.y - 15, 40, 30) をセットする
            enemy_rect = pygame.Rect(
                enemy.x - 20,
                enemy.y - 15,
                40,
                30
            )

            # bullet_rect.colliderect(enemy_rect) が True なら
            if bullet_rect.colliderect(enemy_rect):
                # bullets_to_remove に bullet を追加する
                bullets_to_remove.append(bullet)
                # enemies_to_remove に enemy を追加する
                enemies_to_remove.append(enemy)

        # boss_active が True なら
        if boss_active:
            # boss_rect に pygame.Rect(boss_x - 60, boss_y - 30, 120, 60) をセットする
            boss_rect = pygame.Rect(
                boss_x - 60,
                boss_y - 30,
                120,
                60
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

    # player_rect に pygame.Rect(player_x - 20, player_y - 20, 40, 40) をセットする
    player_rect = pygame.Rect(
        player_x - 20,
        player_y - 20,
        40,
        40
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
        # running に False を入れる
        running = False

    # boss_active が True で boss_hp が0以下なら
    if boss_active and boss_hp <= 0:
        # game_clear に True を入れる
        game_clear = True
        # running に False を入れる
        running = False

    # screen に background_image を (0, background_y_1) の位置へ描く
    screen.blit(background_image, (0, background_y_1))
    # screen に background_image を (0, background_y_2) の位置へ描く
    screen.blit(background_image, (0, background_y_2))

    # player_points に (player_x, player_y - 20)、(player_x - 20, player_y + 20)、(player_x + 20, player_y + 20) を入れる
    player_points = [
        (player_x, player_y - 20),
        (player_x - 20, player_y + 20),
        (player_x + 20, player_y + 20)
    ]

    # screen に (100, 200, 255) と player_points を使った多角形を描く
    pygame.draw.polygon(screen, (100, 200, 255), player_points)

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
        # screen に (255, 100, 100) と (enemy.x - 20, enemy.y - 15, 40, 30) を使った四角形を描く
        pygame.draw.rect(
            screen,
            (255, 100, 100),
            (enemy.x - 20, enemy.y - 15, 40, 30)
        )

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
        # screen に (180, 80, 255) と (boss_x - 60, boss_y - 30, 120, 60) を使った四角形を描く
        pygame.draw.rect(
            screen,
            (180, 80, 255),
            (boss_x - 60, boss_y - 30, 120, 60)
        )

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

# game_clear が True なら
if game_clear:
    # "GAME CLEAR" を表示する
    print("GAME CLEAR")
