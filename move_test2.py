def move_test(drone):

    # 3秒ホバリング(空中で止まる)
    drone.hover(3)                                              # ホバリング 3s

    # 以降処理毎に ホバリング(1s) を実行
    drone.move_distance(0, 0, 0.7, 1)                           # 下降：0.7m, speed 1m/s
    drone.hover(1)
    drone.move_forward(distance=100, units="cm", speed=1)       # 前進：100cm, speed 1m/s
    drone.hover(1)
    drone.move_distance(0, 0, 0.5, 1)                           # 上昇：0.5m, speed 1m/s
    drone.hover(1)
    drone.turn_right(180)                                       # 右旋回 180°
    drone.hover(1)
    drone.move_forward(distance=100, units="cm", speed=1)       # 前進：100cm, speed 1m/s
    drone.hover(1)
    drone.move_distance(0, 0, -0.5, 1)                          # 下降：0.5m, speed 1m/s
    drone.hover(1)
    drone.turn_right(180)                                       # 右旋回 180°
    drone.hover(1)
    drone.move_forward(distance=100, units="cm", speed=1)       # 前進：100cm, speed 1m/s
    drone.hover(1)
    drone.move_distance(0, 0, 0.5, 1)                           # 上昇：0.5m, speed 1m/s
    drone.hover(1)
    drone.turn_right(180)                                       # 右旋回 180°
    drone.hover(1)
    drone.move_forward(distance=100, units="cm", speed=1)       # 前進：100cm, speed 1m/s

    drone.hover(3)                                              # ホバリング 3s