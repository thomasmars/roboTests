from motors.motor_controller3 import MotorController
from sonar.sonar_controller import SonarController
import RPi.GPIO as GPIO
import time
import threading

mc = MotorController()
sc = SonarController()
distance_threshold = 25
running = True


def terminate():
    global running
    print "wait for remaining processes"
    running = False
    time.sleep(3)
    print "Terminating!"
    mc.terminate()
    sc.terminate()
    time.sleep(2)
    GPIO.cleanup()


def back_up_and_turn_right():
    global running

    if running:
        print "Assess the situation!"
        mc.add_move("stop")
        time.sleep(1)

    # Back up for 0.5 seconds
    if running:
        print "backing up!"
        mc.add_move("backward")
        time.sleep(1)

    if running:
        print "Assess the situation!"
        mc.add_move("stop")
        time.sleep(1)

    if running:
        print "backward left!"
        mc.add_move("backward_left")
        time.sleep(0.5)

    if running:
        print "Assess the situation!"
        mc.add_move("stop")
        time.sleep(1)

    # Turn right for 0.5 seconds
    if running:
        print "turning right!"
        mc.add_move("forward_right")
        time.sleep(0.5)

    if running:
        print "Assess the situation!"
        mc.add_move("stop")
        time.sleep(1)

    # Continue exploring
    if running:
        mc.add_move("forward")
        sc.on_distance(distance_threshold, back_up_and_turn_right)
    else:
        mc.terminate()


def nothing():
    pass

threading.Timer(120, terminate).start()
mc.add_move("forward")
sc.on_distance(distance_threshold, back_up_and_turn_right)


# DEBUG SONAR
# threading.Timer(10, terminate).start()
# sc.on_distance(distance_threshold, nothing)
