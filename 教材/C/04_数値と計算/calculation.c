#include <stdio.h>

int main(void) {
    int answer = 42;
    int guess = 0;
    int difference = 0;

    printf("1から100までの数字を予想してください: ");
    scanf("%d", &guess);

    difference = guess - answer;

    printf("あなたの予想: %d\n", guess);
    printf("答え: %d\n", answer);
    printf("予想 - 答え = %d\n", difference);
    return 0;
}
