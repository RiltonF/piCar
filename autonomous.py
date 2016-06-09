#!/usr/bin/python
import BaseControlls as Base
import BaseRangeControlls2 as Sonic
import RPi.GPIO as GPIO
import PSControl
import aicontrol
from time import sleep
from triangula.input import SixAxisResource, SixAxis


mode = "mantr"

#pins
pinServoUp = 4
pinServoDown = 5
GPIO.setup(pinServoUp,GPIO.OUT)
GPIO.setup(pinServoDown, GPIO.OUT)

def Main():
	joyst = "lel"
	Dispatcher(joyst)

def AcquireController():
	while True:
	    try:
                with SixAxisResource() as joyy:
                    jy = joyy
	    except:
		sleep(1)
	    else:
		print 'acquired controller'
		break
	return jy

def Dispatcher(joyy):
    with SixAxisResource() as joy:
	joy.register_button_handler(Handler, SixAxis.BUTTON_SELECT)
	joy.register_button_handler(ServoHandler, SixAxis.BUTTON_D_DOWN)
	joy.register_button_handler(ServoHandler, SixAxis.BUTTON_D_UP)

	while True:
	    if mode=="manxy":
	        PSControl.step(joy)
	    elif mode=="mantr":
		PSControl.stepTR(joy)
	    elif mode=="ai":
		aicontrol.MainSequence()
	    elif mode=="halt":
		sleep(1)
		if mode=="halt":
		    sleep(1)
		    if mode=="halt":
			sleep(1)
			if mode=="halt":
			    sleep(1)
			    if mode=="halt":
				sleep(1)
				if mode=="halt":
				    return


def Handler(button):
    print 'handled button'
    if mode=="manxy":
	mode = "mantr"
    elif mode=="mantr":
	mode = "ai"
    elif mode=="ai":
	mode = "halt"
    else:
	mode = "manxy"

def ServoHandler(butt):
    if butt==SixAxis.BUTTON_D_DOWN:
	GPIO.output(pinServoDown, True)
	sleep(0.05)
	GPIO.output(pinServoDown, False)
    else:
	GPIO.output(pinServoUp, True)
	sleep(0.05)
	GPIO.output(pinServoUp, False)


try:
    Main()
except KeyboardInterrupt:
    Base.cleanUP()
    Sonic.cleanUP()
