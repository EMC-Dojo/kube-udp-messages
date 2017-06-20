import socket
import os
import time



OUT_IP = os.getenv("OUT_IP") if os.getenv("OUT_IP") else os.getenv("UDPLISTEN_SERVICE_HOST")
OUT_PORT = int(os.getenv("OUT_PORT")) if os.getenv("OUT_PORT") else int(os.getenv("UDPLISTEN_SERVICE_PORT"))

print "OUT IP", OUT_IP
print "OUT PORT", OUT_PORT

sockout = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)

while True:
    MESSAGE = "IM HAVING THE "+ time.ctime()+ " OF MY LIFE"
    print "new MESSAGE \"", MESSAGE, "\""
    sockout.sendto(MESSAGE, (OUT_IP, OUT_PORT))
    time.sleep(1)
