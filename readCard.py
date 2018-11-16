import RPi.GPIO as GPIO
import lcddriver
from time import *
import time as t
import getStatus
import led
import MFRC522
import signal
import SimpleMFRC522
import sendToServer

reader = SimpleMFRC522.SimpleMFRC522()
read=MFRC522.MFRC522()

# LCD display

def action(status):
    if status == 1:  # CARD_OK
        print("CARD_OK")
        led.greenOn()
        sleep(2)
        led.greenOff()
    elif status == -1:  # CARD_BLOCKED
        print("CARD_BLOCKED")
        led.orangeOn()
        sleep(2)
        led.orangeOff()
    elif status == 0:  # CARD_NOT_FOUND
        print("CARD_NOT_FOUND")
        led.redOn()
        sleep(2)
        led.redOff()
        
def ledOff():
    GPIO.output(40, GPIO.LOW)


def ledOn():
    GPIO.output(40, GPIO.HIGH)

def initGPIO():
    GPIO.setwarnings(False)
    GPIO.setup(40, GPIO.OUT)
    ledOff()
    
def read():
    #led.cardOn()
    
    cardId, text = reader.read()
    ledOn()
    sleep(3)
    ledOff()
    #led.cardOff()
    return cardId

def check():
    (status, TagType) = read.MFRC522_Request(read.PICC_REQIDL)
    if status == read.MI_OK:
        print("Card detected")
        return 'inserted'
    else:
        print("Card not detected")
        return 'removed'


def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    try:
        initGPIO()
        sleep(2)
        ledOff()
        while True:
            #Check if the card is inserted first before continuing the reading action
            ch=check()
            if ch == 'inserted':
                id = read()
                status = getStatus.status(id,'view')
                action = 'insert'
                print("Card status is : "+status)
                sendToServer.send(id,action, status)
                print("sent to server")
                c=check()
                if c=='removed':
                    print("Card removed")
                    var = action == 'withdraw'
                    sendToServer.send(id,action,status)
            else:
                print("Card removed or no card inserted")

            
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
    GPIO.cleanup()


if __name__ == '__main__':
    # debug("----------========== Starting session! ==========----------")
    main()
