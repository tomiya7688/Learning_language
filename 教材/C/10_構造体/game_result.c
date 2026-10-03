#include <stdio.h>

typedef struct {
    char player_name[32];
    int score;
    int cleared_stages;
} GameResult;

int main(void) {
    GameResult result = {"Player1", 1250, 4};

    printf("プレイヤー: %s\n", result.player_name);
    printf("スコア: %d点\n", result.score);
    printf("クリア数: %dステージ\n", result.cleared_stages);

    return 0;
}
