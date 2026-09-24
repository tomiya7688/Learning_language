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

    # ゲーム画面全体を暗く青みのある色で塗ります。
    # 色は赤・緑・青の順で、それぞれ0〜255です。
    screen.fill((10, 10, 30))

    # プレイヤーの三角形を作る3つの点です。
    # 座標の数字はゲーム画面上のピクセル数です。
    player_points = [
        (player_x, player_y - 20),
        (player_x - 20, player_y + 20),
        (player_x + 20, player_y + 20)
    ]

    # screenへ、明るい水色でplayer_pointsの三角形を描きます。
    pygame.draw.polygon(screen, (100, 200, 255), player_points)

    # このフレームで描いた内容を画面へ反映します。
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
