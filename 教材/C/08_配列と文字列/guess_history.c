#include <stdio.h>

#define MAX_GUESSES 10

int main(void) {
    const int answer = 42;
    char player_name[21];
    int guesses[MAX_GUESSES];
    int attempts = 0;
    int cleared = 0;

    printf("プレイヤー名を20文字以内の半角英数字で入力してください: ");

    if (scanf("%20s", player_name) != 1) {
        printf("名前を読み取れませんでした。\n");
        return 1;
    }

    printf("1から100までの数字を当ててください。\n");

    while (attempts < MAX_GUESSES && cleared == 0) {
        int guess;

        printf("%d回目の予想: ", attempts + 1);

        if (scanf("%d", &guess) != 1) {
            printf("数字ではないため終了します。\n");
            return 1;
        }

        if (guess < 1 || guess > 100) {
            printf("1から100までの数字を入力してください。\n");
            return 1;
        }

        guesses[attempts] = guess;
        attempts++;

        if (guess < answer) {
            printf("もっと大きい数字です。\n");
        } else if (guess > answer) {
            printf("もっと小さい数字です。\n");
        } else {
            cleared = 1;
        }
    }

    printf("\n%sさんの予想履歴: ", player_name);

    for (int i = 0; i < attempts; i++) {
        printf("%d ", guesses[i]);
    }

    printf("\n");

    if (cleared == 1) {
        printf("%d回で正解しました！\n", attempts);
    } else {
        printf("%d回以内に正解できませんでした。\n", MAX_GUESSES);
    }

    return 0;
}
