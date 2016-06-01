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

def PingSonic(sens):
    trig = 0
    echo = 0
    if (sens == "main"):
        trig = TRIG
        echo = ECHO
    elif (sens == "left"):
        trig = TRIGL
        echo = ECHOL
    elif (sens == "right"):
        trig = TRIGR
        echo = ECHOR
    else:
        break

    retutn PingSensor(trig,echo)

def PingSensor(trig,echo):
        GPIO.output(trig, False)
	print "Waiting For Sensor To Settle"
	time.sleep(2)

	GPIO.output(trig, True)
	time.sleep(0.00001)
	GPIO.output(trig, False)

	while GPIO.input(echo)==0:
	  pulse_start = time.time()

	while GPIO.input(echo)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
	print("Distance Main: " + str(distance) + "cm")
	return distance

def CleanUP():
    GPIO.cleanup()
