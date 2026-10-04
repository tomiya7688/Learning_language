# pygame をインポートする
import pygame

# pygame を初期化する
pygame.init()

# screen に640×480のpygame画面をセットする
screen = pygame.display.set_mode((640, 480))
# pygame画面のタイトルに「プレイヤーを表示する」をセットする
pygame.display.set_caption("プレイヤーを表示する")

# 画面更新の間隔を調整する時計を用意する（後でclock.tick(60)に使う）
# clock に pygame.time.Clock() で作った時計を入れる
clock = pygame.time.Clock()

# player_x に320を入れる
player_x = 320
# player_y に400を入れる
player_y = 400

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
