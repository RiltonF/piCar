import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)#set pin numbering type

#constants
step = .75
stepSpeed = 9
PWM_MAX = 100
#left motor setup
leftmotor_in1_pin = 27
leftmotor_in2_pin = 22
GPIO.setup(leftmotor_in1_pin, GPIO.OUT)
GPIO.setup(leftmotor_in2_pin, GPIO.OUT)

#right motor setup
rightmotor_in1_pin = 23
rightmotor_in2_pin = 24
GPIO.setup(rightmotor_in1_pin, GPIO.OUT)
GPIO.setup(rightmotor_in2_pin, GPIO.OUT)

#object init for PWM pins
left1 = GPIO.PWM(27, 500) #test the freq
left2 = GPIO.PWM(22, 500)
right1 = GPIO.PWM(23, 500)
right2 = GPIO.PWM(24, 500) #24

#start the PWM
left1.start(PWM_MAX)
left2.start(PWM_MAX)
right1.start(PWM_MAX)
right2.start(PWM_MAX)

#control specific motor, its direction, and speed.
def setMotorMode(motor, mode, speed):
    if motor == "l":
	if mode == "r":
            left1.ChangeDutyCycle(speed)
            left2.ChangeDutyCycle(0)
	elif mode == "f":
            left1.ChangeDutyCycle(0)
            left2.ChangeDutyCycle(speed)
    elif motor == "r":
	if mode == "r":
            right1.ChangeDutyCycle(speed)
            right2.ChangeDutyCycle(0)
	elif mode == "f":
            right1.ChangeDutyCycle(0)
            right2.ChangeDutyCycle(speed)
    else:
	left1.ChangeDutyCycle(0)
       	left2.ChangeDutyCycle(0)
	right1.ChangeDutyCycle(0)
        right2.ChangeDutyCycle(0)

#set the motor speeds to zero
setMotorMode(0,0,0)

#set direction of vehicle
def setDirection(mode, speed):
	#set speed
	speed = speed*11
	if speed == 99:
		speed += 1
	
	if mode == "w":
		setMotorMode("l","f",speed)
		setMotorMode("r","f",speed)
	elif mode == "a":
		setMotorMode("l","r",speed)
		setMotorMode("r","f",speed)
	elif mode == "s":
		setMotorMode("l","r",speed)
		setMotorMode("r","r",speed)
	elif mode == "d":
		setMotorMode("l","f",speed)
		setMotorMode("r","r",speed)
	else:
		setMotorMode(0,0,0)

def turn90Right():
	setDirection("d",stepSpeed)
	sleep(step);
	setDirection("0",0)

def turn90Left():
	setDirection("a",stepSpeed)
	sleep(step);
	setDirection("0",0)

def cleanUP():
	GPIO.cleanup()
