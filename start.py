import calibrate

def start(drone):
    try:
        # ドローンとPCを接続する
        drone.pair()
        # # トリム値を設定
        # drone.set_trim(calibrate.load_trim_config())
        # 離陸する
        drone.takeoff()
        # 1秒ホバリング(空中で止まる)
        drone.hover(1)
    except TimeoutError:
        print("ドローンとの接続が失敗しました")