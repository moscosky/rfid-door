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
    currentTime=strftime("%Y%m%d%H%M%S", localtime())
    cur.execute("SELECT action FROM readings WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.commit()
    if row[0] == "logout":
        action = "login"
    else:
        action = "logout"
    cur.execute("SELECT name FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    name = cur.fetchone()
    db.commit()
    cur.execute("""INSERT INTO readings (name, tagId, time, action) VALUES (%s, %s, %s, %s)""",(name,tagId,currentTime,action)) 
    db.close()

def activeornot(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT active FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    return row[0]