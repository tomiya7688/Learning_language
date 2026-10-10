# pathlib から Path を読み込む
from pathlib import Path
# pygame を読み込む
import pygame

# load_image の処理を定義する
def load_image(name, size=None):
    # path は画像ファイルの場所です。
    # path に Path(__file__).parent.parent / 'assets' / name を入れる
    path = Path(__file__).parent.parent / "assets" / name
    # image は画像。画面へ描く内容を持ちます。
    # image に pygame.image.load(str(path)).convert_alpha() を入れる
    image = pygame.image.load(str(path)).convert_alpha()
    # size is not None が成り立つなら
    if size is not None:
        # image は画像。画面へ描く内容を持ちます。
        # image に pygame.transform.scale(image, size) を入れる
        image = pygame.transform.scale(image, size)
    # image を返す
    return image

# Images という型を定義する
class Images:
    # __init__ の処理を定義する
    def __init__(self):
        # player はプレイヤー。ここでは操作する自機です。
        # self.player に load_image('player_ship.png') を入れる
        self.player = load_image("player_ship.png")
        # enemy は敵。通常の敵1機を表します。
        # self.enemy に load_image('enemy_ship.png') を入れる
        self.enemy = load_image("enemy_ship.png")
        # boss はボス。通常の敵が全ていなくなった後に登場します。
        # self.boss に load_image('boss_ship.png') を入れる
        self.boss = load_image("boss_ship.png")
