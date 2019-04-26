#!/usr/bin/python3
import socket
import time
import struct
import math

robot_ip = "192.168.1.10" # The remote robot_ip
port = 30003

print("Starting Program")

def get_pos():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((robot_ip, port))
        s.send("get_state()"+"\n")
        time.sleep(1)
        packet_1 = s.recv(444)
 
        packet_12 = s.recv(8)
        packet_12 = packet_12.encode("hex") #convert the data from \x hex notation to plain hex
        x = str(packet_12)
        x = struct.unpack('!d', packet_12.decode('hex'))[0]
        print("X = ", x * 1000) 

        packet_13 = s.recv(8)
        packet_13 = packet_13.encode("hex") #convert the data from \x hex notation to plain hex
        y = str(packet_13)
        y = struct.unpack('!d', packet_13.decode('hex'))[0]
        print("Y = ", y * 1000)

        packet_14 = s.recv(8)
        packet_14 = packet_14.encode("hex") #convert the data from \x hex notation to plain hex
        z = str(packet_14)
        z = struct.unpack('!d', packet_14.decode('hex'))[0]
        print("Z = ", z * 1000)

        packet_15 = s.recv(8)
        packet_15 = packet_15.encode("hex") #convert the data from \x hex notation to plain hex
        Rx = str(packet_15)
        Rx = struct.unpack('!d', packet_15.decode('hex'))[0]
        # print "Rx = ", Rx

        packet_16 = s.recv(8)
        packet_16 = packet_16.encode("hex") #convert the data from \x hex notation to plain hex
        Ry = str(packet_16)
        Ry = struct.unpack('!d', packet_16.decode('hex'))[0]
        # print "Ry = ", Ry

        packet_17 = s.recv(8)
        packet_17 = packet_17.encode("hex") #convert the data from \x hex notation to plain hex
        Rz = str(packet_17)
        Rz = struct.unpack('!d', packet_17.decode('hex'))[0]
        # print "Rz = ", Rz
        beta = (1-2*3.14/math.sqrt(Rx*Rx+Ry*Ry+Rz*Rz))
        Rx = -Rx * beta
        Ry = -Ry * beta
        Rz = -Rz * beta
        print("Rx = ", Rx)
        print("Ry = ", Ry)
        print("Rz = ", Rz)
        s.close()

    except socket.error as socketerror:
        print("Error: ", socketerror)

def movej(x, y, z, Rx, Ry, Rz, a, v):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((robot_ip, port))

    time.sleep(0.05)
    # s.send ("set_digital_out(2,True)" + "\n")  # Set digital output 2 high True

    # time.sleep(0.1)
    s.send ("movej(p[ %f, %f, %f, %f, %f, %f], a = %f, v = %f)\n" %(x/1000.0,y/1000.0,z/1000.0,Rx,Ry,Rz,a,v))   
    time.sleep(2)

    #s.send ("movej([d2r(0.55), d2r(0.395), d2r(0.45), 3.362, -2.744, 1.48], a=0.01, v=0.1)" + "\n") 
    # time.sleep(2)

    # time.sleep(4)
    # s.send ("movej(p[550/1000, 395/1000, 450/1000, 3.362, -2.744, 1.48], t = 4, r = 0)\n")														
    # time.sleep(1)

    s.close()

if __name__=="__main__":
    get_pos()  
    raw_input('Press enter to continue: ')  
    movej(446.0, 286.0, 329.0, 3.07, -0.38, -0.03, 0.1, 0.1)    
    get_pos()
    print("Program finish")
