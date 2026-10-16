# hit_enemiesは「弾が敵に重なったのに通り抜けた！」を防ぐため、重なった弾と敵を一覧から外します。
# 敵の移動へ命中時の削除も混ぜると追いにくいため、命中時の処理をcollisions.pyへまとめます。
# collisions（コリジョンズ）は衝突、hit_enemiesは敵への命中、hit_playerは自機への命中を扱います。Battle.updateがこの2つの処理を実行します。
# bulletsは自機の弾の一覧、enemiesは敵の一覧で、Battleが管理する元の一覧を受け取ります。
def hit_enemies(bullets, enemies):
    # bullets[:]は自機弾の並びを別の一覧へ写します。弾そのものは新しく作らず、同じ弾1発を両方の一覧から使えます。
    # hit_enemiesは確認用のコピーを読みます。元のbulletsから調べた弾を外しても、コピーに残る次の弾を続けて選べます。
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
                # hit_enemiesが同じ弾で次の敵への命中も調べ、その敵とも重なった場合、既に外した弾を再びremoveしてValueError（一覧に指定した弾がないエラー）になります。
                # breakは内側のfor enemy in enemies[:]（選んだ弾に重なる敵を探す繰り返し）だけを終えます。
                # 外側のfor bullet in bullets[:]は続き、hit_enemiesは次の弾についてenemiesに残っている敵を調べます。
                break

# hit_player（自機への命中）は「同じ敵弾で何度も体力が減った！」を防ぐため、命中した敵弾を外し、自機の体力を減らします。
# 敵弾の移動と命中後の対応を分けるため、Battle.updateがhit_playerを実行します。hit_playerは命中した敵弾1発ごとにplayer.take_damage()（自機の体力を1減らす処理）を実行します。
def hit_player(bullets, player):
    # bulletsはBattleの敵弾一覧self.enemy_bullets、playerはBattleの自機self.playerです。新しい弾や自機は作りません。
    # bullets[:]はfor開始時の敵弾一覧のコピーです。弾を作り直さず、元の一覧から弾を外してもコピーから次の弾を選べます。
    for bullet in bullets[:]:
        # rectは位置と大きさを持つ長方形です。colliderectは選んだ敵弾bullet.rectと自機player.rectの内側が重なるかを調べます。
        # colliderectは重なればTrue、辺だけの接触や離れた場合はFalseを返します。ifはTrueのときだけ、下の除外と体力変更を行います。
        if bullet.rect.colliderect(player.rect):
            # removeは指定した弾を一覧から外す操作です。元の敵弾一覧bulletsから、命中した弾bulletを外します。
            bullets.remove(bullet)
            # player.take_damage()は自機の体力を1減らします。外した敵弾は元の一覧に残らず、次の更新の命中判定に入りません。
            # hit_playerはbreak（繰り返しの打ち切り）を使いません。自機の体力が0以下でも、コピーに残る敵弾を調べ、命中した分だけ体力を減らします。
            player.take_damage()
