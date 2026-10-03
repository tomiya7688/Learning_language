#include <stdio.h>

void show_hint(int guess, int answer) {
    if (guess < answer) {
        printf("もっと大きい数字です。\n");
    } else if (guess > answer) {
        printf("もっと小さい数字です。\n");
    } else {
        printf("正解です！\n");
    }
}

int calculate_score(int attempts) {
    int score = 100 - (attempts - 1) * 10;

    if (score < 10) {
        return 10;
    }

    return score;
}

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
        show_hint(guess, answer);
    }

    printf("挑戦回数: %d回\n", attempts);
    printf("スコア: %d点\n", calculate_score(attempts));
    return 0;
}
