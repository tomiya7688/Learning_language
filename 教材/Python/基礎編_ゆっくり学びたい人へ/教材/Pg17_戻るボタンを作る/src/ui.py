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

# Button という型を定義する
class Button:
    # __init__ の処理を定義する
    def __init__(self, rect, text, action):
        # rect はrectangle（長方形）の略。位置・大きさと当たり判定に使います。
        # self.rect に pygame.Rect(rect) を入れる
        self.rect = pygame.Rect(rect)
        # text は表示する文字列です。
        # self.text に text を入れる
        self.text = text
        # action はボタンが押されたときに呼ぶ処理です。
        # self.action に action を入れる
        self.action = action
        # font はフォント。文字の形と大きさを指定します。
        # self.font に pygame.font.Font(None, 40) を入れる
        self.font = pygame.font.Font(None, 40)

    # handle_event の処理を定義する
    def handle_event(self, event):
        # event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 が成り立つなら
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # self.rect.collidepoint(event.pos) が成り立つなら
            if self.rect.collidepoint(event.pos):
                # self.action() を実行する
                self.action()

    # draw の処理を定義する
    def draw(self, screen):
        # pygame.draw.rect(screen, (70, 110, 190), self.rect, border_radius=8) を実行する
        pygame.draw.rect(screen, (70, 110, 190), self.rect, border_radius=8)
        # draw_centered_text(screen, self.font, self.text, (255, 255, 255), self.rect.center) を実行する
        draw_centered_text(screen, self.font, self.text, (255, 255, 255), self.rect.center)
