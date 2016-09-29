# from sonar.sonar_controller import SonarController
import RPi.GPIO as GPIO
import imp
sc = imp.load_source('SonarController', '/home/bananapi/pyProjects/sonar/sonar_controller.py')
sonar_ctrl = sc.SonarController()
stop_distance = 20


def distance_print():
    print "reached 20 cm"

if __name__ == '__main__':
    print "hello!"

    sonar_ctrl.on_distance(stop_distance, distance_print)
    sonar_ctrl.terminate()
    GPIO.cleanup()
