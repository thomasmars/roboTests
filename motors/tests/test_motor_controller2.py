from motors.motor_controller2 import MotorController
import time

# Test Halting Loop
ctrl = MotorController()
print "go forward"
ctrl.add_move("forward")
print "Wait 2 seconds"
time.sleep(1)
print "Now halt"
halt_time = 3
ctrl.halt(halt_time)
time.sleep(halt_time / float(2))
print "Move forward"
ctrl.add_move("forward")
time.sleep(2)
print "Double halt"
ctrl.halt(1)
time.sleep(0.5)
ctrl.halt(4)
time.sleep(5)
print "backward"
ctrl.add_move("backward")
time.sleep(1)
ctrl.halt(3)
time.sleep(3)
print "Forward left"
ctrl.add_move("forward_left")
time.sleep(4)
ctrl.halt(4)
time.sleep(6)
ctrl.add_move("forward")
time.sleep(1)
print "5 sec halt"
ctrl.halt(5)
time.sleep(2)
ctrl.halt(1)
time.sleep(3)
ctrl.terminate()
