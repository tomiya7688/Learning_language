# settingsは設定という意味です。数値の調整場所をまとめるため、このファイルへゲームの設定を置きます。
# WIDTHは画面の横幅（ピクセル、画面の大きさを数える単位）。=は右の数値を左の名前へ保存する書き方です。
WIDTH = 640
# HEIGHT はゲーム画面の縦幅（ピクセル）です。
# HEIGHT に 480 を入れる
HEIGHT = 480
# FPSはframes per second（1秒あたりの画面更新回数）の略。このゲームでは更新回数の上限を指定します。
# Game.runはsettings.FPSをClock.tickへ指定して毎秒最大60回に抑えます。実際の更新が毎秒60回になる保証はありません。
FPS = 60
# PLAYER_X は自機を最初に置く中心位置です。画面左端からの距離をピクセルで表します。
# PLAYER_X に 320 を入れる
PLAYER_X = 320
# PLAYER_Y は自機を最初に置く中心位置です。画面上端からの距離をピクセルで表します。
# PLAYER_Y に 400 を入れる
PLAYER_Y = 400
# PLAYER_SPEEDは自機が矢印の方向ごとに更新1回で進む量（ピクセル）です。Playerは作成時にこの値を保存します。
# 配布時の値5で、その更新で画面端に届かない場合、Player.moveは右と上の同時押しで横5・縦5動かします。値5で右と上を押し、更新後もどの端にも届かない場合、自機の斜め距離は約7.1です。
# Player.moveは画面端では自機を画面内へ戻すため、矢印の方向へ進む量がPLAYER_SPEED未満になる場合があります。
PLAYER_SPEED = 5
# BULLET_SPEEDは自機弾の上への移動量の大きさ（ピクセル/更新1回）です。配布時の値8なら、Player.shootは負の-8を新しい弾へ指定します。
# 配布時の値8なら、Bullet.moveは弾の上端の縦位置へ-8を足し、自機弾を上へ8動かします。縦位置は画面上端0から下ほど大きくなります。
# BULLET_SPEEDが12ならPlayer.shootは-12をBulletへ指定し、Bullet.__init__が保存します。Bullet.moveはその弾を更新1回で上へ12動かします。
BULLET_SPEED = 8
# ENEMY_SPEEDはこの章の敵が下へ進む量（ピクセル/更新1回）です。Enemyは作成時にこの値を保存します。
# Enemy.moveは敵の上端の縦位置へ保存した移動量を足します。値1なら下へ1、値2なら下へ2ピクセル動きます。
ENEMY_SPEED = 1
# PLAYER_HPは自機の初期体力です。Player.take_damageは命中した敵弾1発ごとに自機の体力を1減らし、Game.runは体力0以下で終了します。
# Player.__init__は作成時にsettings.PLAYER_HPを自機へ保存します。3なら合計3発、5なら合計5発の命中で体力0になります。
PLAYER_HP = 3
# ENEMY_BULLET_SPEEDは敵弾の下への移動量（ピクセル/更新1回）です。配布時の値4なら、Enemy.shootは正の4を新しい弾へ指定します。
# Bullet.moveは敵弾の上端の縦位置へ保存した移動量を足します。値4なら下へ4、値6なら下へ6ピクセル動きます。
ENEMY_BULLET_SPEED = 4
# ENEMY_FIRE_INTERVALは、Battleが敵全体で共有する発射間隔（更新回数）です。Battleの敵一覧に残る敵は同じ更新で一斉に撃ちます。
# Game.runが毎秒60回更新できる場合、発射間隔90回は約1.5秒、60回は約1秒です。Battleは更新回数を数えるため、更新が遅いほど秒数は長くなります。
ENEMY_FIRE_INTERVAL = 90
