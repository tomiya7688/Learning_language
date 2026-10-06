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
# menu_view から MenuScreen を読み込む
from menu_view import MenuScreen
# game_over_view から GameOverScreen を読み込む
from game_over_view import GameOverScreen

# Game という型を定義する
class Game:
    # __init__ の処理を定義する
    def __init__(self):
        # screen は画面。pygameが用意した描画先です。
        # self.screen に pygame.display.set_mode((settings.WIDTH, settings.HEIGHT)) を入れる
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # pygame.display.set_caption('ゲームオーバー画面を作る') を実行する
        pygame.display.set_caption('ゲームオーバー画面を作る')

        # clock は時計。画面更新を最大60回/秒に調整します。
        # self.clock に pygame.time.Clock() を入れる
        self.clock = pygame.time.Clock()
        # running は実行中かどうか。Falseで繰り返しを終えます。
        # self.running に True を入れる
        self.running = True

        # self.start_game() を実行する
        self.start_game()

    # start_game の処理を定義する
    def start_game(self):
        # battle は戦闘。1回のゲームで使う自機と敵と弾の一覧を持ちます。
        # self.battle に Battle() を入れる
        self.battle = Battle()

        # current_screen は現在の画面。入力・更新・描画をこの画面へ任せます。
        # self.current_screen に PlayingScreen(self) を入れる
        self.current_screen = PlayingScreen(self)

    # show_clear の処理を定義する
    def show_clear(self):
        # current_screen は現在の画面。入力・更新・描画をこの画面へ任せます。
        # self.current_screen に ClearScreen(self) を入れる
        self.current_screen = ClearScreen(self)

    # show_menu の処理を定義する
    def show_menu(self):
        # current_screen は現在の画面。入力・更新・描画をこの画面へ任せます。
        # self.current_screen に MenuScreen(self) を入れる
        self.current_screen = MenuScreen(self)

    # show_game_over の処理を定義する
    def show_game_over(self):
        # current_screen は現在の画面。入力・更新・描画をこの画面へ任せます。
        # self.current_screen に GameOverScreen(self) を入れる
        self.current_screen = GameOverScreen(self)

    # run の処理を定義する
    def run(self):
        # self.running が成り立つ間、繰り返す
        while self.running:
            # self.handle_events() を実行する
            self.handle_events()
            # not self.running が成り立つなら
            if not self.running:
                # この繰り返しを終える
                break

            # self.current_screen.update() を実行する
            self.current_screen.update()
            # self.current_screen.draw(self.screen) を実行する
            self.current_screen.draw(self.screen)

            # pygame.display.flip() を実行する
            pygame.display.flip()
            # self.clock.tick(settings.FPS) を実行する
            self.clock.tick(settings.FPS)

    # handle_events の処理を定義する
    def handle_events(self):
        # pygame.event.get() から event を1つずつ取り出して繰り返す
        for event in pygame.event.get():
            # event.type == pygame.QUIT が成り立つなら
            if event.type == pygame.QUIT:
                # running は実行中かどうか。Falseで繰り返しを終えます。
                # self.running に False を入れる
                self.running = False
                # この繰り返しを終える
                break

            # self.current_screen.handle_event(event) を実行する
            self.current_screen.handle_event(event)
