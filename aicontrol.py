import BaseControlls as Base
import BaseRangeControlls as Sonic
import time

SPEED = 1
trigDis = 10

def MainLoop():
	while True:
		MainSequence()

def MainSequence():
	obstr = pollSensors()

	if obstr == 0:
		Base.setDirection("w", SPEED)
	elif obstr == 1:
		Base.turn90Right()
	elif obstr == 2:
		Base.turn90Left()

def pollSensors():
	mDis = Sonic.PingSonicMain()
	dirr = 0  # 0 straight, 1 left, 2 right
	if mDis < trigDis:
		time.sleep(0.01)
		ld = Sonic.PingSonicLeft()
		rd = Sonic.PingSonicRight()
		if rd > ld:
			print("Found edge at left side!")
			dirr = 2
		else:
			print("Found edge a right side!")
			dirr = 1
	else:
		dirr = 0
	return dirr