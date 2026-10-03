#include <stdio.h>

int main(void) {
    int answer = 42;
    int guess = 0;

    printf("1から100までの数字を予想してください: ");

    if (scanf("%d", &guess) != 1) {
        printf("数字ではないため終了します。\n");
        return 1;
    }

    if (guess < 1 || guess > 100) {
        printf("1から100までの数字を入力してください。\n");
        return 1;
    }

    if (guess == answer) {
        printf("正解です！\n");
    } else if (guess > answer) {
        printf("もっと小さい数字です。\n");
    } else {
        printf("もっと大きい数字です。\n");
    }

    return 0;
}
