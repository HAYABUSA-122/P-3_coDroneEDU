def emergency_stop(drone):
    drone.hover(3)
    drone.land()
    print("緊急停止しました")