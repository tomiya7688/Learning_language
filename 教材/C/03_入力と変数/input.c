#include <stdio.h>

int main(void) {
    int guess = 0;

    printf("1から100までの数字を入力してください: ");
    scanf("%d", &guess);

    printf("入力した数字は%dです。\n", guess);
    return 0;
}
