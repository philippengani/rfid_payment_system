#!/usr/bin/env python
import lcddriver
from time import *
#import display
import time as t
import mysql
import RPi.GPIO as GPIO
import MFRC522
import signal
import SimpleMFRC522

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)
sleep(3)
reader = SimpleMFRC522.SimpleMFRC522()
#LCD display
'''
lcd = lcddriver.lcd()
lcd.lcd_clear()
lcd.lcd_clear()
str_pad = " " * 20
my_long_string = "WELCOME TO DEXXYS-REGISTER A CUSTOMER"
my_long_string = str_pad + my_long_string
for i in range (0, len(my_long_string)):
        lcd_text = my_long_string[i:(i+20)]
        lcd.lcd_display_string(lcd_text,1)
        sleep(0.1)
        lcd.lcd_display_string(str_pad,1)

lcd.lcd_display_string("WELCOME TO DEXXYS", 1)
'''
checkUser=True
while checkUser:
        try:
                GPIO.setmode(GPIO.BOARD)
                GPIO.setwarnings(False)
                GPIO.setup(40,GPIO.OUT)
                GPIO.output(40,GPIO.LOW)
                print("Place card near reader")
                id, text = reader.read()
                GPIO.output(40,GPIO.HIGH)
                print(id)
                sleep(5)
                print(text)
        finally:
                GPIO.cleanup()
