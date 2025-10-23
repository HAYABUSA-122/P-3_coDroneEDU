import start
import emergency_stop
import move_test

from codrone_edu.drone import *

# オブジェクト変数を生成
drone=Drone()

try:
    start.start(drone) # ドローンを接続して離陸する

    move_test.move_test(drone)  # ドローンを動かすテスト

except KeyboardInterrupt:# プログラムの停止ボタンを押したらドローンを緊急着陸
    emergency_stop.emergency_stop(drone)

finally: # プログラム終了時に必ず実行する ドローン着陸　接続停止処理
    print("プログラムを終了します")
    drone.land()
    drone.close()
