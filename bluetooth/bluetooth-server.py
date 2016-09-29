import sys

import bluetooth

from motors.tests.pwm_motor import test

#  create a socket on bluetooth
#  RFCOMM is one of several protocols bluetooth can use
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# choose a port number, must be same on client and server, 1 is fine
# port = bluetooth.PORT_ANY
port = bluetooth.PORT_ANY
# uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
uuid = "00001101-0000-1000-8000-00805f9b34fb"
print "USING UUID " + str(uuid)
# bind our socket to this port, the "" indicates we are happy to connect
# on any available bluetooth adapter
server_sock.bind(("", port))
print "listening"
# listen for any incoming connections
server_sock.listen(5)

# incoming_port = server_sock.getsockname()[1]
# print "SOCKET NAME" + str(incoming_port)

advertisemenet = bluetooth.advertise_service(server_sock, "Test server",
                                             service_id=uuid,
                                             service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                             profiles=[bluetooth.SERIAL_PORT_PROFILE]
                                             )


port = server_sock.getsockname()[1]

while True:

    print "WAITING for connection on RFCOMM channel %d" % port
    # accept connections and create the client socket
    client_sock, address = server_sock.accept()
    print("Accepted connection from ", address)
    # now everything is set-up we're ready to receive data
    try:
        print "not able to receive ??"
        data = client_sock.recv(1024)
        print "LEN data" + str(len(data))
        if len(data) == 0:
            break
        print str(data)

        if data == "drive":
            test()

        if data == "exit":
            break
    except:
        print "invalid socket!"
        print sys.exc_info()[0]
        break

    # print what we've received for debugging


    # now we've got data it's up to you want you want to do with it!
    # We recommend sending tuples and decoding them as speeds to send
    # ensure client and server are consistent

# when finished be sure to close your sockets
print "Exiting"
client_sock.close()
server_sock.close()
