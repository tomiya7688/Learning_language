#include <stdio.h>

void add_bonus(int *score, int bonus) {
    *score = *score + bonus;
}

int main(void) {
    int score = 250;

    printf("ボーナス前: %d点\n", score);
    add_bonus(&score, 100);
    printf("ボーナス後: %d点\n", score);

    return 0;
}
