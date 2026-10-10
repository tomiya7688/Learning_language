# 「弾が敵に重なったのに通り抜けた！」を防ぐため、重なった弾と敵を一覧から外します。
# 敵の移動へ命中時の削除も混ぜると追いにくいため、このファイルへまとめます。
# collisionsは衝突、hit_enemiesは敵への命中を扱う名前です。
# bulletsは自機の弾の一覧、enemiesは敵の一覧で、Battleが管理する元の一覧を受け取ります。
def hit_enemies(bullets, enemies):
    # bullets[:]は弾の一覧だけをコピーします。コピーの中も、元と同じ弾を指します。
    # 元の一覧から弾を外しても、コピーには調べる弾が残るため、次の弾を飛ばしません。
    # forはコピーから弾を1発ずつ選び、その1発をbullet（弾）という名前で使います。
    for bullet in bullets[:]:
        # 弾を1発選ぶたびに、その時点で残っている敵の一覧をenemies[:]でコピーします。
        # コピーの中も元と同じ敵を指し、前の弾で一覧から外した敵は入りません。
        # forはコピーから敵を1機ずつ選び、その1機をenemy（敵）という名前で使います。
        for enemy in enemies[:]:
            # rectはrectangle（長方形）の略で、弾・敵の位置と大きさを表します。
            # colliderectは2つの長方形の重なりを調べる操作です。
            # 弾と敵の長方形が面積を持って重なるとcolliderectはTrue（成り立つ）を返します。
            # 辺が接するだけか、離れている場合、colliderectはFalse（成り立たない）を返します。
            # ifは判定がTrueのときだけ、下の削除とbreakを行います。
            if bullet.rect.colliderect(enemy.rect):
                # removeは指定した要素を一覧から外す操作です。
                # bullets.removeは当たった弾を、Battleが管理する元の弾一覧から外します。
                # 以後、Battleはこの弾を移動・描画しません。
                bullets.remove(bullet)
                # enemies.removeは当たった敵を、Battleが管理する元の敵一覧から外します。
                # 以後、Battleはこの敵を移動・描画しません。
                enemies.remove(enemy)
                # 消費した弾を別の敵にも当てると、同じ弾を2回removeしてエラーになります。
                # breakは内側の「この弾に重なる敵を探す」繰り返しだけを終えます。
                # 外側の繰り返しは続き、次の弾について、残っている敵を調べます。
                break
