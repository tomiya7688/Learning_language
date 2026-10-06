# pygame を読み込む
import pygame
# ui から draw_centered_text を読み込む
from ui import draw_centered_text
# ui から Button を読み込む
from ui import Button

# TitleScreen という型を定義する
class TitleScreen:
    # __init__ の処理を定義する
    def __init__(self, game):
        # game はゲーム全体。起動・繰り返し・画面切り替えを担当します。
        # self.game に game を入れる
        self.game = game
        # heading_font は見出し用のフォントです。
        # self.heading_font に pygame.font.Font(None, 64) を入れる
        self.heading_font = pygame.font.Font(None, 64)

        # sub_font は補足文用のフォントです。
        # self.sub_font に pygame.font.Font(None, 32) を入れる
        self.sub_font = pygame.font.Font(None, 32)
        # buttons はボタンの一覧。表示する文字と押した後の処理を持ちます。
        # self.buttons に [Button((220, 330, 200, 60), 'START', game.start_game)] を入れる
        self.buttons = [
            Button((220, 330, 200, 60), 'START', game.start_game),
        ]

    # handle_event の処理を定義する
    def handle_event(self, event):
        # self.buttons から button を1つずつ取り出して繰り返す
        for button in self.buttons:
            # button.handle_event(event) を実行する
            button.handle_event(event)

    # update の処理を定義する
    def update(self):
        # この処理を終える
        return

    # draw の処理を定義する
    def draw(self, screen):
        # screen.fill((10, 10, 30)) を実行する
        screen.fill((10, 10, 30))
        # draw_centered_text(screen, self.heading_font, 'SPACE SHOOTER', (255, 240, 100), (320, 200)) を実行する
        draw_centered_text(screen, self.heading_font, 'SPACE SHOOTER', (255, 240, 100), (320, 200))
        # draw_centered_text(screen, self.sub_font, 'Defeat the boss!', (190, 190, 210), (320, 280)) を実行する
        draw_centered_text(screen, self.sub_font, 'Defeat the boss!', (190, 190, 210), (320, 280))

        # self.buttons から button を1つずつ取り出して繰り返す
        for button in self.buttons:
            # button.draw(screen) を実行する
            button.draw(screen)
