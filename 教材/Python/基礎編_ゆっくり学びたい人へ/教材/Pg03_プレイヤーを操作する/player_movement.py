# pygame をインポートする
import pygame

# pygame を初期化する
pygame.init()

# screen に640×480のpygame画面をセットする
screen = pygame.display.set_mode((640, 480))
# pygame画面のタイトルに「プレイヤーを操作する」をセットする
pygame.display.set_caption("プレイヤーを操作する")

# 画面更新の間隔を調整する時計を用意する（後でclock.tick(60)に使う）
# clock に pygame.time.Clock() で作った時計を入れる
clock = pygame.time.Clock()

# player_x に320を入れる
player_x = 320
# player_y に400を入れる
player_y = 400
# player_speed に5を入れる
player_speed = 5

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

    # screen を (10, 10, 30) で塗る
    screen.fill((10, 10, 30))

    # player_points に (player_x, player_y - 20)、(player_x - 20, player_y + 20)、(player_x + 20, player_y + 20) を入れる
    player_points = [
        (player_x, player_y - 20),
        (player_x - 20, player_y + 20),
        (player_x + 20, player_y + 20)
    ]

    # screen に (100, 200, 255) と player_points を使った多角形を描く
    pygame.draw.polygon(screen, (100, 200, 255), player_points)

    # このフレームの描画内容を画面に反映する
    pygame.display.flip()

    # 1秒間に60回を上限にして clock を進める
    clock.tick(60)

# pygame を終了する
pygame.quit()
