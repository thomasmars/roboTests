import RPi.GPIO as GPIO
import time
from threading import Thread


class MotorPWM():
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.motor_pin = pin
        self.pwm = GPIO.PWM(pin, 100)
        self.currentDutyCycle = 100
        self.halting = False
        self.pwm.start(100)
        self.cycles_per_second = 100

    def stop(self):
        self.wait_for_halt()
        self.currentDutyCycle = 100
        self.pwm.ChangeDutyCycle(100)

    def set_speed(self, cycle):
        self.wait_for_halt()
        if (cycle < 0) | (cycle > 100):
            self.currentDutyCycle = 100
            self.pwm.ChangeDutyCycle(100)
        else:
            self.currentDutyCycle = cycle
            self.pwm.ChangeDutyCycle(cycle)

    def terminate(self):
        self.pwm.ChangeDutyCycle(100)

    def wait_for_halt(self):
        # Cancel any running threads
        if self.halting:
            self.halting = False
            # Wait two cycles
            time.sleep(2 * (1 / float(self.cycles_per_second)))

    def slow_to_halt(self, time_to_halt):
        # Already halted
        if self.currentDutyCycle >= 100:
            return

        self.wait_for_halt()
        halt = Thread(target=self.halting_loop, args=[time_to_halt])
        halt.start()

    def halting_loop(self, time_to_halt):
        self.halting = True

        # calculations
        total_speed_change = 100 - self.currentDutyCycle
        speed_change_per_second = total_speed_change / time_to_halt
        speed_change_per_cycle = speed_change_per_second / float(self.cycles_per_second)

        # Change cycle
        while self.halting & (self.currentDutyCycle < 100):
            self.currentDutyCycle += speed_change_per_cycle
            # Cap at 100
            if self.currentDutyCycle > 100:
                self.currentDutyCycle = 100

            # Change duty cycle and wait for next
            self.pwm.ChangeDutyCycle(self.currentDutyCycle)
            time.sleep(1 / float(self.cycles_per_second))

        self.halting = False


class MotorController:
    moves = {
        'forward': [0, 0, -1, -1],
        'forward_left': [50, 0, -1, -1],
        'forward_right': [0, 50, -1, -1],
        'backward': [-1, -1, 30, 30],
        'slow_backward': [-1, -1, 90, 90],
        'backward_left': [-1, -1, 50, 0],
        'backward_right': [-1, -1, 0, 50],
        'stop': [-1, -1, -1, -1]
    }

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.motor_1a = MotorPWM(11)
        self.motor_1b = MotorPWM(13)
        self.motor_2a = MotorPWM(3)
        self.motor_2b = MotorPWM(5)
        self.moves_queue = []
        self.is_running = False
        self.max_queue = 5
        self.move_duration = 0.5

    def add_move(self, move):
        # Max entries
        if len(self.moves_queue) < self.max_queue:
            self.moves_queue.append(move)

        if not self.is_running:
            thread = Thread(target=self.execute_move)
            thread.start()

    def execute_move(self):
        self.is_running = True
        move = self.moves_queue.pop()

        # Execute move
        print "executing move", str(self.moves[move])
        self.change_speeds(*self.moves[move])

        # Wait for move
        time.sleep(self.move_duration)

        if len(self.moves_queue) >= 1:
            thread = Thread(target=self.execute_move)
            thread.start()
        else:
            self.is_running = False

    def change_speeds(self, speed_1a, speed_2a, speed_1b, speed_2b):
        self.motor_1a.set_speed(speed_1a)
        self.motor_2a.set_speed(speed_2a)
        self.motor_1b.set_speed(speed_1b)
        self.motor_2b.set_speed(speed_2b)

    def halt(self, halt_time):
        self.motor_1a.slow_to_halt(halt_time)
        self.motor_1b.slow_to_halt(halt_time)
        self.motor_2a.slow_to_halt(halt_time)
        self.motor_2b.slow_to_halt(halt_time)

    def instant_stop(self):
        self.change_speeds(100, 100, 100, 100)

    def terminate(self):
        self.motor_1a.terminate()
        self.motor_1b.terminate()
        self.motor_2a.terminate()
        self.motor_2b.terminate()
