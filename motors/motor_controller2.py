import RPi.GPIO as GPIO
import time
from threading import Thread


class MotorPWM:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.motor_pin = pin
        self.pwm = GPIO.PWM(pin, 100)

    def start(self):
        self.pwm.start(100)

    def stop(self):
        self.pwm.ChangeDutyCycle(100)

    def set_speed(self, cycle):
        if cycle < 0:
            self.pwm.ChangeDutyCycle(100)
        else:
            self.pwm.ChangeDutyCycle(cycle)

    def terminate(self):
        self.pwm.ChangeDutyCycle(100)
        self.pwm.stop()


class MotorController:
    moves = {
        'forward': [0, 0, -1, -1],
        'forward_left': [50, 0, -1, -1],
        'forward_right': [0, 50, -1, -1],
        'backward': [-1, -1, 30, 30],
        'backward_left': [-1, -1, 50, 0],
        'backward_right': [-1, -1, 0, 50]
    }

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.motor_1a = MotorPWM(11)
        self.motor_1b = MotorPWM(13)
        self.motor_2a = MotorPWM(3)
        self.motor_2b = MotorPWM(5)
        self.motor_1a.start()
        self.motor_1b.start()
        self.motor_2a.start()
        self.motor_2b.start()
        self.moves_queue = []
        self.is_running = False
        self.max_queue = 5
        self.move_duration = 0.5

    def add_move(self, move):
        # Max entries
        if len(self.moves_queue) < self.max_queue:
            print "added move to queue"
            self.moves_queue.append(move)

        print "Are we running ? " + str(self.is_running)
        if not self.is_running:
            print "Creating a new execute_move thread!"
            thread = Thread(target=self.execute_move)
            thread.start()

    def execute_move(self):
        self.is_running = True
        move = self.moves_queue.pop()

        # Execute move
        print "Change speeds " + str(self.moves[move])
        self.change_speeds(*self.moves[move])

        # Wait for move
        print "Sleeping " + str(self.move_duration)
        time.sleep(self.move_duration)

        print "What is moves queue ? " + str(self.moves_queue)
        print "What is length ? " + str(len(self.moves_queue))
        if len(self.moves_queue) >= 1:
            print "Next move"
            thread = Thread(target=self.execute_move)
            thread.start()
        else:
            print "TURNING OFF ALL MOTORS!"
            # Turn off all motors
            self.motor_1a.stop()
            self.motor_1b.stop()
            self.motor_2a.stop()
            self.motor_2b.stop()
            self.is_running = False

    def change_speeds(self, speed_1a, speed_2a, speed_1b, speed_2b):
        self.motor_1a.set_speed(speed_1a)
        self.motor_2a.set_speed(speed_2a)
        self.motor_1b.set_speed(speed_1b)
        self.motor_2b.set_speed(speed_2b)

    def terminate(self):
        print "EXITING cleanup"
        self.motor_1a.terminate()
        self.motor_1b.terminate()
        self.motor_2a.terminate()
        self.motor_2b.terminate()
        GPIO.cleanup()

# INPUT for debugging purposes:

# ctrl = MotorController()
# gettingInput = True
# while gettingInput:
#     cmd = str(raw_input('Command ? (f,b,l,r,exit)'))
#     print "input is: " + cmd
#     if cmd == 'exit':
#         print "exit"
#         ctrl.terminate()
#     elif cmd == 'f':
#         print "forward"
#         ctrl.add_move("forward")
#     elif cmd == 'fl':
#         print "forward_left"
#         ctrl.add_move("forward_left")
#     elif cmd == 'fr':
#         print "forward_right"
#         ctrl.add_move("forward_right")
#     elif cmd == 'b':
#         print "backward"
#         ctrl.add_move("backward")
#     elif cmd == 'bl':
#         print "backward_left"
#         ctrl.add_move("backward_left")
#     elif cmd == 'br':
#         print "backward_right"
#         ctrl.add_move("backward_right")
