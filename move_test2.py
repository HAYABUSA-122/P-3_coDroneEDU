from codrone_edu.drone import Drone

def move_test(drone: Drone):
#
#     # 3秒ホバリング(空中で止まる)
#     drone.hover(3)                                              # ホバリング 3s
#
#     # 以降処理毎に ホバリング(1s) を実行
#     drone.move_distance(0, 0, 0.7, 1)                           # 下降：0.7m, speed 1m/s
#     drone.hover(1)
#
#     drone.set_pitch(30)                                         # 前進：100cm, speed 1m/s
#     drone.set_roll(0)
#     drone.move(2)
#     drone.hover(1)
#
#     drone.move_distance(0, 0, 0.5, 1)                           # 上昇：0.5m, speed 1m/s
#     drone.hover(1)
#
#     drone.turn_right(180)                                       # 右旋回 180°
#     drone.hover(1)
#
#     drone.set_pitch(30)                                         # 前進：100cm, speed 1m/s
#     drone.set_roll(0)
#     drone.move(2)
#     drone.hover(1)
#
#     drone.move_distance(0, 0, -0.5, 1)                          # 下降：0.5m, speed 1m/s
#     drone.hover(1)
#
#     drone.turn_right(180)                                       # 右旋回 180°
#     drone.hover(1)
#
#     drone.set_pitch(30)                                         # 前進：100cm, speed 1m/s
#     drone.set_roll(0)
#     drone.move(2)
#     drone.hover(1)
#
#     drone.move_distance(0, 0, 0.5, 1)                           # 上昇：0.5m, speed 1m/s
#     drone.hover(1)
#
#     drone.turn_right(180)                                       # 右旋回 180°
#     drone.hover(1)
#
#     drone.set_pitch(30)                                         # 前進：100cm, speed 1m/s
#     drone.set_roll(0)
#     drone.move(2)
#
#     drone.hover(3)
#
#
#
#     # メモ
#
#     # # 前に移動
#     # drone.set_pitch(30)
#     # drone.set_roll(0)
#     # drone.move(2)
#
#     # # 右に移動
#     # drone.set_pitch(0)
#     # drone.set_roll(30)
#     # drone.move(2)
#
#     # # 後ろに移動
#     # drone.set_pitch(-30)
#     # drone.set_roll(0)
#     # drone.move(2)
#
#     # # 左に移動
#     # drone.set_pitch(0)
#     # drone.set_roll(-30)
#     # drone.move(2)


    # drone.set_roll(-30)
    # drone.move(0.78)
    # drone.reset_move_values()
    drone.hover(1)
    drone.move_forward(distance=82, units="cm",speed = 1)
    drone.hover(1)