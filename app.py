#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import mysql

continue_reading = True

def initGpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

def ledRedOn():
    GPIO.output(5,True)

def ledRedOff():
    GPIO.output(5,False)

def ledGreenOn():
    GPIO.output(6,True)

def ledGreenOff():
    GPIO.output(6,False)

def openDoor():
    GPIO.output(13,True)

def lockDoor():
    GPIO.output(13,False)

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
        if active = "1":
            logcheck = mysql.logcheck(tagId)
            if logcheck = "logout":
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


    

