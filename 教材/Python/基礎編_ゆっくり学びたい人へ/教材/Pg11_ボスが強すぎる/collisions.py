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

# hit_player の処理を定義する
def hit_player(bullets, player):
    # bullets[:] から bullet を1つずつ取り出して繰り返す
    for bullet in bullets[:]:
        # bullet.rect.colliderect(player.rect) が成り立つなら
        if bullet.rect.colliderect(player.rect):
            # bullets.remove(bullet) を実行する
            bullets.remove(bullet)
            # player.take_damage() を実行する
            player.take_damage()

# hit_boss の処理を定義する
def hit_boss(bullets, boss):
    # bullets[:] から bullet を1つずつ取り出して繰り返す
    for bullet in bullets[:]:
        # bullet.rect.colliderect(boss.rect) が成り立つなら
        if bullet.rect.colliderect(boss.rect):
            # bullets.remove(bullet) を実行する
            bullets.remove(bullet)
            # boss.take_damage() を実行する
            boss.take_damage()
