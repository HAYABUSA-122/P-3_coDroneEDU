from codrone_edu.drone import *
# オブジェクト変数を生成
drone=Drone()
# ドローンとPCを接続する
drone.pair()


# 離陸する
drone.takeoff()


# 3秒ホバリング(空中で止まる)
drone.hover(3)

drone.move_forward(distance=100, units="cm", speed=1)
drone.move_backward(distance=50, units="cm", speed=1)
drone.move_left(distance=50, units="cm", speed=1)
drone.move_right(distance=50, units="cm", speed=1)

drone.turn_left(360)
drone.turn_right(360)

drone.hover(3)

# 着陸する
drone.land()


# 接続を解除する
drone.close()

#おあそびいいいいいい