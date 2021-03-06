# smart_car

1.2 OBJECTIVES:
1. To build a remote controlled car
2. To control the car with the help of X-BOX Controller.
3. To design a software to process the instructions
4. To detect the objects that come on the path of car and avoid them

2.1 Requirements Engineering:
The following are the requirements of the system
⦁	Input 	: Movement input from Xbox Controller, ID from RFID
⦁	Output: 	Motors direction, Livestream video
⦁	Processing: 	Controller Processing, Video Processing, Distance Processing
⦁	Input 	Supply: 9V for motors, 5V for Raspberry Pi
⦁	Size: 	Small Scale
⦁	Operating 	Environment: Flat terrain surface

2.2 Hardware-Software Partitioning:
2.2.1 Hardware Specifications:
1. Raspberry Pi
Raspberry Pi is used as the brain of the project, processing the video from the stereoscopic camera and live streaming to the smartphone intact in Google Cardboard. It also the controls the wheels of the car by processing the input from the Xbox controller. In addition, the pi is also responsible for processing the movements of the VR set to correspond the movement of the camera mounted in front of the car. The car is provided with two Raspberry Pis for faster processing. Two Pis have divided tasks, such that all the components work smoothly in simultaneously manner. Both Raspberry Pi are powered by 5V battery.

2. Webcam
A webcam is a video camera that connects to a computer, and can let people see each other over the Internet or without the internet. Most people that have webcams use them with an instant messenger to see each other at the same time. Webcams can also be used for recording videos and video blogs. The webcam can be part of a computer, mobile phone or it can be an independent device.

3. XBOX Controller
A wireless XBOX controller is used to control the directions and movements of the car. A chip XBOX receiver is connected to the Raspberry Pi, to connect the controller to the system. When the buttons and joystick are used, controller sends signals to the receiver, which in its part sends received signal to Pi for processing.

4. H-BRIDGE
L298N H-bridge Dual Motor Controller Module 2A with Raspberry Pi. This allows you to control the speed and direction of two DC motors, or control one bipolar stepper motor with ease. The L298N H-bridge module can be used with motors that have a voltage of between 5 and 35V DC.

5. Motor
We have used two 6V 250 Rpm Plastic Gear motor, wheel and a free moving wheel at the front to construct the moving part for the car.

6. Ultrasonic sensor
As the name indicates, ultrasonic sensors measure distance by using ultrasonic waves. The sensor head emits an ultrasonic wave and receives the wave reflected back from the target. Ultrasonic Sensors measure the distance to the target by measuring the time between the emission and reception.

7. Power Sources
For providing power to our hardware, we used two different power sources. We used a 5V 1mAh power bank to power the Raspberry Pi and 6V battery for H-BRIDGE.

8. Car Chassis and Body Parts
Two car chassis plate was used along with fasteners and zip ties to assemble the body for the car.

2.2.2 Software Specifications:
Operating System: Linux Mint, Ubuntu
Programming Language: Python
Development tools: Atom, Pycharm
Library Used: Xbox Gamepad User space Driver for Linux(Xboxdrv)


