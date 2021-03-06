import RPi.GPIO as GPIO
import time
import threading


class SonarController:
    def __init__(self):
        # black/black
        self.trigger = 16

        # brown/white
        self.echo = 18

        speed_of_sound = 34300
        self.one_way_speed = speed_of_sound / 2
        self.running = True

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trigger, False)

    def get_distance(self):
        distance = self.catch_signal()
        return distance

    def trigger_signal(self):
        GPIO.output(self.trigger, False)
        time.sleep(0.01)
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

    def catch_signal(self):
        pulse_start = time.time()
        pulse_end = -1
        self.trigger_signal()
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()

        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        # speed * time = distance
        distance = pulse_duration * self.one_way_speed
        distance = round(distance, 2)
        return distance

    def on_distance(self, stop_distance, callback):
        if not self.running:
            return
        accuracy = []
        while (len(accuracy) <= 4) & self.running:
            distance = self.get_distance()
            if (distance < stop_distance) & (distance > 0):
                accuracy.append(distance)
            else:
                accuracy = []
            print "distance: ", str(distance)
            time.sleep(0.02)

        callback()

    def terminate(self):
        self.running = False
        GPIO.output(self.trigger, False)
