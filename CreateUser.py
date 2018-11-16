import RPi.GPIO as GPIO
import lcddriver
from time import *
import time as t
import mysql
import RPi.GPIO as GPIO
import MFRC522
import signal
import SimpleMFRC522
import generateData
import sendToServer
import thread

reader = SimpleMFRC522.SimpleMFRC522()

# LCD display


def read():
    cardId, text = reader.read()
    ledOn()
    initGPIO()
    sleep(3)
    ledOff()
    return cardId


def ledOff():
    GPIO.output(40, GPIO.LOW)


def ledOn():
    GPIO.output(40, GPIO.HIGH)

def initGPIO():
    GPIO.setwarnings(False)
    GPIO.setup(40, GPIO.OUT)
    ledOff()



def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    try:
        initGPIO()
        sleep(2)
        while True:
            card_id = read()
            data= generateData.generate(card_id,'insert')
            sendToServer.send(data, status)
            print("sent to server")

    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
    GPIO.cleanup()


if __name__ == '__main__':
    # debug("----------========== Starting session! ==========----------")
    main()
