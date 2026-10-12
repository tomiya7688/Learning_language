// printfとscanfを使うため、標準入出力の宣言を読み込む
#include <stdio.h>

// C言語のプログラムで最初に実行されるmain関数を書く
int main(void) {
    // 数当てゲームの答えを保存する
    int answer = 42;

    // 入力された予想を保存する
    int guess = 0;

    // 予想と答えの差を保存する
    int difference = 0;

    // 入力を促す文章を表示する
    printf("1から100までの数字を予想してください: ");

    // 入力された整数をguessの保存場所へ書き込む
    scanf("%d", &guess);

    // 予想から答えを引き、差を保存する
    difference = guess - answer;

    // 入力された予想を表示する
    printf("あなたの予想: %d\n", guess);

    // プログラムに設定した答えを表示する
    printf("答え: %d\n", answer);

    // 計算した差を表示する
    printf("予想 - 答え = %d\n", difference);

    // 正常終了を表す0をOSへ返す
    return 0;
}
