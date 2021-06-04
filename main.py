import xbox
import sys
import time
import math
import RPi.GPIO as GPIO
import ultrasonic
import SimpleMFRC522

def initial():
 GPIO.setmode(GPIO.BCM);
 GPIO.setup(17, GPIO.OUT);
 GPIO.setup(22, GPIO.OUT);
 GPIO.setup(23, GPIO.OUT);
 GPIO.setup(24, GPIO.OUT);

def move_wheel(IN1, IN2, IN3, IN4):
 GPIO.output(17, IN1);
 GPIO.output(22, IN2);
 GPIO.output(23, IN3);
 GPIO.output(24, IN4);

def joypad(x,y):
    angle = 0.0
    if x >= 0.0 and y > 0.0:
        # first quadrant
        angle = math.degrees(math.atan(y/x)) if x!=0.0 else 90.0
    elif x < 0.0 and y >= 0.0:
        # second quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x < 0.0 and y < 0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x >= 0.0 and y < 0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x)) if x!=0.0 else -90.0
        angle += 360.0
    return angle





reader = SimpleMFRC522.SimpleMFRC522() #object

id = reader.read()
print("Scan your RFID Card...")
while not id:
   id = reader.read()

if id == 115173304638:
 print("                       ")
 print("Welcome Bibash Shrestha")
 print("                       ")
 joy = xbox.Joystick()

 while not joy.Back():

    if joy.connected():
        print ("Connected  "),
    else:
        print("Disconnected"),

    angle = joypad(joy.leftX(), joy.leftY())
    if (60 <= angle < 120):
       distance = ultrasonic.dist()
       if distance < 20:
        pass
        print("Object Ahead"),
        print("Distance: "+ str(distance)),
       else:
        initial()
        move_wheel(1,0,1,0) #forward
        time.sleep(0.1)

    elif (120 <= angle < 180):
       initial()
       move_wheel(0,0,1,0) #forward_left
       time.sleep(0.001)

    elif (0 < angle < 60):
       initial()
       move_wheel(1,0,0,0) #forward_right
       time.sleep(0.001)

    elif (240 <= angle < 300):
       initial()
       move_wheel(0,1,0,1) #backward
       time.sleep(0.001)

    elif (300 <= angle < 360):
       initial()
       move_wheel(0,1,0,0) #backward_left
       time.sleep(0.001)

    elif (180 < angle < 240):
       initial()
       move_wheel(0,0,0,1) #backward_right
       time.sleep(0.001)

    else:
       print("            "),
       print("                             "),
       initial()
       move_wheel(0,0,0,0)
       GPIO.cleanup()

    # Move cursor back to start of line
    print chr(13),


 joy.close()

else:
 print("Acess Denied")

