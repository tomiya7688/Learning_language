# pygame を読み込む
import pygame
# settings を読み込む
import settings
# player から Player を読み込む
from player import Player
# enemy から Enemy を読み込む
from enemy import Enemy
# collisions から hit_enemies を読み込む
from collisions import hit_enemies
# collisions から hit_player を読み込む
from collisions import hit_player

# Battle（戦闘）は、自機・敵・弾がどの戦闘のものか分かるよう、情報と更新する操作を同じクラスへまとめます。
class Battle:
    # Battleは、更新ごとに自機の位置や体力を初期値へ戻さないよう、作成時の準備を__init__、毎回の移動と命中判定をupdateへ分けます。
    def __init__(self):
        # player（プレイヤー）は操作する自機。selfは作成中の戦闘を指します。
        # Player()が自機1機を作り、Battleはself.playerから後の移動・射撃・体力確認で同じ自機を使います。
        self.player = Player()

        # bullets は弾の一覧。ここでは自機が撃った弾を並べます。
        # Battleは発射前の自機弾一覧を[]（空の一覧）で用意し、handle_eventで撃った弾を追加します。
        self.bullets = []

        # enemies（敵の複数形）は通常の敵の一覧。各要素はEnemyで作った敵1機です。
        # Battleは敵一覧を空で用意し、下の3回のappend（末尾への追加）で敵を1機ずつ加えます。
        self.enemies = []
        # Enemyが中心を左端から160・上端から80ピクセルへ置いた敵1機を作り、appendが戦闘の敵一覧へ加えます。
        self.enemies.append(Enemy(160, 80))
        # Enemyが中心を左端から320・上端から40ピクセルへ置いた敵1機を作り、appendが同じself.enemiesへ加えます。
        self.enemies.append(Enemy(320, 40))
        # Enemyが中心を左端から480・上端から100ピクセルへ置いた敵1機を作り、appendが同じself.enemiesへ加えます。
        self.enemies.append(Enemy(480, 100))

        # enemy_bullets は通常の敵が撃った弾の一覧です。
        # Battleは敵の発射前なので敵弾一覧も空で用意し、update_enemiesで作った敵弾を追加します。
        self.enemy_bullets = []
        # BattleはHP（hit points、体力）の文字画像を毎回作るため、文字の形と大きさを決めるフォントを戦闘のself.fontへ保存します。
        # FontのNoneは同梱のFreeSans Boldを選ぶ指定、36はピクセル単位のサイズ指定です。ピクセルは画面上の点を数える単位です。
        # Battle.__init__がフォントを一度作り、Battle.draw_textが保存済みのself.fontで更新後のHPを文字画像にします。36は文字画像の実寸の高さを保証する値ではありません。
        self.font = pygame.font.Font(None, 36)

        # Battleのself.fire_timerは、開始時または前回の発射タイミングからの更新回数。Enemyごとのタイマーではなく、戦闘で1つを共有します。
        # Battle.__init__が0を保存し、Battle.update_enemiesが更新ごとに1を足します。
        self.fire_timer = 0

    # 押した知らせで弾を作る処理を、押している状態で移動する処理と混ぜないよう、handle_event（知らせへの対応）へ分けます。
    def handle_event(self, event):
        # eventは呼び出す側が指定した操作の知らせ1件、event.typeは知らせの種類、pygame.KEYDOWNはキーを押した知らせです。
        # andは左右の条件を両方満たす指定です。キーを押した知らせのときだけ、event.key（押したキー）がpygame.K_SPACE（スペースキー）か調べます。
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # self.player.shoot()が自機の位置から弾1発を作って返し、append（末尾へ追加）がその弾を自機の弾一覧self.bulletsへ加えます。
            # appendはself.bulletsに残っている以前の弾を置き換えません。弾の作成と一覧への追加だけでは、弾の移動や描画は行いません。
            self.bullets.append(self.player.shoot())

    # Battleは、準備した機体や弾を動かし続けるため、更新1回分の移動と移動後の命中判定をupdate（更新）へまとめます。
    def update(self):
        # pygame.key.get_pressed()が今押しているキーの状態を調べ、Player.moveが矢印キーの状態に従って自機の位置を変えます。
        self.player.move(pygame.key.get_pressed())

        # Battle.move_bulletsが自機弾一覧self.bulletsの各弾を1回動かし、上下の画面外に出た弾を元の一覧から外します。
        self.move_bullets(self.bullets)

        # Battle.updateが敵の移動・画面外除外・一斉発射を行うupdate_enemiesを呼び出します。
        self.update_enemies()

        # Battle.updateが敵弾一覧self.enemy_bulletsをmove_bulletsへ指定し、今作った敵弾も同じ更新で1回動かします。
        self.move_bullets(self.enemy_bullets)

        # hit_enemiesが自機の弾と敵の重なりを調べ、命中した自機の弾をBattleのself.bullets、敵をBattleのself.enemiesから直接外します。敵の発射より後の判定です。
        hit_enemies(self.bullets, self.enemies)

        # hit_playerが移動後の敵弾と自機の重なりを調べ、命中した敵弾をBattleのself.enemy_bulletsから直接外し、Battleの自機self.playerへダメージを与えます。
        hit_player(self.enemy_bullets, self.player)

    # Battleは、戦闘の体力判定へウィンドウの終了まで混ぜないよう、HPが0以下かをis_game_over（ゲームオーバーか）へまとめ、終了はGame.runへ任せます。
    def is_game_over(self):
        # Battle.is_game_overが自機self.playerの体力hpを調べ、0以下ならTrue（成り立つ）、正ならFalse（成り立たない）をGame.runへ返します。
        # <=は以下か調べる比較。Battle.is_game_over自体は体力変更・ターミナル表示・繰り返しの終了を行いません。
        return self.player.hp <= 0

    # 弾1発の移動と、弾一覧からの削除は別の役割なので、一覧を順に管理する処理をmove_bullets（弾を動かす）へ分けます。
    def move_bullets(self, bullets):
        # bulletsは呼び出す側が指定した弾一覧です。bullets[:]は一覧だけのコピーで、各要素は元の一覧と同じ弾を指します。
        # forはコピーの弾を順に1発ずつbulletへ選びます。元のbulletsから削除しても、コピーの次の弾を飛ばしません。
        for bullet in bullets[:]:
            # bullet.move()が、選んだ弾bulletに保存した移動量で位置を1回進めます。
            bullet.move()
            # bullet.is_off_screen()（選んだ弾が画面外か）がTrue（成り立つ）を返した場合だけ、bullets.remove(bullet)を実行します。
            if bullet.is_off_screen():
                # bullets.remove(bullet)が選んだ弾bulletを元の弾一覧bulletsから外します。弾一覧の削除は画面の絵を直接消す操作ではありません。
                bullets.remove(bullet)

    # Battleは、敵1機の移動・弾の作成へ一覧の変更まで混ぜないよう、敵一覧の更新と一斉発射の間隔をupdate_enemiesへまとめます。
    # Battle.updateがupdate_enemiesを1回呼び、Enemy.move・is_off_screen・shootへ敵1機ずつの操作を任せます。
    def update_enemies(self):
        # self.enemies[:]はBattleの敵一覧だけのコピー。forは元のself.enemiesと同じ敵をenemy（選んだ敵）へ1機ずつ選びます。
        # Battle.update_enemiesが元のself.enemiesから敵を外しても、コピーを読むforは次の敵を飛ばしません。
        for enemy in self.enemies[:]:
            # Enemy.moveが選んだ敵の保存済みの移動量で位置を1回進めます。発射位置を使う前に敵を移動します。
            enemy.move()
            # Enemy.is_off_screenが敵の上端と画面の高さを比較し、Trueの場合だけBattle.update_enemiesが除外を行います。
            if enemy.is_off_screen():
                # removeが選んだ敵を元の敵一覧self.enemiesから外します。除外された敵は、この後の発射対象へ入りません。
                self.enemies.remove(enemy)

        # Battle.update_enemiesが、戦闘で共有する更新回数self.fire_timerへ1を足します。敵が0機でもこの回数は進みます。
        self.fire_timer += 1
        # >=は以上か調べる比較。数えた回数がsettings.ENEMY_FIRE_INTERVALに届くと、残った敵を一斉に発射させます。
        if self.fire_timer >= settings.ENEMY_FIRE_INTERVAL:
            # Battle.update_enemiesが回数を0へ戻し、次の発射タイミングまで再び更新を数えます。残った敵が0機でも0へ戻します。
            self.fire_timer = 0
            # forが元の敵一覧self.enemiesに残った敵だけを、enemyへ1機ずつ選びます。
            for enemy in self.enemies:
                # Enemy.shootが選んだ敵の移動後の位置で作った弾を返し、appendがBattleの敵弾一覧self.enemy_bulletsへ加えます。
                # appendは以前の敵弾を置き換えません。Battle.updateが、この呼び出しの後に敵弾の移動と命中判定を行います。
                self.enemy_bullets.append(enemy.shoot())

    # Battleは、位置や体力を変更するupdateと絵を描く処理を混ぜないよう、戦闘全体の描画をdraw（描く）へまとめます。
    # Game.runがゲームの描画先self.screenをscreenへ指定します。Battle.drawは同じ描画先へ背景・機体・弾・HPの順に描きます。
    def draw(self, screen):
        # fillが描画先screen全体を暗い青系の色で塗り、前の更新の絵を覆います。色は赤10・緑10・青30で、各値は0（暗い）から255（明るい）です。
        # Battleの自機・弾・敵の情報は変えず、描画先の色だけを変えます。背景を後から塗ると、その前に描いた機体や文字も覆ってしまいます。
        screen.fill((10, 10, 30))

        # Player.drawが戦闘の自機self.playerの長方形から3点を選び、水色(100, 200, 255)の三角形をscreenへ描きます。Battle.drawは自機を動かしません。
        self.player.draw(screen)
        # Battle.draw_bulletsが戦闘の自機の弾一覧self.bulletsに残る弾をscreenへ描きます。命中や画面外判定で除外した弾は描きません。
        self.draw_bullets(screen, self.bullets)

        # forが戦闘の敵一覧self.enemiesに残る敵をenemy（選んだ敵）へ1機ずつ選びます。空の一覧なら敵を描く処理は0回です。
        for enemy in self.enemies:
            # Enemy.drawが選んだ敵enemyの長方形を赤系の色(255, 100, 100)で同じ描画先screenへ描きます。
            enemy.draw(screen)

        # Battle.draw_bulletsが戦闘の敵弾一覧self.enemy_bulletsに残る弾を同じscreenへ描きます。
        self.draw_bullets(screen, self.enemy_bullets)
        # f付きの文字列は{}内の値を文字列へ組み込みます。自機self.player.hpが3ならHP: 3、2ならHP: 2、-1ならHP: -1をdraw_textへ指定します。
        # Battle.draw_textが白いHP文字画像の左上を、screenの左端から10・上端から10ピクセルへ置きます。Game.runが後のflipで描画済みの画面を表示します。
        self.draw_text(screen, f"HP: {self.player.hp}", (10, 10))

    # 自機の弾一覧と敵弾一覧を描く繰り返しが同じなので、Battleは一覧の描画をdraw_bulletsへまとめ、弾1発の描画はBullet.drawへ任せます。
    def draw_bullets(self, screen, bullets):
        # Battle.drawが指定したscreenはGameの描画先、bulletsは戦闘のself.bullets（自機の弾）またはself.enemy_bullets（敵弾）と同じ一覧です。
        # forが指定された一覧に残る弾をbullet（選んだ弾）へ1発ずつ選びます。空の一覧ならBullet.drawの呼び出しは0回です。
        for bullet in bullets:
            # Bullet.drawが選んだ弾の保存済みの位置・大きさ・色でscreenへ描きます。Battle.draw_bulletsは弾を動かしたり一覧へ追加・除外したりしません。
            bullet.draw(screen)

    # HP文字を用意するdrawへ文字画像の作成と配置まで詰めないよう、Battleは文字列から画像を作って置く処理をdraw_text（文字を描く）へまとめます。
    def draw_text(self, screen, text, position):
        # Battle.drawが、Gameの描画先をscreen、更新後の自機のHPを含む文字列をtext、文字画像の左上の位置(10, 10)をpositionへ指定します。
        # imageは文字画像。保存済みのフォントself.fontのrenderがtextを描いた新しいSurface（画像を持つPygameの部品）を返し、imageへ保存します。
        # Trueは文字の縁を滑らかにする指定、(255, 255, 255)は赤・緑・青を各255にする白色です。背景色は省略するので、文字以外の部分は透明です。
        image = self.font.render(text, True, (255, 255, 255))
        # blitが文字画像imageを描画先screenへ重ねます。positionは画像の左上で、中心位置ではありません。文字画像を作っただけではscreenへ描かれません。
        # Battle.draw_textは画像をファイルへ保存せず、Game.runのpygame.display.flipが後でウィンドウへ表示します。
        screen.blit(image, position)
