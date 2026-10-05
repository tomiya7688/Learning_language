# answer は「返答」という意味
# answer に何も文字がない文字列を入れる
answer = ""

# answer が「終了」でない間、下の処理を繰り返す
while answer != "終了":
    # answer に「終了するには「終了」と入力してください: 」と表示して入力された内容を入れる
    answer = input("終了するには「終了」と入力してください: ")
    # answer が「終了」でなければ、次の行を実行する
    if answer != "終了":
        # 「入力した内容:」と answer を表示する
        print("入力した内容:", answer)

# 「終了しました」と表示する
print("終了しました")
