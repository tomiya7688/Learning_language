# pygame を読み込む
import pygame
# settings を読み込む
import settings
# battle から Battle を読み込む
from battle import Battle
# playing_view から PlayingScreen を読み込む
from playing_view import PlayingScreen
# clear_view から ClearScreen を読み込む
from clear_view import ClearScreen
# game_over_view から GameOverScreen を読み込む
from game_over_view import GameOverScreen
# title_view から TitleScreen を読み込む
from title_view import TitleScreen

# Game という型を定義する
class Game:
    # __init__ の処理を定義する
    def __init__(self):
        # settings.pyで決めた幅と高さのウィンドウを開き、あとで色や絵を描く画面を self.screen に保存する
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # pygame.display.set_caption('始めるボタンを作る') を実行する
        pygame.display.set_caption('始めるボタンを作る')

        # self.clock.tick(settings.FPS) で、画面更新を1秒あたり最大 settings.FPS 回に抑える
        # pygame.time.Clock() で、画面更新の間隔を測る self.clock を作る
        self.clock = pygame.time.Clock()
        # self.running を True にして、ゲーム画面の繰り返しを続ける
        self.running = True

        # self.show_title() を実行する
        self.show_title()

    # start_game の処理を定義する
    def start_game(self):
        # battle は戦闘。1回のゲームで使う自機と敵と弾の一覧を持ちます。
        # self.battle に Battle() を入れる
        self.battle = Battle()

        # self.current_screen を PlayingScreen に替え、次の更新から戦闘画面を表示する
        # self.current_screen に PlayingScreen(self) を入れる
        self.current_screen = PlayingScreen(self)

    # show_clear の処理を定義する
    def show_clear(self):
        # self.current_screen を ClearScreen に替え、次の更新からクリア結果を表示する
        # self.current_screen に ClearScreen(self) を入れる
        self.current_screen = ClearScreen(self)

    # show_game_over の処理を定義する
    def show_game_over(self):
        # self.current_screen を GameOverScreen に替え、次の更新からゲームオーバー結果を表示する
        # self.current_screen に GameOverScreen(self) を入れる
        self.current_screen = GameOverScreen(self)

    # show_title の処理を定義する
    def show_title(self):
        # self.current_screen を TitleScreen に替え、次の更新からタイトル画面を表示する
        # self.current_screen に TitleScreen(self) を入れる
        self.current_screen = TitleScreen(self)

    # run の処理を定義する
    def run(self):
        # self.running が True の間、ゲーム画面を更新する
        while self.running:
            # self.handle_events() を実行する
            self.handle_events()
            # self.running が False なら、次の画面更新をせず繰り返しを終える
            if not self.running:
                # 画面更新を繰り返す while を終える
                break

            # self.current_screen.update() を実行する
            self.current_screen.update()
            # self.current_screen.draw(self.screen) を実行する
            self.current_screen.draw(self.screen)

            # pygame.display.flip() を実行する
            pygame.display.flip()
            # settings.FPS 回/秒を上限にして、画面更新が速くなりすぎないよう待つ
            self.clock.tick(settings.FPS)

    # handle_events の処理を定義する
    def handle_events(self):
        # Pygameに届いた操作の知らせを1つずつ取り出して確認する
        for event in pygame.event.get():
            # event.type が pygame.QUIT なら、ウィンドウを閉じる操作を受けています。
            if event.type == pygame.QUIT:
                # self.running を False にし、ゲーム画面の繰り返しを終える
                self.running = False
                # 残りの操作を確認せず、操作確認の繰り返しを終える
                break

            # self.current_screen.handle_event(event) を実行する
            self.current_screen.handle_event(event)
