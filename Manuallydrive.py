import RPi.GPIO as gpio
import time
import sys
from bottle import get,post,run,request,template

gpio.setwarnings(False)
goleft = 7
goright = 15
backleft = 11
backright = 13

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(goleft, gpio.OUT)
    gpio.setup(backleft, gpio.OUT)
    gpio.setup(goright, gpio.OUT)
    gpio.setup(backright, gpio.OUT)

def go():
    gpio.output(goleft, True)
    gpio.output(backleft, False)
    gpio.output(goright, True)
    gpio.output(backright, False)

def back():
    gpio.output(goleft, False)
    gpio.output(backleft, True)
    gpio.output(goright, False)
    gpio.output(backright, True)

def turnLeft():
    gpio.output(goleft, False)
    gpio.output(backleft, False)
    gpio.output(goright, True)
    gpio.output(backright, False)

def turnRight():
    gpio.output(goleft, True)
    gpio.output(backleft, False)
    gpio.output(goright, False)
    gpio.output(backright, False)

def Stop():
    init()
    gpio.output(goleft, False)
    gpio.output(backleft, False)
    gpio.output(goright, False)
    gpio.output(backright, False)
    gpio.cleanup()

#get the command from website
@get("/")
def index():
    return template("index")
@post("/cmd")
def cmd():
    print("pressed: "+request.body.read().decode())
    init()
    sleep_time = 1
    arg = request.body.read().decode()
    if(arg=='up'):
        go()
    elif(arg=='down'):
        back()
    elif(arg=='left'):
        turnLeft()
    elif(arg=='right'):
        turnRight()
    elif(arg=='stop'):
        Stop()
    else:
        return False

#set host to your raspberrypi's IP
run(host="192.168.1.20",port="8080")


