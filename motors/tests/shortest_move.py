import RPi.GPIO as GPIO
import time


def test():
    motor_1a = 11
    motor_1b = 13
    motor_2a = 3
    motor_2b = 5

    print "Configuring..."
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motor_1a, GPIO.OUT)
    GPIO.setup(motor_2a, GPIO.OUT)
    GPIO.setup(motor_1b, GPIO.OUT)
    GPIO.setup(motor_2b, GPIO.OUT)

    print "turning on frequency"
    power_1a = GPIO.PWM(motor_1a, 60)
    power_2a = GPIO.PWM(motor_2a, 60)
    power_1b = GPIO.PWM(motor_1b, 60)
    power_2b = GPIO.PWM(motor_2b, 60)

    print("Testing motor " + str(motor_1a))
    time.sleep(2)
    # test_power(power_1a, 20, 50)
    print "80 duty cycle, 60 hz 2 seconds"
    power_1b.start(100)
    power_2b.start(100)
    power_1a.start(50)
    power_2a.start(50)
    time.sleep(2)

    power_1a.stop()
    power_1b.stop()
    power_2a.stop()
    power_2b.stop()
    time.sleep(2)

    print "GPIO cleanup"
    GPIO.cleanup()

test()
