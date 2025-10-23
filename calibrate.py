import configparser
import keyboard
import emergency_stop
import time

# iniファイルからトリム値を読み込む関数
def load_trim_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        roll_trim = int(config['TRIM']['roll_trim'])
        pitch_trim = int(config['TRIM']['pitch_trim'])
    except (KeyError, ValueError):
        roll_trim = 0
        pitch_trim = 0

    return roll_trim,pitch_trim

# iniファイルにトリム値を書き込む関数
def save_trim_config(roll,pitch):

    config = configparser.ConfigParser()
    config.read('config.ini')

    config = configparser.ConfigParser()
    config['TRIM'] = {
        'roll_trim': str(roll),
        'pitch_trim': str(pitch),
    }

    # .iniファイルに書き込む
    try:
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print(f"トリム値を {'config.ini'} に保存しました。")
    except IOError as e:
        print(f"ファイルの保存中にエラーが発生しました: {e}")
        return None  # エラー時はNoneを返す

# ホバーしながらリアルタイムでトリム値を変更する関数
def set_trim_config(drone):

    try:

        drone.pair()

        # トリム値の設定を呼び出して設定　離陸
        roll_trim,pitch_trim = load_trim_config()
        print(f"ロール(左右)の現在のトリム値{roll_trim}")
        print(f"ピッチ(前後)の現在のトリム値{pitch_trim}")
        drone.set_trim(roll_trim, pitch_trim)
        drone.takeoff()


        # 最後にキーが押された時間
        last_keypress_time = 0

        while True:

            drone.hover(0.1)

            # チェンジのチェック
            trim_changed = False
            # 現在時刻の取得
            current_time = time.time()

            if current_time - last_keypress_time > 0.1:
                if keyboard.is_pressed('up'):      # 矢印↑を押すとピッチをプラス
                    pitch_trim += 1
                    trim_changed = True
                elif keyboard.is_pressed('down'):  # 矢印↓を押すとピッチをマイナス
                    pitch_trim -= 1
                    trim_changed = True
                elif keyboard.is_pressed('right'): # 矢印→を押すとロールをプラス
                    roll_trim += 1
                    trim_changed = True
                elif keyboard.is_pressed('left'):  # 矢印←を押すとロールをマイナス
                    roll_trim -= 1
                    trim_changed = True
                elif keyboard.is_pressed('q'):
                    print("Qが押されました　調整を終了します")
                    save_trim_config(roll_trim,pitch_trim)
                    break

                if trim_changed: # トリム値が変更されたらその値を表示
                    last_keypress_time = time.time()
                    print(f"\nロール(左右)の現在のトリム値{roll_trim}")
                    print(f"ピッチ(前後)の現在のトリム値{pitch_trim}")


    except KeyboardInterrupt:# プログラムの停止ボタンを押したらドローンを緊急着陸
        emergency_stop.emergency_stop(drone)

    finally:  # プログラム終了時に必ず実行する ドローン着陸　接続停止処理
        print("プログラムを終了します")
        drone.land()
        drone.close()

