#!/usr/bin/env python3
import bluetooth
from ev3dev2.sound import Sound

sound = Sound()

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_sock.bind(("", port))
server_sock.listen(1)

sound.speak("Accepting connections on port " + str(port))

client_sock, address = server_sock.accept()
sound.speak("Accepted connection from " + str(address))

data = client_sock.recv(1024)
sound.speak("received " + str(data))

client_sock.close()
server_sock.close()
