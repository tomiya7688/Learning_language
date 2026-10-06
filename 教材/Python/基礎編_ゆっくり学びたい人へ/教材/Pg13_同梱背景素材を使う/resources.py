# pathlib から Path を読み込む
from pathlib import Path
# pygame を読み込む
import pygame

# load_image の処理を定義する
def load_image(name, size=None):
    # path は画像ファイルの場所です。
    # path に Path(__file__).parent / 'assets' / name を入れる
    path = Path(__file__).parent / "assets" / name
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
