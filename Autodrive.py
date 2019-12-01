import RPi.GPIO as gpio
import time
import sys
import random

gpio.setwarnings(False)
goleft = 7
goright = 15
backleft = 11
backright = 13
TRIG = 12
ECHO = 16

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(goleft, gpio.OUT)
    gpio.setup(backleft, gpio.OUT)
    gpio.setup(goright, gpio.OUT)
    gpio.setup(backright, gpio.OUT)
    gpio.setup(TRIG, gpio.OUT)
    gpio.setup(ECHO, gpio.IN)

def go(timerun):
    init()
    gpio.output(goleft, True)
    gpio.output(backleft, False)
    gpio.output(goright, True)
    gpio.output(backright, False)
    time.sleep(timerun)
    gpio.cleanup()

def back(timerun):
    init()
    gpio.output(goleft, False)
    gpio.output(backleft, True)
    gpio.output(goright, False)
    gpio.output(backright, True)
    time.sleep(timerun)
    gpio.cleanup()

def turnLeft(timerun):
    init()
    gpio.output(goleft, False)
    gpio.output(backleft, False)
    gpio.output(goright, True)
    gpio.output(backright, False)
    time.sleep(timerun)
    gpio.cleanup()

def turnRight(timerun):
    init()
    gpio.output(goleft, True)
    gpio.output(backleft, False)
    gpio.output(goright, False)
    gpio.output(backright, False)
    time.sleep(timerun)
    gpio.cleanup()

def spinLeft(timerun):
    init()
    gpio.output(goleft, False)
    gpio.output(backleft, True)
    gpio.output(goright, True)
    gpio.output(backright, False)
    time.sleep(timerun)
    gpio.cleanup()

def spinRight(timerun):
    init()
    gpio.output(goleft, True)
    gpio.output(backleft, False)
    gpio.output(goright, False)
    gpio.output(backright, True)
    time.sleep(timerun)
    gpio.cleanup()

def Stop(timerun):
    init()
    gpio.output(goleft, False)
    gpio.output(backleft, False)
    gpio.output(goright, False)
    gpio.output(backright, False)
    time.sleep(timerun)
    gpio.cleanup()

def distance():
    init()
    gpio.output(TRIG, True)
    time.sleep(0.000012)
    gpio.output(TRIG, False)
    while not gpio.input(ECHO):
        pass
    start = time.time()
    while gpio.input(ECHO):
        pass
    end = time.time()

    return (end - start)*34300/2
    gpio.cleanup()
    return distance

def cheack_front():
    init()
    dist = distance()

    if dist < 15:
        print("Close! Distance: {:.2f} cm".format(dist))
        init()
        back(1)
        init()
        dist = distance()
        if dist < 15:
            print("Too Close! Distance: {:.2f} cm".format(dist))
            init()
            spinLeft(3)
            init()
            back(1)
            dist = distance()
            if dist < 15:
                print("Too much Close!!! Distance: {:.2f} cm".format(dist))
                stop(2)

def autodrive():
    tf = 0.1
    x = random.randrange(0,3)

    if x == 0:
        check_front()
        init()
        go(1)
        print("Fowarding. The distance now is: %0.2f cm" %distance())
    elif x == 1:
        cheack_front()
        init()
        spinLeft(0.3)
        print("Spining left. The distance now is: %0.2f cm" %distance())
    elif x == 2:
        cheack_front()
        init()
        spinRight(0.15)
        print("Spining right. The distance now is: %0.2f cm" %distance())
    elif x == 3:
        cheack_front()
        init()
        spinRight(tf)
        print("Spining right. The distance now is: %0.2f cm" %distance())

#go(3)
#back(3)
#turnLeft(3)
#turnRight(3)
#spinLeft(3)
#spinRight(3)
#Stop(3)
