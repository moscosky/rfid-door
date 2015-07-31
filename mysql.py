#-------------------------------------------------------------------------------
# Name:        MySQL reader/writer
# Purpose:
#
# Author:      Jakub 'Yim' Dvorak
#
# Created:     26.10.2013
# Copyright:   (c) Jakub Dvorak 2013
# Licence:
#   ----------------------------------------------------------------------------
#   "THE BEER-WARE LICENSE" (Revision 42):
#   Jakub Dvorak wrote this file. As long as you retain this notice you
#   can do whatever you want with this stuff. If we meet some day, and you think
#   this stuff is worth it, you can buy me a beer in return.
#   ----------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import MySQLdb

from time import strftime,localtime
import datetime
from unidecode import unidecode

def connect():
    # Mysql connection setup. Insert your values here
    return MySQLdb.connect(host="localhost", user="root", passwd="root", db="pi")

def insertReading(tagId):
    db = connect()
    cur = db.cursor()
    currentTime=strftime("%Y.%m.%d - %H:%M:%S", localtime())
    cur.execute("SELECT action FROM readings WHERE tagId=%s ORDER BY id DESC LIMIT 1",(tagId))
    row = cur.fetchone()
    db.commit()
    if row:
        if row[0] == "logout":
            action = "login"
        else:
            action = "logout"
    else:
        action = "login"
    cur.execute("SELECT name FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    name = cur.fetchone()
    cur.execute("""INSERT INTO readings (name, tagId, time, action) VALUES (%s, %s, %s, %s)""",(name[0],tagId,currentTime,action)) 
    db.commit()
    db.close()

def insertCard(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("""INSERT INTO cards (name, tagId, active, onlyweekend) VALUES ('new', %s, '0', '0')""",(tagId))
    db.commit()
    db.close()

def activeornot(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT active FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def mondaycheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT monday FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def tuesdaycheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT tuesday FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def wednesdaycheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT wednesday FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def thursdaycheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT thursday FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def fridaycheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT friday FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def saturdaycheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT saturday FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def sundaycheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT sunday FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def logcheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT action FROM readings WHERE tagId=%s ORDER BY id DESC LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]
    else:
        return "logout"