from codrone_edu.drone import Drone

PIPE_SHORT = 1  #0.2 (200ミリ)
PIPE_RONG = 1  #1.524 (1524ミリ)


def move_test(drone: Drone):

    drone.hover(1)
    drone.move_distance(PIPE_RONG, 0, 0,1)   # x = 3.5
    drone.hover(1)
    drone.move_distance(0, 0, -0.3, 0.5)
    drone.hover(1)
    drone.move_distance(PIPE_RONG, 0, 0, 0.2) # x = 3.048
    drone.hover(1)


