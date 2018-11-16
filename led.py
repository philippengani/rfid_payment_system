# Program asks for user input to determine color to shine.

import time, sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
cardSwipe = 36
redPin = 37  # Set to appropriate GPIO
greenPin = 38  # Should be set in the
bluePin = 40  # GPIO.BOARD format


def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def ledOff():
    redOff()
    greenOff()
    blueOff()
    orangeOff()
    cyanOff()
    whiteOff()
    magentaOff()
    cardOff()


def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def redOn():
    blink(redPin)


def redOff():
    turnOff(redPin)


def greenOn():
    blink(greenPin)


def greenOff():
    turnOff(greenPin)


def blueOn():
    blink(bluePin)


def blueOff():
    turnOff(bluePin)


def cardOn():
    blink(cardSwipe)


def cardOff():
    turnOff(cardSwipe)

def orangeOn():
    blink(redPin)
    blink(greenPin)


def orangeOff():
    turnOff(redPin)
    turnOff(greenPin)


def cyanOn():
    blink(greenPin)
    blink(bluePin)


def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)


def magentaOn():
    blink(redPin)
    blink(bluePin)


def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)


def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)


def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)


