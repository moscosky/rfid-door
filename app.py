#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import mysql
import datetime
import threading

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

def errorLed():
    ledRedOn()
    wait.wait(timeout=0.2)
    ledRedOff()
    wait.wait(timeout=0.2)
    ledRedOn()
    wait.wait(timeout=0.2)
    ledRedOff()
    wait.wait(timeout=0.2)
    ledRedOn()
    wait.wait(timeout=0.2)
    ledRedOff()

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
    wait = threading.Event()

    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        tagId = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
        if mysql.activeornot(tagId):
            if mysql.activeornot(tagId) == "1":
                monday = mysql.mondaycheck(tagId)
                tuesday = mysql.tuesdaycheck(tagId)
                wednesday = mysql.wednesdaycheck(tagId)
                thursday = mysql.thursdaycheck(tagId)
                friday = mysql.fridaycheck(tagId)
                saturday = mysql.saturdaycheck(tagId)
                sunday = mysql.sundaycheck(tagId)
                weekday = datetime.date.today().isoweekday()
                time = datetime.datetime.now().time()
                from_string = mysql.fromcheck(tagId)
                till_string = mysql.tillcheck(tagId)
                fromtime = datetime.datetime.strptime(from_string, "%H:%M").time()
                tilltime = datetime.datetime.strptime(till_string, "%H:%M").time()
                a1 = weekday == 1 and monday == "1"
                a2 = weekday == 2 and tuesday == "1"
                a3 = weekday == 3 and wednesday == "1"
                a4 = weekday == 4 and thursday == "1"
                a5 = weekday == 5 and friday == "1"
                a6 = weekday == 6 and saturday == "1"
                a7 = weekday == 7 and sunday == "1"
                weekday_state = a1 or a2 or a3 or a4 or a5 or a6 or a7
                time_state = fromtime < time < tilltime
                if weekday_state and time_state:
                    logcheck = mysql.logcheck(tagId)
                    if logcheck == "logout":
                        ledGreenOn()
                        openDoor()
                        mysql.insertReading(tagId)
                        wait.wait(timeout=3)
                        lockDoor()
                        ledGreenOff()
                    else:
                        ledRedOn()
                        mysql.insertReading(tagId)
                        wait.wait(timeout=1)
                        ledRedOff()
                else:
                    errorLed()
                    
            else:
                errorLed()

        elif mysql.event_activeornot(tagId):
            if mysql.event_activeornot(tagId) == "1":
                time = datetime.datetime.now()
                from_string = mysql.event_fromcheck(tagId)
                till_string = mysql.event_tillcheck(tagId)
                fromtime = datetime.datetime.strptime(from_string, "%Y.%m.%d - %H:%M:%S")
                tilltime = datetime.datetime.strptime(till_string, "%Y.%m.%d - %H:%M:%S")
                time_state = fromtime < time < tilltime
                if time_state:
                    logcheck = mysql.event_logcheck(tagId)
                    if logcheck == "logout":
                        ledGreenOn()
                        openDoor()
                        mysql.event_insertReading(tagId)
                        wait.wait(timeout=3)
                        lockDoor()
                        ledGreenOff()
                    else:
                        ledRedOn()
                        mysql.event_insertReading(tagId)
                        wait.wait(timeout=1)
                        ledRedOff()
                else:
                    errorLed()

            else:
                errorLed()

        else:
            mysql.insertCard(tagId)
            mysql.event_insertCard(tagId)
            errorLed()


    

