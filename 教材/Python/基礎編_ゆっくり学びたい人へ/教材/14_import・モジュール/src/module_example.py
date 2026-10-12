# 別ファイルの message_tools を使えるようにします。
import message_tools

# 挨拶文を作り、message1 に保存します。
message1 = message_tools.make_greeting("たろう")
# 別れの挨拶を作り、message2 に保存します。
message2 = message_tools.make_goodbye("さくら")

print(message1)
print(message2)
