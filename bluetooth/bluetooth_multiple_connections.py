# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $
from threading import Thread

from bluetooth import *
from motors.motor_controller3 import MotorController

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(5)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service(server_sock, "SampleServer",
                   service_id=uuid,
                   service_classes=[uuid, SERIAL_PORT_CLASS],
                   profiles=[SERIAL_PORT_PROFILE])

print "Waiting for connection on RFCOMM channel %d" % port
ctrl = MotorController()


def start_client(cs, ci):
    print "Accepted connection from ", ci

    try:
        while True:
            print "Waiting for client data"
            data = cs.recv(1024)
            print "Received client data"
            if len(data) == 0:
                break
            print "received [%s]" % data
            ctrl.add_move(data)

    except IOError:
        pass

    print "Closing socket!"
    cs.close()

while True:
    print "main loop"
    print "Waiting for client"
    client_sock, client_info = server_sock.accept()
    print "Got client connection"
    Thread(target=start_client, args=(client_sock, client_info)).start()
print "disconnected"
server_sock.close()
print "all done"
