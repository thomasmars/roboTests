from sonar.sonar_controller import SonarController
import RPi.GPIO as GPIO

sonar_ctrl = SonarController()
stop_distance = 20


def distance_print():
    print "reached 20 cm"

if __name__ == '__main__':
    print "hello!"

    # sonar_ctrl.on_distance(stop_distance, distance_print)
    #
    # sonar_ctrl.terminate()
    # GPIO.cleanup()

