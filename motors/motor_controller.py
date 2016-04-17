import RPi.GPIO as GPIO
import time

motor_1a = 11
motor_1b = 13
motor_2a = 3
motor_2b = 5

print "Configuring..."
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_1a, GPIO.OUT)
GPIO.setup(motor_1b, GPIO.OUT)
GPIO.setup(motor_2a, GPIO.OUT)
GPIO.setup(motor_2b, GPIO.OUT)

power_1a = GPIO.PWM(motor_1a, 100)
power_1b = GPIO.PWM(motor_1b, 100)
power_2a = GPIO.PWM(motor_2a, 100)
power_2b = GPIO.PWM(motor_2b, 100)

# Max 3 moves queued
moves_queue = []


def motor_run():
    while True:
        if execute_move():
            break


def add_move(move):
    # Max 3 entries
    if len(moves_queue) < 3:
        moves_queue.append(move)

    execute_move()


def execute_move():
    print "executing move"
    if len(moves_queue) == 0:

        # Turn off all motors
        power_1a.ChangeDutyCycle(100)
        power_1b.ChangeDutyCycle(100)
        power_2a.ChangeDutyCycle(100)
        power_2b.ChangeDutyCycle(100)

        return False
    print "move queue: " + str(moves_queue)
    move = moves_queue.pop()

    print "popped move: " + str(move)

    # Exit loop
    if move == "exit":
        return True

    # Execute move
    if move == "forward":
        forward()
    elif move == "forward_left":
        forward_left()
    elif move == "backward":
        backward()

    # Wait 0.5 seconds
    time.sleep(0.5)
    return False


def forward_left():
    start_motor_with_cycle(power_1a, 50)
    start_motor_with_cycle(power_2a, 0)


def forward():
    print "GOING FOWARD!!"
    start_motor_with_cycle(power_1a, 0)
    start_motor_with_cycle(power_2a, 0)


def forward_right():
    start_motor_with_cycle(power_1a, 50)
    start_motor_with_cycle(power_2a, 0)


def backward_left():
    start_motor_with_cycle(power_1b, 50)
    start_motor_with_cycle(power_2b, 0)


def backward():
    start_motor_with_cycle(power_1b, 0)
    start_motor_with_cycle(power_2b, 0)


def backward_righ():
    start_motor_with_cycle(power_1b, 0)
    start_motor_with_cycle(power_2b, 50)


def start_motor_with_cycle(pwm_motor, cycle):
    # pwm_motor.ChangeDutyCycle(cycle)
    pwm_motor.start(cycle)
    # Wait 0.5 seconds
    time.sleep(0.5)
    pwm_motor.stop()


add_move("forward")
add_move("backward")
add_move("forward_left")
add_move("forward_right")