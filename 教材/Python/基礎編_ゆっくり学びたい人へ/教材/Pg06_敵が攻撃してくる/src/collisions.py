# hit_enemiesは「弾が敵に重なったのに通り抜けた！」を防ぐため、重なった弾と敵を一覧から外します。
# 敵の移動へ命中時の削除も混ぜると追いにくいため、命中時の処理をcollisions.pyへまとめます。
# collisions（コリジョンズ）は衝突、hit_enemiesは敵への命中。Battle.updateがこのファイルのhit_enemiesとhit_playerを実行します。
# bulletsは自機の弾の一覧、enemiesは敵の一覧で、Battleが管理する元の一覧を受け取ります。
def hit_enemies(bullets, enemies):
    # bullets[:]は自機弾の並びを別の一覧へ写します。弾そのものは新しく作らず、同じ弾1発を両方の一覧から使えます。
    # hit_enemiesは確認用のコピーを読みます。元のbulletsから弾Aを外しても、コピーの次の弾Bを続けて選べます。
    # 外側のforはbullets[:]から弾を1発ずつ選び、その1発をbullet（弾）という名前で使います。
    for bullet in bullets[:]:
        # hit_enemiesは弾を1発選ぶたびに、その時点の敵の一覧enemiesをenemies[:]でコピーします。
        # enemies[:]の各要素はenemiesと同じ敵を指します。hit_enemiesが前の弾でenemiesから外した敵は、新しいenemies[:]へ入りません。
        # 内側のforはenemies[:]から敵を1機ずつ選び、その1機をenemy（敵）という名前で使います。
        for enemy in enemies[:]:
            # rectはrectangle（長方形）の略で、弾・敵の位置と大きさを表します。
            # colliderectは2つの長方形の重なりを調べる操作です。
            # 弾と敵の長方形が面積を持って重なるとcolliderectはTrue（成り立つ）を返します。
            # 弾と敵の長方形の辺が接するだけか、弾と敵の長方形が離れている場合、colliderectはFalse（成り立たない）を返します。
            # ifはbullet.rect.colliderect(enemy.rect)がTrueのときだけ、bullets.remove(bullet)とenemies.remove(enemy)を行います。
            if bullet.rect.colliderect(enemy.rect):
                # removeは指定した要素を一覧から外す操作です。
                # bullets.removeは当たった弾を、Battleが管理する元の弾一覧から外します。
                # 以後、Battleはbulletsから外したbulletを移動・描画しません。
                bullets.remove(bullet)
                # enemies.removeは当たった敵を、Battleが管理する元の敵一覧から外します。
                # 以後、Battleはenemiesから外したenemyを移動・描画しません。
                enemies.remove(enemy)
                # hit_enemiesは自機弾1発につき敵1機で命中判定を止めます。除外した弾で別の敵を調べ続けないためです。
                # breakは内側のfor enemy in enemies[:]（選んだ弾に重なる敵を探す繰り返し）だけを終えます。
                # 外側のfor bullet in bullets[:]は続き、hit_enemiesは次の弾についてenemiesに残っている敵を調べます。
                break

# hit_player（自機への命中）は、敵弾の移動へ一覧の除外と体力変更まで混ぜないよう、命中した弾の除外と自機へのダメージをまとめる処理です。
# Battle.updateが、戦闘の敵弾一覧self.enemy_bulletsをbullets、自機self.playerをplayerへ指定します。各引数は元の一覧・自機と同じものを指します。
def hit_player(bullets, player):
    # hit_playerは一覧から弾を外しても次の弾を飛ばさないよう、bullets[:]で敵弾の一覧だけをコピーします。弾自体を新しく作る操作ではありません。
    # forがコピーbullets[:]の各弾をbullet（選んだ弾）へ1発ずつ選びます。元のbulletsとコピーは同じ弾を指します。
    for bullet in bullets[:]:
        # rectはrectangle（長方形）の略。colliderectが選んだ弾bullet.rectと自機player.rectの長方形に面積の重なりがあるかを返します。
        # hit_playerはTrue（重なる）の場合だけ、元の敵弾一覧からの除外と自機へのダメージを行います。辺だけの接触や離れた場合はFalseで、弾と体力を変更しません。
        if bullet.rect.colliderect(player.rect):
            # removeが選んだ弾bulletを元のbullets、つまりBattleのself.enemy_bulletsから直接外します。以後その弾は移動・描画・再判定されません。
            bullets.remove(bullet)
            # Player.take_damageが指定された自機playerのHP（体力）を1減らします。命中した弾を外すので、同じ弾で次の更新も体力を減らしません。
            # hit_playerにはbreak（繰り返しの打ち切り）やHPの確認がないため、コピーに残る次の弾も調べ、命中した弾ごとに体力を減らします。
            player.take_damage()
