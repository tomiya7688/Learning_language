# pygame を読み込む
import pygame
# settings を読み込む
import settings
# battle から Battle を読み込む
from battle import Battle

# Game という型を定義する
class Game:
    # __init__ の処理を定義する
    def __init__(self):
        # settings.pyで決めた幅と高さのウィンドウを開き、あとで色や絵を描く画面を self.screen に保存する
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # pygame.display.set_caption('敵が攻撃してくる') を実行する
        pygame.display.set_caption('敵が攻撃してくる')

        # self.clock.tick(settings.FPS) で、画面更新を1秒あたり最大 settings.FPS 回に抑える
        # pygame.time.Clock() で、画面更新の間隔を測る self.clock を作る
        self.clock = pygame.time.Clock()
        # self.running を True にして、ゲーム画面の繰り返しを続ける
        self.running = True

        # self.start_game() を実行する
        self.start_game()

    # ウィンドウの準備と戦闘の作成を分けると、start_game（ゲームを始める）から戦闘の作成場所を探せます。
    def start_game(self):
        # Battle（戦闘）が、自機や弾など、この章の戦闘で使う情報を作ります。
        # GameはBattle()で作った戦闘をself.battleへ保存し、後の更新と描画で同じ戦闘を使います。
        self.battle = Battle()

    # Gameは、ウィンドウの準備と毎回の進行を混ぜないよう、操作の確認・戦闘の更新・終了判定・描画と表示をrun（実行）へまとめます。
    # main.pyのmainがgame.run()を呼び出します。runが終わるとmainへ戻り、mainのfinally内のpygame.quit()がウィンドウを閉じます。
    def run(self):
        # whileは条件がTrueの間繰り返す指定。Game.runはゲーム全体のself.runningがTrueの間、操作の確認と更新を続けます。
        while self.running:
            # Game.handle_eventsが操作の知らせを確認し、ウィンドウを閉じる知らせならGameのself.runningをFalseへ変更します。
            self.handle_events()
            # Game.runは閉じる操作でself.runningがFalseになった場合、戦闘の更新を行う前にbreakを実行します。
            if not self.running:
                # breakが画面更新のwhileをすぐに終えます。この経路では下の戦闘更新・描画・表示を行いません。
                break

            # Battle.updateが自機・弾・敵を動かし、命中した敵弾を除外して自機の体力を減らします。更新全体が終わってからGame.runへ戻ります。
            self.battle.update()

            # Game.runがBattle.is_game_overで更新後の自機のHPを確認し、0以下でTrueが返った場合だけ終了を決めます。
            if self.battle.is_game_over():
                # Game.runがGAME OVERという文字列を実行用ターミナルへ1行表示します。ゲームのウィンドウへ表示する処理ではありません。
                print("GAME OVER")
                # Game.runがself.runningをFalseにし、次のwhileの確認では繰り返しを続けないようにします。ここにはbreakがなく、今回の描画・表示は続きます。
                self.running = False

            # Battle.drawが更新後の戦闘をGameの描画先self.screenへ描きます。体力表示にも今回の命中後のHPを使います。
            self.battle.draw(self.screen)

            # pygame.display.flipが描画済みの画面をウィンドウへ表示します。HPで終了を決めた場合もこの呼び出しを行います。
            pygame.display.flip()
            # Gameのself.clock.tickがsettings.FPSを更新回数の上限として待ちます。HPで終了を決めた場合もこの呼び出しの後にwhileの条件へ戻ります。
            self.clock.tick(settings.FPS)

    # 操作ごとの分岐をhandle_events（操作を確認する）へ分けると、runから画面更新の順序を追えます。
    def handle_events(self):
        # Game.handle_eventsが、pygame.event.get()で取り出した操作の知らせの一覧をforで順番に確認します。
        # event（操作の知らせ）は、forが今回確認する1件の知らせを入れる名前です。
        for event in pygame.event.get():
            # Game.handle_eventsが知らせの種類event.typeを確認し、QUIT（終了）なら閉じる操作として扱います。
            if event.type == pygame.QUIT:
                # Game.handle_eventsがself.runningをFalse（続けない）にし、runが画面更新を終えるようにします。
                self.running = False
                # Game.handle_eventsが操作確認のforを終え、取り出した一覧の残りの知らせはBattleへ送りません。
                break

            # Game.handle_eventsが終了以外の知らせeventを今の戦闘self.battleへ渡し、Battleがキー入力を確認します。
            self.battle.handle_event(event)
