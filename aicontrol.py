#!/usr/bin/env python
import BaseControlls as Base
import BaseRangeControlls2 as Sonic
import time

SPEED = 9
trigDis = 10

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
            print 'Turning right'
            Base.turn90Right()
	elif obstr == 2:
            print 'Turning left'
            Base.turn90Left()

def pollSensors():
	mDis = Sonic.PingSonic('main')
	dirr = 0  # 0 straight, 1 left, 2 right
	if mDis < trigDis:
            print 'Entered turning routine'
            Base.setMotorMode(0,0,0) #stop
            time.sleep(0.01)
            ld = Sonic.PingSonic('left')
            print str(ld)
	    rd = Sonic.PingSonic('right')
	    if rd < ld:
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
except KeyboardInterrupt:
    Base.cleanUP()
    Sonic.cleanUP()
