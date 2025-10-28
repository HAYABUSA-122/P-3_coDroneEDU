from codrone_edu.drone import Drone


def move_test(drone: Drone):

    drone.hover(3)
    drone.reset_move_values()  # 値をリセット

    drone.set_pitch(20)
    drone.move(2)
    drone.reset_move_values()