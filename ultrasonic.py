import RPi.GPIO as GPIO;
import time;

def dist():
 GPIO.setmode(GPIO.BCM);
 TRIG = 04;
 ECHO = 18;

 GPIO.setup(TRIG,GPIO.OUT);
 GPIO.output(TRIG,0);           #set low
 GPIO.setup(ECHO,GPIO.IN);

 #print("Starting Measurement");

 time.sleep(0.001);
 GPIO.output(TRIG,1);
 time.sleep(0.00001);       #set trigger high and wait for 10 microsecond
 GPIO.output(TRIG,0);       #and set trigger high

 #now we have to listen to the input pin
 while GPIO.input(ECHO) == 0:      #while comtinues until pin goes high..
                                  #when high signal has arrived with is start time
  pass                            #do nothing
 start = time.time();              #time.time() gives current time in sec

 while GPIO.input(ECHO) == 1:       #while continues until pin goes low
                                   #when low signal has ended which start time
  pass
 stop = time.time();


 distance = (stop-start)*170*100;
 GPIO.cleanup();
 return distance;

