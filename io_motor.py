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


def drive(seconds, motor1, motor2=None):
    GPIO.output(motor1, True)
    if motor2 is not None:
        GPIO.output(motor2, True)
    time.sleep(seconds)
    if motor2 is not None:
        GPIO.output(motor1, False)
    GPIO.output(motor2, False)

running = True
while running:
    cmd = str(raw_input('Command ? (f,b,l,r,exit)'))
    print "input is: " + cmd
    if cmd == 'exit':
        print "exit"
        running = False
    elif cmd == 'f':
        print "forward"
        drive(0.5, MOTOR_1A, MOTOR_2A)
    elif cmd == 'b':
        print "backwards"
        drive(0.5, MOTOR_1B, MOTOR_2B)

print "GPIO cleanup"
GPIO.cleanup()
