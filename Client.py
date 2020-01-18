#*****************************************************************************#
# Conor Ryan - Socket Programming - Python                                    #
# Basic UDP Client                                                            #
# May 2018                                                                    #
#*****************************************************************************#
import socket
Address = "52.212.27.187"
Port = 5008
Message = "UDP Socket Test"
Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Socket.sendto(Message.encode(), (Address, Port))
