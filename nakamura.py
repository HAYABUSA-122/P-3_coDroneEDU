def move_test(drone):


    drone.hover(3)

    drone.move_forward(distance=200, units="cm",speed = 1)
    drone.hover(1)
    drone.move_right(distance=200, units="cm", speed=1)
    drone.hover(1)
    drone.move_forward(distance=200, units="cm", speed=1)
    drone.hover(1)
    drone.move_left(distance=200, units="cm", speed=1)






