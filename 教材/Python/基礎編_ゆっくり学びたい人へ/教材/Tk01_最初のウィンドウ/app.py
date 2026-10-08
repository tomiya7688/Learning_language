# tkinterを、このプログラムで使えるようにする
import tkinter

# window に tkinterのTkクラスから作ったウィンドウを入れる
window = tkinter.Tk()

# window のタイトルを「はじめてのGUI」にする
window.title("はじめてのGUI")

# window の大きさを横400、縦300にする
window.geometry("400x300")

# window の画面を表示し、操作を待ち続ける
window.mainloop()
