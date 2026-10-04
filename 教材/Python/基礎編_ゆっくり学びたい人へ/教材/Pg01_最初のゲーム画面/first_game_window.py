# pygame をインポートする
import pygame

# pygame を初期化する
pygame.init()

# screen に640×480のpygame画面をセットする
screen = pygame.display.set_mode((640, 480))
# pygame画面のタイトルに「最初のpygame」をセットする
pygame.display.set_caption("最初のpygame")

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

# pygame を終了する
pygame.quit()
