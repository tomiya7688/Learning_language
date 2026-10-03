#include <stdio.h>

int main(void) {
    int score = 1250;
    int loaded_score = 0;

    FILE *file = fopen("game_result.txt", "w");

    if (file == NULL) {
        printf("保存用のファイルを開けませんでした。\n");
        return 1;
    }

    fprintf(file, "%d\n", score);
    fclose(file);

    file = fopen("game_result.txt", "r");

    if (file == NULL) {
        printf("読込用のファイルを開けませんでした。\n");
        return 1;
    }

    if (fscanf(file, "%d", &loaded_score) != 1) {
        printf("スコアを読み込めませんでした。\n");
        fclose(file);
        return 1;
    }

    fclose(file);

    printf("読み込んだスコア: %d点\n", loaded_score);

    return 0;
}
