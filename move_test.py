def move_test(drone):

    drone.hover(1)

    drone.set_throttle(-20)    # 下の力を設定
    drone.move(1)              # 値を参照して動かす
    drone.reset_move_values()  # 値をリセット

    drone.set_pitch(20)        # 前に傾ける
    drone.move(1)              # 値を参照して動かす
    drone.reset_move_values()  # 値をリセット

    drone.set_throttle(-20)    # 下の力を設定
    drone.move(1)              # 値を参照して動かす
    drone.reset_move_values()  # 値をリセット

    drone.set_pitch(-20)       # 後ろに傾ける
    drone.move(2)              # 値を参照して動かす
    drone.reset_move_values()  # 値をリセット

    drone.set_throttle(20)     # 上の力を設定
    drone.move(1)              # 値を参照して動かす
    drone.reset_move_values()  # 値をリセット

    drone.set_pitch(20)        # 前へ動かす
    drone.move(1)              # 値を参照して動かす
    drone.reset_move_values()  # 値をリセット

    # 着陸
    drone.hover(1)
    drone.land()