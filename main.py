from codrone_edu.drone import *
# オブジェクト変数を生成
drone=Drone()
# ドローンとPCを接続する
drone.pair()
# 離陸する
drone.takeoff()
# 3秒ホバリング(空中で止まる)
drone.hover(3)
# 着陸する
drone.land()
# 接続を解除する
drone.close()
