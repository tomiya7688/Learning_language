# random は「無作為の」という意味
# Pythonに用意されている random の処理を使えるようにする
import random

# number は「数字」という意味
# number に1から10までの整数からランダムに選んだ値を入れる
number = random.randint(1, 10)
# 「出た数字:」と number を表示する
print("出た数字:", number)
