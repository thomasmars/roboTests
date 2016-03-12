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


def set_output(motor, boolean):
    GPIO.output(motor, boolean)
    
    
def test_motor(motor):
    print "PIN" + str(motor) + " TRUE"
    set_output(motor, True)
    time.sleep(3)
    print "PIN" + str(motor) + " FALSE"
    set_output(motor, False)
    time.sleep(3)

test_motor(MOTOR_1A)
test_motor(MOTOR_1B)
test_motor(MOTOR_2A)
test_motor(MOTOR_2B)

GPIO.output(MOTOR_1A, True)

print "GPIO cleanup"
GPIO.cleanup()
