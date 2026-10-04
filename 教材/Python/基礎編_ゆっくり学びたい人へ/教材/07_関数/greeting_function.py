# name を受け取り、挨拶文を返す関数です。
def make_greeting(name):
    return f"こんにちは {name}"


# 関数を呼び出し、返ってきた文字列を変数へ保存します。
message1 = make_greeting("たろう")
message2 = make_greeting("さくら")

# 関数が返した結果を表示します。
print(message1)
print(message2)
