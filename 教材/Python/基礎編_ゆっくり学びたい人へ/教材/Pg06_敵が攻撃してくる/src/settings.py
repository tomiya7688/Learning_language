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
# PLAYER_SPEED は、画面更新1回で押した矢印の方向へ進む距離です（ピクセル）。
# 縦と横を同時に押すと、それぞれの方向へ PLAYER_SPEED だけ進みます
# PLAYER_SPEED に 5 を入れる
PLAYER_SPEED = 5
# BULLET_SPEED は自機の弾が1回の画面更新で動く距離（ピクセル）です。
# player.py はこの値を負にし、自機の弾を上へ動かします。
# BULLET_SPEED に 8 を入れる
BULLET_SPEED = 8
# ENEMY_SPEED は通常の敵が画面を1回更新する間に下へ動く距離です。単位はピクセルです。
# ENEMY_SPEED に 1 を入れる
ENEMY_SPEED = 1
# PLAYER_HPは自機の初期体力です。Player.take_damageは命中した敵弾1発ごとに自機の体力を1減らし、Game.runは体力0以下で終了します。
# Player.__init__は作成時にsettings.PLAYER_HPを自機へ保存します。3なら合計3発、5なら合計5発の命中で体力0になります。
PLAYER_HP = 3
# ENEMY_BULLET_SPEED は通常の敵の弾が画面を1回更新する間に下へ動く距離です。単位はピクセルです。
# ENEMY_BULLET_SPEED に 4 を入れる
ENEMY_BULLET_SPEED = 4
# ENEMY_FIRE_INTERVALは、Battleが敵全体で共有する発射間隔（更新回数）です。Battleの敵一覧に残る敵は同じ更新で一斉に撃ちます。
# Game.runが毎秒60回更新できる場合、発射間隔90回は約1.5秒、60回は約1秒です。Battleは更新回数を数えるため、更新が遅いほど秒数は長くなります。
ENEMY_FIRE_INTERVAL = 90
