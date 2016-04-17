import RPi.GPIO as GPIO
import time

print "Test!"

PIN_NUM = 11

print "Configuring..."
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUM, GPIO.OUT)

print "Lighting up!"
GPIO.output(PIN_NUM, True)

print "Sleeping 3sek"
time.sleep(3)

print "Light off"
GPIO.output(PIN_NUM, False)
