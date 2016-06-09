#!/usr/bin/python
import BaseControlls as Base
from triangula.input import SixAxisResource, SixAxis

def recalcspeed(a, b):
    if (a == 0 and b == 0):
        return 0
    else:
        return a / (a+b)

def makemove(up, right, vx, vy, vt):
    lt = 1
    rt = 1
    f = -1
    if right:
        if up:
            f = 1
        lt = vy * f
        rt = (vy - vx*0.5) * f
    else:
        if up:
            f = 1
        lt = (vy - vx*0.5) * f
        rt = vy * f
    #print("left: " + str(lt) + " - right: " + str(rt))
    Base.setMotorMode("l", lt > 0, abs(lt)*5 + 4)
    Base.setMotorMode("r", rt > 0, abs(rt)*5 + 4)

def makemove2(up, right, v1, v2):
    lt = 1
    rt = 1
    f = -1
    if right:
        if up:
            f = 1
        lt = f * v1
        rt = f * v2
    else:
        if up:
            f = 1
        lt = f * v2
        rt = f * v1
    #print("left: " + str(lt) + " - right: " + str(rt))
    Base.setMotorMode("l", lt > 0, abs(lt)*5 + 4)
    Base.setMotorMode("r", rt > 0, abs(rt)*5 + 4)

def headloop():
    with SixAxisResource() as joyst:
        while 1:
            #Values go -1.0 to 1.0 when:
            #x-axes: left to right
            #y-axes: down to up
            x1 = joyst.axes[0].corrected_value()
            y1 = joyst.axes[1].corrected_value()
            x2 = joyst.axes[2].corrected_value()
            y2 = joyst.axes[3].corrected_value()
            #
            up = y1 > 0
            right = x1 > 0
            vt = max(x1,y1)
            if abs(y1) >= abs(x1):
                if abs(x1) >= 0.5*abs(y1):
                    vx = (abs(x1) - 0.5*abs(y1)) * 2
                else:
                    vx = 0
                vy = abs(y1)
                makemove(up, right, vx, vy, vt)
            elif (x1 < 0.2 and y1 < 0.2):
                makemove2(True, True, 0, 0)
            else:
                altv = recalcspeed(x1, y1)
                regv = abs(x1)
                makemove2(up, right, regv, altv)


headloop()

