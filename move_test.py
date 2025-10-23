def move_test(drone):

    # 前に移動
    drone.set_pitch(30)
    drone.set_roll(0)
    drone.move(2)

    # 右に移動
    drone.set_pitch(0)
    drone.set_roll(30)
    drone.move(2)

    # 後ろに移動
    drone.set_pitch(-30)
    drone.set_roll(0)
    drone.move(2)

    # 左に移動
    drone.set_pitch(0)
    drone.set_roll(-30)
    drone.move(2)

    # 着陸
    drone.hover(1)
    drone.land()