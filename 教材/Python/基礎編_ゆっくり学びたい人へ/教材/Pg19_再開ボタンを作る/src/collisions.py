# hit_enemiesは「弾が敵に重なったのに通り抜けた！」を防ぐため、重なった弾と敵を一覧から外します。
# 敵の移動へ命中時の削除も混ぜると追いにくいため、命中時の処理をcollisions.pyへまとめます。
# collisionsは衝突、hit_enemiesは敵への命中を扱う名前です。
# bulletsは自機の弾の一覧、enemiesは敵の一覧で、Battleが管理する元の一覧を受け取ります。
def hit_enemies(bullets, enemies):
    # bullets[:]は弾の一覧だけをコピーします。bullets[:]の各要素は、元のbulletsと同じ弾を指します。
    # hit_enemiesがbulletsから弾を外しても、bullets[:]には調べる弾が残るため、次の弾を飛ばしません。
    # 外側のforはbullets[:]から弾を1発ずつ選び、その1発をbullet（弾）という名前で使います。
    for bullet in bullets[:]:
        # hit_enemiesは弾を1発選ぶたびに、その時点の敵の一覧enemiesをenemies[:]でコピーします。
        # enemies[:]の各要素はenemiesと同じ敵を指し、hit_enemiesがenemiesから外した敵は入りません。
        # 内側のforはenemies[:]から敵を1機ずつ選び、その1機をenemy（敵）という名前で使います。
        for enemy in enemies[:]:
            # rectはrectangle（長方形）の略で、弾・敵の位置と大きさを表します。
            # colliderectは2つの長方形の重なりを調べる操作です。
            # 弾と敵の長方形が面積を持って重なるとcolliderectはTrue（成り立つ）を返します。
            # 辺が接するだけか、離れている場合、colliderectはFalse（成り立たない）を返します。
            # ifはcolliderectの判定がTrueのときだけ、下の削除とbreakを行います。
            if bullet.rect.colliderect(enemy.rect):
                # removeは指定した要素を一覧から外す操作です。
                # bullets.removeは当たった弾を、Battleが管理する元の弾一覧から外します。
                # 以後、Battleはbulletsから外したbulletを移動・描画しません。
                bullets.remove(bullet)
                # enemies.removeは当たった敵を、Battleが管理する元の敵一覧から外します。
                # 以後、Battleはenemiesから外したenemyを移動・描画しません。
                enemies.remove(enemy)
                # hit_enemiesが命中後も同じ弾で別の敵への命中を調べ続けると、重なった場合に同じ弾を2回removeしてエラーになります。
                # breakは内側のfor enemy in enemies[:]（選んだ弾に重なる敵を探す繰り返し）だけを終えます。
                # 外側のfor bullet in bullets[:]は続き、hit_enemiesは次の弾についてenemiesに残っている敵を調べます。
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
