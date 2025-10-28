from codrone_edu.drone import Drone

def move_test(drone: Drone):

    drone.hover(3)


    drone.move_forward(100,units="cm",speed=0.5)

    # drone.set_pitch(-100)
    # drone.move(2)