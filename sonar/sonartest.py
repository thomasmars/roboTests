import RPi.GPIO as GPIO
import time

# black/black
trigger = 16

# brown/white
echo = 18


GPIO.setmode(GPIO.BOARD)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

print "measure distance"

print "sending echo"
GPIO.output(trigger, False)

print "Waiting 2 sec"
time.sleep(2)

GPIO.output(trigger, True)
time.sleep(0.00001)
GPIO.output(trigger, False)

while GPIO.input(echo) == 0:
    pulse_start = time.time()

while GPIO.input(echo) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start
speed_of_sound = 34300
one_way_speed = speed_of_sound / 2

# speed * time = distance
distance = pulse_duration * one_way_speed
distance = round(distance, 2)

print "Distance:", distance, "cm"

GPIO.cleanup()
