import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#main
TRIG = 21
ECHO = 20
#right
TRIGR = 13
ECHOR = 6
#left
TRIGL = 26
ECHOL = 19 

print "Started sensor setup"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(TRIGR,GPIO.OUT)
GPIO.setup(TRIGL,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(ECHOR,GPIO.IN)
GPIO.setup(ECHOL,GPIO.IN)

def PingSonicMAIN ():
	GPIO.output(TRIG, False)
	print "Waiting For Sensor To Settle"
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance1 = pulse_duration1 * 17150

	distance1 = round(distance1, 2)

	print "Distance Main: ",distance,"cm"

	return distance

def PingSonicRIGHT ():
	GPIO.output(TRIGR, False)
	print "Waiting For Sensor To Settle"
	time.sleep(2)

	GPIO.output(TRIGR, True)
	time.sleep(0.00001)
	GPIO.output(TRIGR, False)

	while GPIO.input(ECHOR)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHOR)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance1 = pulse_duration1 * 17150

	distance1 = round(distance1, 2)

	print "Distance Right: ",distance,"cm"

	return distance

def PingSonicLEFT ():
	GPIO.output(TRIGL, False)
	print "Waiting For Sensor To Settle"
	time.sleep(2)

	GPIO.output(TRIGL, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHOL)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance1 = pulse_duration1 * 17150

	distance1 = round(distance1, 2)

	print "Distance Left: ",distance,"cm"

	return distance



