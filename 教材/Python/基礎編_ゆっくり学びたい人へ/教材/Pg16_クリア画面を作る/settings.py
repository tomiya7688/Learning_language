# WIDTH はゲーム画面の横幅（ピクセル）です。
# WIDTH に 640 を入れる
WIDTH = 640
# HEIGHT はゲーム画面の縦幅（ピクセル）です。
# HEIGHT に 480 を入れる
HEIGHT = 480
# FPS はゲーム画面を1秒間に更新する回数の上限です。
# FPS に 60 を入れる
FPS = 60
# PLAYER_X は自機を最初に置く中心位置です。画面左端からの距離をピクセルで表します。
# PLAYER_X に 320 を入れる
PLAYER_X = 320
# PLAYER_Y は自機を最初に置く中心位置です。画面上端からの距離をピクセルで表します。
# PLAYER_Y に 400 を入れる
PLAYER_Y = 400
# PLAYER_SPEED は自機が画面を1回更新する間に移動する距離です。単位はピクセルです。
# PLAYER_SPEED に 5 を入れる
PLAYER_SPEED = 5
# BULLET_SPEED は自機の弾が1回の画面更新で動く距離（ピクセル）です。
# player.py はこの値を負にし、自機の弾を上へ動かします。
# BULLET_SPEED に 8 を入れる
BULLET_SPEED = 8
# ENEMY_SPEED は通常の敵が画面を1回更新する間に下へ動く距離です。単位はピクセルです。
# ENEMY_SPEED に 1 を入れる
ENEMY_SPEED = 1
# PLAYER_HP は自機がゲーム開始時に持つ体力の値です。
# PLAYER_HP に 3 を入れる
PLAYER_HP = 3
# ENEMY_BULLET_SPEED は通常の敵の弾が画面を1回更新する間に下へ動く距離です。単位はピクセルです。
# ENEMY_BULLET_SPEED に 4 を入れる
ENEMY_BULLET_SPEED = 4
# SPAWN_POSITIONS_X は敵を出す順に並べた横位置です。
# 各値は画面左端から敵の中心までの距離（ピクセル）です。
# SPAWN_POSITIONS_X に (120, 320, 520, 220, 420, 100, 540) を入れる
SPAWN_POSITIONS_X = (120, 320, 520, 220, 420, 100, 540)
# SPAWN_INTERVAL は次の敵が出現するまでの画面更新回数です。
# FPS=60で毎秒60回更新される場合、90回は約1.5秒です。
# SPAWN_INTERVAL に 90 を入れる
SPAWN_INTERVAL = 90
# ENEMY_FIRE_INTERVALS は出現順の敵ごとに、次の弾を撃つまでの画面更新回数を並べた一覧です。
# ENEMY_FIRE_INTERVALS に (60, 90, 120, 75, 105, 80, 110) を入れる
ENEMY_FIRE_INTERVALS = (60, 90, 120, 75, 105, 80, 110)
# BOSS_X はボスを最初に置く中心位置です。画面左端からの距離をピクセルで表します。
# BOSS_X に 320 を入れる
BOSS_X = 320
# BOSS_Y はボスを最初に置く中心位置です。画面上端からの距離をピクセルで表します。
# BOSS_Y に 90 を入れる
BOSS_Y = 90
# BOSS_HP はボスがゲーム開始時に持つ体力の値です。
# BOSS_HP に 50 を入れる
BOSS_HP = 50
# BOSS_BULLET_SPEED はボスの弾が画面を1回更新する間に下へ動く距離です。単位はピクセルです。
# BOSS_BULLET_SPEED に 4 を入れる
BOSS_BULLET_SPEED = 4
# BOSS_FIRE_INTERVAL はボスが次の弾を撃つまでの画面更新回数です。
# BOSS_FIRE_INTERVAL に 120 を入れる
BOSS_FIRE_INTERVAL = 120
# BOSS_BULLET_WIDTH はボスの弾の横幅です。単位はピクセルです。
# BOSS_BULLET_WIDTH に 48 を入れる
BOSS_BULLET_WIDTH = 48
# BOSS_BULLET_HEIGHT はボスの弾の高さです。単位はピクセルです。
# BOSS_BULLET_HEIGHT に 48 を入れる
BOSS_BULLET_HEIGHT = 48
# BACKGROUND_SPEED は背景が画面を1回更新する間に下へ動く距離です。単位はピクセルです。
# BACKGROUND_SPEED に 2 を入れる
BACKGROUND_SPEED = 2
