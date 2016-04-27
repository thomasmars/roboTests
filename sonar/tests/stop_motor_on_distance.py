from motors.motor_controller3 import MotorController
from sonar.sonar_controller import SonarController
import RPi.GPIO as GPIO

mc = MotorController()
sc = SonarController()

mc.add_move("forward")


def gpio_terminate():
    mc.terminate()
    sc.terminate()

# Stop motor on 40cm
sc.on_distance(40, gpio_terminate)
GPIO.cleanup()
