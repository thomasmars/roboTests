import RPi.GPIO as GPIO
import time

MOTOR_1A = 11
MOTOR_1B = 13
MOTOR_2A = 3
MOTOR_2B = 5

print "Configuring..."
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_1A, GPIO.OUT)
GPIO.setup(MOTOR_1B, GPIO.OUT)
GPIO.setup(MOTOR_2A, GPIO.OUT)
GPIO.setup(MOTOR_2B, GPIO.OUT)

POWER_1A = GPIO.PWM(MOTOR_1A, 10)
POWER_1B = GPIO.PWM(MOTOR_1B, 10)
POWER_2A = GPIO.PWM(MOTOR_2A, 10)
POWER_2B = GPIO.PWM(MOTOR_2B, 10)


def set_output(motor, boolean):
    GPIO.output(motor, boolean)


def test_motor(motor):
    print "PIN" + str(motor) + " TRUE"
    set_output(motor, True)
    time.sleep(3)
    print "PIN" + str(motor) + " FALSE"
    set_output(motor, False)
    time.sleep(3)


# Not working yet
def test_power(power, duty1, duty2):
    print "POWER" + str(power) + " TRUE"
    power.start(duty1)
    time.sleep(3)
    print "PIN" + str(power) + " FALSE"
    power.ChangeDutyCycle(duty2)
    time.sleep(3)
    print "stop!"

test_power(POWER_1A, 10, 100)
test_power(POWER_2A, 10, 100)

print "GPIO cleanup"
GPIO.cleanup()
