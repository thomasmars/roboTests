import RPi.GPIO as GPIO
import time
import sys

# TODO: Create commands that will move the robot around in any direction
commands = ['f', 'b', 'fr', 'br', 'fl', 'bl']

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

# Forward left and right
# TODO: Figure out if 1 is left and 2 is right
power_1a = GPIO.PWM(motor_1a, 20)
power_2a = GPIO.PWM(motor_2a, 20)

# Backward left and rightf
power_1b = GPIO.PWM(motor_1b, 20)
power_2b = GPIO.PWM(motor_2b, 20)

time.sleep(1)
# 80 duty cycle, 60 hz 2 seconds

gettingInput = True


# Set speed of different motors
def stop():
    power_1a.stop()
    power_1b.stop()
    power_2a.stop()
    power_2b.stop()
    time.sleep(2)


def output():
    print 'output from python, Hello Thomas'

if __name__ == '__main__':

    print 'bubu'
    print "args", len(sys.argv)
    print "args list", str(sys.argv)
    print "arg 1 ", str(sys.argv[0])
    output()

    cmd = sys.argv[1]
    print "input is: " + cmd
    if cmd == 'exit':
        isIdle = False
        gettingInput = False
        print "exit"
        stop()
    elif cmd == 'f':
        isIdle = False
        print "forward"
        power_1b.start(100)
        power_2b.start(100)
        power_1a.start(40)
        power_2a.start(40)
        time.sleep(2)
        stop()
    elif cmd == 'fl':
        isIdle = False
        print "fl"
        power_1b.start(100)
        power_2b.start(100)
        power_1a.start(40)
        power_2a.start(80)
        time.sleep(2)
        stop()
    elif cmd == 'fr':
        print "forward_right"
        isIdle = False
        power_1b.start(100)
        power_2b.start(100)
        power_1a.start(80)
        power_2a.start(40)
        time.sleep(2)
        stop()
    elif cmd == 'b':
        print "backward"
        isIdle = False
        power_1b.start(40)
        power_2b.start(40)
        power_1a.start(100)
        power_2a.start(100)
        time.sleep(2)
        stop()
    elif cmd == 'bl':
        print "backward_left"
        isIdle = False
        power_1b.start(40)
        power_2b.start(80)
        power_1a.start(100)
        power_2a.start(100)
        time.sleep(2)
        stop()
    elif cmd == 'br':
        print "backward_right"
        isIdle = False
        power_1b.start(80)
        power_2b.start(40)
        power_1a.start(100)
        power_2a.start(100)
        time.sleep(2)
        stop()

    GPIO.cleanup()
