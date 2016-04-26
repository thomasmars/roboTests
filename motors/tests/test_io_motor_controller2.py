from motors.motor_controller2 import MotorController
# INPUT for debugging purposes:

ctrl = MotorController()
gettingInput = True
while gettingInput:
    cmd = str(raw_input('Command ? (f,b,l,r,exit)'))
    print "input is: " + cmd
    if cmd == 'exit':
        print "exit"
        ctrl.terminate()
    elif cmd == 'f':
        print "forward"
        ctrl.add_move("forward")
    elif cmd == 'fl':
        print "forward_left"
        ctrl.add_move("forward_left")
    elif cmd == 'fr':
        print "forward_right"
        ctrl.add_move("forward_right")
    elif cmd == 'b':
        print "backward"
        ctrl.add_move("backward")
    elif cmd == 'bl':
        print "backward_left"
        ctrl.add_move("backward_left")
    elif cmd == 'br':
        print "backward_right"
        ctrl.add_move("backward_right")
