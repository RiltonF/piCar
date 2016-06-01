#!/usr/bin/env python
import sys, tty, termios, os
import BaseControlls as Base
import RPi.GPIO as gpio

speedleft = 0
speedright = 0

# Instructions for when the user has an interface
print("w/s: direction")
print("a/d: steering")
print("q: stops the motors")
print("p: print motor speed (L/R)")
print("x: exit")

# The catch method can determine which key has been pressed
# by the user on the keyboard.
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Infinite loop
# The loop will not end until the user presses the
# exit key 'X' or the program crashes...

def printscreen():
	# Print the motor speed just for interest
	#os.system('clear')
	print("w/s: direction")
	print("a/d: steering")
	print("q: stops the motors")
	print("x: exit")
	print("========== Speed Control ==========")
	print "left motor:  ", speedleft
	print "right motor: ", speedright

try:
	while True:
	    # Keyboard character retrieval method. This method will save
	    # the pressed key into the variable char
		char = getch()

		# The car will drive forward when the "w" key is pressed
		if(char == "w"):
			print("w")
			Base.setDirection("w",9)

	    # The car will reverse when the "s" key is pressed
		elif(char == "s"):
			print("s")
			Base.setDirection("s",9)

	    # The "d" key will toggle the steering right
		elif(char == "d"):
			print("d")
			Base.setDirection("d",9)
		
	    # The "a" key will toggle the steering left
		elif(char == "a"):
			print("a")
			Base.setDirection("a",9)

		elif(char == "x"):
			Base.left1.stop()
			Base.left2.stop()
			Base.right1.stop()
			Base.right2.stop()
                        print "CleanUp"
			gpio.cleanup()
			break
		else:
			Base.setDirection("0",0)
		#empty Char
		char = ""
#clean exit and wiping GPIO registers when the program is exited by ^c
except KeyboardInterrupt:
	Base.left1.stop()
	Base.left2.stop()
	Base.right1.stop()
	Base.right2.stop()
	gpio.cleanup()
