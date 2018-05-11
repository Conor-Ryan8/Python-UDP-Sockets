#*****************************************************************************#
# Conor Ryan - Socket Programming - Python                                    #
# Basic UDP Client                                                            #
# May 2018                                                                    #
#*****************************************************************************#

import socket

IP = raw_input("IP Address? ")
type(IP)

PORT = input("Port Number? ")
type(PORT)

MESSAGE = raw_input("Enter Message: ")
type(MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (IP, PORT))
