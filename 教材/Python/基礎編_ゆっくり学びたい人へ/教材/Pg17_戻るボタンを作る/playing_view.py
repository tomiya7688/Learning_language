# PlayingScreen という型を定義する
class PlayingScreen:
    # __init__ の処理を定義する
    def __init__(self, game):
        # game はゲーム全体。起動・繰り返し・画面切り替えを担当します。
        # self.game に game を入れる
        self.game = game

    # handle_event の処理を定義する
    def handle_event(self, event):
        # self.game.battle.handle_event(event) を実行する
        self.game.battle.handle_event(event)

    # update の処理を定義する
    def update(self):
        # self.game.battle.update() を実行する
        self.game.battle.update()
        # self.game.battle.is_game_over() が成り立つなら
        if self.game.battle.is_game_over():

            # print('GAME OVER') を実行する
            print("GAME OVER")
            # running は実行中かどうか。Falseで繰り返しを終えます。
            # self.game.running に False を入れる
            self.game.running = False

        # self.game.battle.is_clear() が成り立つなら
        elif self.game.battle.is_clear():
            # self.game.show_clear() を実行する
            self.game.show_clear()

    # draw の処理を定義する
    def draw(self, screen):
        # self.game.battle.draw(screen) を実行する
        self.game.battle.draw(screen)
