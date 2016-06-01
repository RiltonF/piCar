#!/usr/bin/env python
import BaseControlls as Base
Base.GPIO.cleanup()
import BaseRangeControlls as Sonic
import time

SPEED = 9
trigDis = 15

def MainLoop():
	while True:
            print("entering mainsequence")
	    MainSequence()

def MainSequence():
	obstr = pollSensors()
        print("obstr = " + str(obstr))
	if obstr == 0:
            Base.setDirection("w", SPEED)
            print 'Moving forward'
	elif obstr == 1:
		Base.turn90Right()
	elif obstr == 2:
		Base.turn90Left()

def pollSensors():
	mDis = Sonic.PingSonicMAIN()
	dirr = 0  # 0 straight, 1 left, 2 right
	if mDis < trigDis:
		time.sleep(0.01)
		ld = Sonic.PingSonicLEFT()
		rd = Sonic.PingSonicRIGHT()
		if rd > ld:
			print("Found edge at left side!")
			dirr = 2
		else:
			print("Found edge a right side!")
			dirr = 1
	else:
		dirr = 0
	return dirr
try:
    MainLoop()
except:
    Base.GPIO.cleanup()
