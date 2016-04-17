import RPi.GPIO as GPIO
import time


def test():
    motor_1a = 11
    # MOTOR_1B = 13
    motor_2a = 3
    # MOTOR_2B = 5

    print "Configuring..."
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motor_1a, GPIO.OUT)
    # GPIO.setup(MOTOR_1B, GPIO.OUT)
    GPIO.setup(motor_2a, GPIO.OUT)
    # GPIO.setup(MOTOR_2B, GPIO.OUT)

    power_1a = GPIO.PWM(motor_1a, 100)
    power_2a = GPIO.PWM(motor_2a, 100)

    print("Testing motor " + str(motor_1a))
    # test_power(power_1a, 20, 50)
    print "80% POWER"
    power_1a.start(20)
    power_2a.start(20)
    time.sleep(2)
    print "50% POWER"
    power_1a.ChangeDutyCycle(50)
    power_2a.ChangeDutyCycle(50)
    time.sleep(2)
    print "0% POWER"
    power_1a.ChangeDutyCycle(100)
    power_2a.ChangeDutyCycle(100)
    time.sleep(2)
    print "100% POWER"
    power_1a.ChangeDutyCycle(0)
    power_2a.ChangeDutyCycle(0)
    time.sleep(2)
    print "Stop!"
    power_1a.stop()
    power_2a.stop()

    print "GPIO cleanup"
    GPIO.cleanup()



test()
