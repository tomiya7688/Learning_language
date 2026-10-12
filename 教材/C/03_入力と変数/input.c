// printfとscanfを使うため、標準入出力の宣言を読み込む
#include <stdio.h>

// C言語のプログラムで最初に実行されるmain関数を書く
int main(void) {
    // 整数を保存する変数guessを作り、0を入れる
    int guess = 0;

    // 1から100の中から整数を1つ入力するよう案内する
    printf("1から100の中から整数を1つ入力してください: ");

    // 入力された整数を1つ読み取り、guessの保存場所へ書き込む
    scanf("%d", &guess);

    // %dをguessの値に置き換えて表示する
    printf("入力した数字は%dです。\n", guess);

    // 正常終了を表す0をOSへ返す
    return 0;
}
