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
    cur.execute("""INSERT INTO cards (name, tagId, active, monday, tuesday, wednesday, thursday, friday, saturday, sunday, time_from, time_till) VALUES ('new', %s, '0', '0', '0', '0', '0', '0', '0', '0', '09:00', '17:00')""",(tagId))
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

def fromcheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT time_from FROM cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def tillcheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT time_till FROM cards WHERE tagId=%s LIMIT 1",(tagId))
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













def event_insertReading(tagId):
    db = connect()
    cur = db.cursor()
    currentTime=strftime("%Y.%m.%d - %H:%M:%S", localtime())
    cur.execute("SELECT action FROM event_readings WHERE tagId=%s ORDER BY id DESC LIMIT 1",(tagId))
    row = cur.fetchone()
    db.commit()
    if row:
        if row[0] == "logout":
            action = "login"
        else:
            action = "logout"
    else:
        action = "login"
    cur.execute("SELECT name FROM event_cards WHERE tagId=%s LIMIT 1",(tagId))
    name = cur.fetchone()
    cur.execute("""INSERT INTO event_readings (name, tagId, time, action) VALUES (%s, %s, %s, %s)""",(name[0],tagId,currentTime,action)) 
    db.commit()
    db.close()

def event_insertCard(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("""INSERT INTO event_cards (name, tagId, active, time_from, time_till) VALUES ('new', %s, '0', '2015.08.01 - 09:00:00', '2015.08.01 - 17:00:00')""",(tagId))
    db.commit()
    db.close()

def event_activeornot(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT active FROM event_cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def event_fromcheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT time_from FROM event_cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def event_tillcheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT time_till FROM event_cards WHERE tagId=%s LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]

def event_logcheck(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT action FROM event_readings WHERE tagId=%s ORDER BY id DESC LIMIT 1",(tagId))
    row = cur.fetchone()
    db.close()
    if row:
        return row[0]
    else:
        return "logout"