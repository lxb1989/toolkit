# Echo client program
import socket
import time

HOST = "192.168.1.10" # The UR IP address
PORT = 30002 # UR secondary client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def closeGripper():
    with open("gripper_close.script", "rb") as f:
        l = f.read(1024)
        while(l):
            s.send(l)
            l = f.read(1024)

def openGripper():
    with open("gripper_open.script", "rb") as f:
        l = f.read(1024)
        while(l):
            s.send(l)
            l = f.read(1024)

def activeGripper():
    with open("gripper_active.script", "rb") as f:
        l = f.read(1024)
        while(l):
            s.send(l)
            l = f.read(1024)

activeGripper()
time.sleep(1)
closeGripper()
time.sleep(1)
openGripper()
time.sleep(1)

s.close()
