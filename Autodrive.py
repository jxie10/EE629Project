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

    distance = (end - start)*34300/2
    gpio.cleanup()
    return distance

def checkfront():
    init()
    dist = distance()
    
    if dist < 30:
        print("Close! Distance: {:.2f} cm".format(dist))
        init()
        turnLeft(1)
        init()
        dist = distance()
        if dist < 25:
            init()
            back(1)
            init()
            turnRight(2)
    if dist < 20:
        print("Too Close! Distance: {:.2f} cm".format(dist))
        init()
        back(1)
        init()
        spinLeft(0.8)
        init()
        dist = distance()
        if dist < 15:
            init()
            spinRight(1.6)
    if dist < 10:
        print("Too much Close!!! Distance: {:.2f} cm".format(dist))
        init()
        back(2)

def autodrive():
    checkfront()
    init()
    go(0.1)
    print("The distance of front now is: %0.2f cm" %distance())
        
try:
    while True:
        autodrive()
except KeyboardInterrupt:
    gpio.cleanup()
