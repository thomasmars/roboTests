import RPi.GPIO as GPIO
import time

MOTOR_1A = 11
# MOTOR_1B = 13
MOTOR_2A = 3
# MOTOR_2B = 5

print "Configuring..."
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_1A, GPIO.OUT)
# GPIO.setup(MOTOR_1B, GPIO.OUT)
GPIO.setup(MOTOR_2A, GPIO.OUT)
# GPIO.setup(MOTOR_2B, GPIO.OUT)

POWER_1A = GPIO.PWM(MOTOR_1A, 100)
POWER_2A = GPIO.PWM(MOTOR_2A, 100)

print("Testing motor " + str(MOTOR_1A))
# test_power(POWER_1A, 20, 50)
print "80% POWER"
POWER_1A.start(20)
POWER_2A.start(20)
time.sleep(2)
print "50% POWER"
POWER_1A.ChangeDutyCycle(50)
POWER_2A.ChangeDutyCycle(50)
time.sleep(2)
print "0% POWER"
POWER_1A.ChangeDutyCycle(100)
POWER_2A.ChangeDutyCycle(100)
time.sleep(2)
print "100% POWER"
POWER_1A.ChangeDutyCycle(0)
POWER_2A.ChangeDutyCycle(0)
time.sleep(2)
print "Stop!"
POWER_1A.stop()
POWER_2A.stop()

print "GPIO cleanup"
GPIO.cleanup()
