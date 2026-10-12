# Pythonが、ウィンドウ・操作の知らせ・更新の間隔を扱うpygameの機能を読み込みます。
import pygame
# Pythonが、同じsrcのsettings.pyから画面の幅・高さ・更新回数の上限を読み込みます。
import settings
# Pythonが、同じsrcのbattle.pyから自機・敵・弾と更新をまとめるBattle（戦闘）の定義を読み込みます。
from battle import Battle

# Game（ゲーム全体）は、戦闘の機体や弾とウィンドウの操作を混ぜないよう、描画先・更新の間隔・続けるかの情報と操作をまとめるクラスです。
class Game:
    # Gameは、更新のたびにウィンドウや戦闘を作り直さないよう、作成時の準備を__init__、毎回の進行をrunへ分けます。selfは作成するゲーム全体を指します。
    def __init__(self):
        # pygame.display.set_modeが幅settings.WIDTH・高さsettings.HEIGHTのウィンドウを開き、絵を描く先のSurface（画像を持つ部品）をself.screenから使えるようにします。
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # pygame.display.set_captionがウィンドウの題名を「敵が攻撃してくる」にします。ゲーム画面の中へ文字を描く処理ではありません。
        pygame.display.set_caption('敵が攻撃してくる')

        # Gameは速すぎる更新を抑えるため、前回のtickからの経過時間を扱うClockをself.clockへ用意します。
        # Clockを作るだけでは待ちません。Game.runのself.clock.tick(settings.FPS)が更新ごとに必要な時間を待ち、1秒あたりの更新回数を制限します。
        self.clock = pygame.time.Clock()
        # running（実行中か）をTrue（続ける）にし、Game.runが更新の繰り返しを始められるようにします。
        self.running = True

        # Game.start_gameが自機・敵・弾を管理する戦闘を作り、Gameのself.battleから使えるようにします。
        self.start_game()

    # Gameは、描画先や更新の間隔の準備へ自機・敵の準備まで詰めないよう、戦闘を作る操作をstart_game（ゲームを始める）へ分けます。
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

    # Gameは、閉じる操作の判断を戦闘の射撃へ混ぜないよう、操作の知らせをhandle_eventsで確認し、終了以外の知らせをBattleへ送ります。
    def handle_events(self):
        # pygame.event.get()が待っている操作や変化の知らせを一覧で取り出します。取り出した知らせはPygameの待ち一覧から外れます。
        # Game.handle_eventsのforが取り出した一覧を順に読み、event（操作や変化の知らせ）へ今回確認する1件を選びます。
        for event in pygame.event.get():
            # Game.handle_eventsが知らせの種類event.typeを確認し、QUIT（終了）なら閉じる操作として扱います。
            if event.type == pygame.QUIT:
                # Game.handle_eventsがself.runningをFalse（続けない）にし、runが画面更新を終えるようにします。
                self.running = False
                # Game.handle_eventsが操作確認のforを終え、取り出した一覧の残りの知らせはBattleへ送りません。
                break

            # Game.handle_eventsが終了以外の知らせeventを戦闘self.battleへ指定します。Battle.handle_eventはスペースキーを押した知らせのときだけ弾を追加します。
            self.battle.handle_event(event)
