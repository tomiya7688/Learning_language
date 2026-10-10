# hit_enemies の処理を定義する
def hit_enemies(bullets, enemies):
    # bullets[:] から bullet を1つずつ取り出して繰り返す
    for bullet in bullets[:]:
        # enemies[:] から enemy を1つずつ取り出して繰り返す
        for enemy in enemies[:]:
            # bullet.rect.colliderect(enemy.rect) が成り立つなら
            if bullet.rect.colliderect(enemy.rect):
                # bullets.remove(bullet) を実行する
                bullets.remove(bullet)
                # enemies.remove(enemy) を実行する
                enemies.remove(enemy)
                # この繰り返しを終える
                break
