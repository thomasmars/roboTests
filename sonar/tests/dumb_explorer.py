from motors.motor_controller3 import MotorController
from sonar.sonar_controller import SonarController
import RPi.GPIO as GPIO
import time
import threading

mc = MotorController()
sc = SonarController()
distance_threshold = 40
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
    # Back up for 0.5 seconds
    if running:
        print "backing up!"
        mc.add_move("slow_backward")
        time.sleep(0.5)

    if running:
        print "back left!"
        mc.add_move("backward_left")
        time.sleep(0.5)

    # Turn right for 0.5 seconds
    if running:
        print "turning right!"
        mc.add_move("forward_right")
        time.sleep(0.5)

    # Continue exploring
    if running:
        mc.add_move("forward")
        sc.on_distance(distance_threshold, back_up_and_turn_right)
    else:
        mc.terminate()

threading.Timer(80, terminate).start()
mc.add_move("forward")
sc.on_distance(distance_threshold, back_up_and_turn_right)
