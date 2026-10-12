# make_greeting は「挨拶を作る」、name は「名前」という意味
# name で名前を受け取り、挨拶文を返す関数を定義する
def make_greeting(name):
    # name を組み込んだ挨拶の文字列を、呼び出した場所へ返す
    return f"こんにちは {name}"


# main は「主な」という意味。このプログラム全体の流れをまとめる
# 2人分の挨拶文を作り、順に表示する関数を定義する
def main():
    # message1 は「1人目の挨拶文」という意味
    # "たろう" で make_greeting を呼び出し、戻った文字列を message1 に代入する
    message1 = make_greeting("たろう")
    # message2 は「2人目の挨拶文」という意味
    # "さくら" で make_greeting を呼び出し、戻った文字列を message2 に代入する
    message2 = make_greeting("さくら")

    # message1 の文字列を画面に表示する
    print(message1)
    # message2 の文字列を画面に表示する
    print(message2)


# このファイルを直接実行した場合かどうかを調べる
if __name__ == "__main__":
    # プログラム全体の流れをまとめた main を呼び出す
    main()
