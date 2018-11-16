import RPi.GPIO as GPIO
import lcddriver
from time import *
import display
import time as t
import mysql
import RPi.GPIO as GPIO
import MFRC522
import signal
import SimpleMFRC522

import thread

reader = SimpleMFRC522.SimpleMFRC522()
lcd = lcddriver.lcd()


# LCD display


class Create:
    incomming = 1
    outcomming = 2
    breakstart = 3
    breakend = 4


def operation(action):
    if (action == 1):
        
        clearDisp()
        display("Create a customer...", 1)
        display("Swipe your card", 2)
        cardId = read()
        ledOn()
        print(cardId)
        # display(str(cardId), 3)
        clearDisp()
        display("Create a customer...", 1)
        display("Enter the name", 2)
        name = raw_input("Name ")
        print(name)
        sleep(1)
        clearDisp()
        display("Create a customer...", 1)
        display("Enter the surname", 2)
        surname = raw_input("Surname ")
        print(surname)
        sleep(1)
        clearDisp()
        display("Create a customer...", 1)
        display("Enter the amount", 2)
        amount = input("Amount ")
        print(amount)
        create = mysql.create(cardId, name, surname, amount)
        clearDisp()
        sleep(1)
        display("Create a customer...", 1)
        display(str(create) + " successfully", 2)
        print(create + " in the database")
        sleep(3)
        ledOff()
    if (action == 2):
        
        clearDisp()
        display("Add money ...", 1)
        display("Swipe your card", 2)
        cardId = read()
        ledOn()
        print(cardId)
        user = mysql.getUser(cardId)
        surname, amt = user.split(',')
        print(surname + "," + amt)
        display(str(surname) + "," + str(amt), 2)
        # display(str(cardId), 3)
        sleep(2)
        clearDisp()
        display(str(surname) + "," + str(amt), 1)
        display("Enter amount ", 2)
        amount = input("Amount to add ")
        print(amount)
        clearDisp()
        display(str(surname) + "," + str(amt), 1)
        display("Adding " + str(amount), 2)
        add = mysql.addMoney(cardId, amount)
        sleep(2)
        clearDisp()
        display(str(surname) + "," + str(amt), 1)
        balance = float(amt) + amount
        display(str(add)+" new balance is "+str(balance), 2)
        print("New balance :")
        print(balance)
        ledOff()
        sleep(3)



def read():
    ledOn()
    cardId, text = reader.read()
    initGPIO()
    ledOff()
    return cardId


def ledOff():
    GPIO.output(40, GPIO.LOW)


def ledOn():
    GPIO.output(40, GPIO.HIGH)


def display(message, position):
    lcd.lcd_display_string(str(message), position)


def clearDisp():
    lcd.lcd_clear()


def initDisplay():
    lcd.lcd_clear()
    lcd.lcd_display_string("WELCOME TO DEXXYS", 1)


def initGPIO():
    GPIO.setwarnings(False)
    GPIO.setup(40, GPIO.OUT)
    ledOff()


def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    try:
        initGPIO()

        initDisplay()
        sleep(2)
        while True:
            clearDisp()
            display("Choose an action ", 1)
            display("1- Create customer", 2)
            display("2- Add money ", 3)
            print("Choose an action ..........")
            print("1- Create customer")
            print("2- Add money ")
            a = input("Enter the action number ")
            if 0 < a < 3:
                operation(a)
            else:
                display("Enter the correct number", 1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
    GPIO.cleanup()


if __name__ == '__main__':
    # debug("----------========== Starting session! ==========----------")
    main()
