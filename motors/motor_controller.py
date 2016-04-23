import RPi.GPIO as GPIO
import time
from threading import Thread

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
running = False

# Start all motors with 0%
power_1a.start(100)
power_1b.start(100)
power_2a.start(100)
power_2b.start(100)
power_1a_running = True
power_1b_running = True
power_2a_running = True
power_2b_running = True


def add_move(move):
    global running, moves_queue
    # Max 3 entries
    print "ADDING MOVE: " + str(move)
    print "array: " + str(moves_queue)
    print "moves queue length" + str(len(moves_queue))
    if len(moves_queue) < 3:
        moves_queue.append(move)

    print "Running ?" + str(running)
    if not running:
        print "Creating a new execute_move thread!"
        thread = Thread(target=execute_move)
        thread.start()


def execute_move():
    global running, moves_queue, power_1a, power_2a, power_1b, power_2b
    global power_1b_running, power_2b_running, power_1a_running, power_2a_running
    running = True
    print "executing move"
    print "move queue: " + str(moves_queue)
    move = moves_queue.pop(0)

    print "popped move: " + str(move)

    # Exit loop
    if move == "exit":
        return True

    # Execute move
    if move == "forward":
        forward()
    elif move == "forward_left":
        forward_left()
    elif move == "forward_right":
        forward_right()
    elif move == "backward":
        backward()
    elif move == "backward_left":
        backward_left()
    elif move == "backward_right":
        backward_right()

    # Wait 0.5 seconds
    print "Sleeping 3s"
    time.sleep(3)

    print "array length" + str(len(moves_queue))
    if len(moves_queue) >= 1:
        thread = Thread(target=execute_move)
        thread.start()
    else:
        print "TURNING OFF ALL MOTORS!"
        # Turn off all motors
        stop_motor(power_1a, power_1a_running)
        stop_motor(power_2a, power_2a_running)
        stop_motor(power_1b, power_1b_running)
        stop_motor(power_2b, power_2b_running)
        running = False


def forward_left():
    print "GOING FORWARD LEFT!"
    global power_1b, power_2b, power_1a, power_2a
    global power_1b_running, power_2b_running, power_1a_running, power_2a_running
    stop_motor(power_1b, power_1b_running)
    stop_motor(power_2b, power_2b_running)
    start_motor_with_cycle(power_1a, 50, power_1a_running)
    start_motor_with_cycle(power_2a, 0, power_2a_running)


def forward():
    print "GOING FOWARD!!"
    global power_1b, power_2b, power_1a, power_2a
    global power_1b_running, power_2b_running, power_1a_running, power_2a_running
    stop_motor(power_1b, power_1b_running)
    stop_motor(power_2b, power_2b_running)
    start_motor_with_cycle(power_1a, 0, power_1a_running)
    start_motor_with_cycle(power_2a, 0, power_2a_running)


def forward_right():
    print "GOING FORWARD RIGHT!"
    global power_1b, power_2b, power_1a, power_2a
    global power_1b_running, power_2b_running, power_1a_running, power_2a_running
    stop_motor(power_1b, power_1b_running)
    stop_motor(power_2b, power_2b_running)
    start_motor_with_cycle(power_1a, 0, power_1a_running)
    start_motor_with_cycle(power_2a, 50, power_2a_running)


def backward_left():
    print "GOING BACKWARD LEFT!"
    global power_1b, power_2b, power_1a, power_2a
    global power_1b_running, power_2b_running, power_1a_running, power_2a_running
    stop_motor(power_1a, power_1a_running)
    stop_motor(power_2a, power_2a_running)
    start_motor_with_cycle(power_1b, 50, power_1b_running)
    start_motor_with_cycle(power_2b, 0, power_2b_running)


def backward():
    print "GOING BACKWARD !"
    global power_1b, power_2b, power_1a, power_2a
    global power_1b_running, power_2b_running, power_1a_running, power_2a_running
    stop_motor(power_1a, power_1a_running)
    stop_motor(power_2a, power_2a_running)
    # Back a little slower, so it doesnt stall
    start_motor_with_cycle(power_1b, 30, power_1b_running)
    start_motor_with_cycle(power_2b, 30, power_2b_running)


def backward_right():
    print "GOING BACKWARD RIGHT!"
    global power_1b, power_2b, power_1a, power_2a
    global power_1b_running, power_2b_running, power_1a_running, power_2a_running
    stop_motor(power_1a, power_1a_running)
    stop_motor(power_2a, power_2a_running)
    start_motor_with_cycle(power_1b, 0, power_1b_running)
    start_motor_with_cycle(power_2b, 50, power_2b_running)


def stop_motor(pwm_motor, is_running):
    print "stop motor " + str(pwm_motor)
    print "is running " + str(is_running)
    # if is_running:
    #     pwm_motor.stop()
    pwm_motor.ChangeDutyCycle(100)


def start_motor_with_cycle(pwm_motor, cycle, is_running):
    print "Starting motor " + str(pwm_motor)
    print "cycle " + str(cycle)
    print "is running " + str(is_running)
    # if is_running:
    # else:
    #     pwm_motor.start(cycle)
    # pwm_motor.start(cycle)
    pwm_motor.ChangeDutyCycle(cycle)


gettingInput = True
while gettingInput:
    cmd = str(raw_input('Command ? (f,b,l,r,exit)'))
    print "input is: " + cmd
    if cmd == 'exit':
        print "exit"
        gettingInput = False
    elif cmd == 'f':
        print "forward"
        add_move("forward")
    elif cmd == 'fl':
        print "forward_left"
        add_move("forward_left")
    elif cmd == 'fr':
        print "forward_right"
        add_move("forward_right")
    elif cmd == 'b':
        print "backward"
        add_move("backward")
    elif cmd == 'bl':
        print "backward_left"
        add_move("backward_left")
    elif cmd == 'br':
        print "backward_right"
        add_move("backward_right")

print "GPIO cleanup"
power_1a.ChangeDutyCycle(100)
power_1b.ChangeDutyCycle(100)
power_2a.ChangeDutyCycle(100)
power_2b.ChangeDutyCycle(100)
power_1a.stop()
power_1b.stop()
power_2a.stop()
power_2b.stop()
GPIO.cleanup()
