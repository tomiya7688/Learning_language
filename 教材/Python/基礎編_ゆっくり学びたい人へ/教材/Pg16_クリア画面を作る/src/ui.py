# pygame を読み込む
import pygame

# draw_centered_text の処理を定義する
def draw_centered_text(screen, font, text, color, center):
    # image は画像。画面へ描く内容を持ちます。
    # image に font.render(text, True, color) を入れる
    image = font.render(text, True, color)
    # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
    # rect に image.get_rect(center=center) を入れる
    rect = image.get_rect(center=center)
    # screen.blit(image, rect) を実行する
    screen.blit(image, rect)
