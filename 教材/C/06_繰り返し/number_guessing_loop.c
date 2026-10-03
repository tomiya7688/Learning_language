#include <stdio.h>

int main(void) {
    const int answer = 42;
    int guess = 0;
    int attempts = 0;

    printf("1から100までの数字を当ててください。\n");

    while (guess != answer) {
        printf("予想した数字: ");

        if (scanf("%d", &guess) != 1) {
            printf("数字ではないため終了します。\n");
            return 1;
        }

        if (guess < 1 || guess > 100) {
            printf("1から100までの数字を入力してください。\n");
            return 1;
        }

        attempts++;

        if (guess < answer) {
            printf("もっと大きい数字です。\n");
        } else if (guess > answer) {
            printf("もっと小さい数字です。\n");
        }
    }

    printf("正解です！ %d回で当たりました。\n", attempts);
    return 0;
}
