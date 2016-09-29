# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

from bluetooth import *
from motors.motor_controller2 import MotorController

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(5)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id=uuid,
                   service_classes=[uuid, SERIAL_PORT_CLASS],
                   profiles=[SERIAL_PORT_PROFILE])

print "Waiting for connection on RFCOMM channel %d" % port


print "Waiting for client"
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

ctrl = MotorController()
try:
    while True:
        print "Waiting for client data"
        data = client_sock.recv(1024)
        print "Received client data"
        if len(data) == 0:
            break
        print "received [%s]" % data
        if ctrl.add_move(data):
            continue
        # Handle other data here

except IOError:
    pass

print "Closing socket!"
client_sock.close()

print "disconnected"

server_sock.close()
print "all done"
