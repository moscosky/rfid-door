#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import mysql

continue_reading = True

def initGpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)

def ledRedOn():
    GPIO.output(29,GPIO.HIGH)

def ledRedOff():
    GPIO.output(29,GPIO.LOW)

def ledGreenOn():
    GPIO.output(31,GPIO.HIGH)

def ledGreenOff():
    GPIO.output(31,GPIO.LOW)

def openDoor():
    GPIO.output(33,GPIO.HIGH)

def lockDoor():
    GPIO.output(33,GPIO.LOW)

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()


initGpio()
ledGreenOn()
ledRedOn()
time.sleep(3)
ledGreenOff()
ledRedOff()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    initGpio()

    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        tagId = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
        active = mysql.activeornot(tagId)
        if active:
            if active == "1":
                logcheck = mysql.logcheck(tagId)
                if logcheck == "logout":
                    ledGreenOn()
                    openDoor()
                    mysql.insertReading(tagId)
                    time.sleep(3)
                    lockDoor()
                    ledGreenOff()
                else:
                    ledRedOn()
                    mysql.insertReading(tagId)
                    time.sleep(1)
                    ledRedOff()

            else:
                ledRedOn()
                time.sleep(0.1)
                ledRedOff()
                time.sleep(0.1)
                ledRedOn()
                time.sleep(0.1)
                ledRedOff()
                time.sleep(0.1)
                ledRedOn()
                time.sleep(0.1)
                ledRedOff()

        else:
            ledRedOn()
            time.sleep(0.1)
            ledRedOff()
            time.sleep(0.1)
            ledRedOn()
            time.sleep(0.1)
            ledRedOff()
            time.sleep(0.1)
            ledRedOn()
            time.sleep(0.1)
            ledRedOff()


    

