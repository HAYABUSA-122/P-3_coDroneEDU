from codrone_edu.drone import Drone
from oauthlib.common import generate_token

def move_test(drone: Drone):

    drone.hover(3)
    drone.reset_move_values()  # 値をリセット

    drone.set_pitch(20)
    drone.move(2)
    drone.reset_move_values()

    drone.set_pitch(-100)
    drone.move(2)