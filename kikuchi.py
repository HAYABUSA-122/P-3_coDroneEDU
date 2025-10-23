from codrone_edu.drone import *
# オブジェクト変数を生成
drone=Drone()


# ドローンとPCを接続する
drone.pair()
# 離陸する
drone.takeoff()


# 2秒ホバリング(空中で止まる)
drone.hover(2)
# 四角形の形でドローンが動く はず
drone.go("forward",30,1)
drone.hover(1)
drone.go("right",30,1)
drone.hover(1)
drone.go("backward",30,1)
drone.hover(1)
drone.go("left",30,1)
# 2秒ホバリング(空中で止まる)
drone.hover(2)


# 着陸する
drone.land()
# 接続を解除する
drone.close()
