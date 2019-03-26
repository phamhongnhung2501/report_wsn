from random import *
import pymysql
from datetime import *
from time import sleep

db = pymysql.connect("localhost", "wsn", "123456", "wsn")

cursor = db.cursor()

sql = """INSERT INTO sensors(longtitude,lathtitude,temperature,humidity,wind_speed,wind_direction,date_time) 
		 VALUES (%s,%s,%s,%s,%s,%s,%s)"""

# insert phan tu muon them vao trong database
try:
    n = int(input("nhap vao so phan tu muon them vao database: "))
    if n < 0:
        exit()
except:
    print("phai nhap so nguyen duong")
    exit()
direct = {1: 'East', 2: 'West', 3: 'Sourth', 4: 'North'}
speed = {1: 'Spit', 2: 'Drizzle', 3: 'Rain', 4: 'Pour '}
for x in range(n):
    longtitude = randrange(1, 4)
    lathtitude = randrange(1, 4)
    temperature = randrange(20, 30)
    humidity = randrange(80, 100)
    wind_speed = speed[randrange(1, 4)]
    wind_direction = direct[randrange(1, 4)]
    val = (longtitude, lathtitude, temperature, humidity,
           wind_speed, wind_direction, datetime.now())
    try:
        # Execute the SQL command
        cursor.execute(sql, val)
        # Commit your changes in the database
        db.commit()
        print(x + 1, " \tLongtitude:", longtitude, " \tLathtitude:", lathtitude, " \tTemp:", temperature, "\tHum:", humidity, " \tWind_Speed:",
              wind_speed, " \tWind_Direction:", wind_direction, "\tTime:", datetime.now())
        sleep(1)
    except:
       # Rollback in case there is any error
        db.rollback()
        print("loi cu phap")
        sleep(1)
#--------------------------------------------------------------------------------#


try:
    column = input("nhap vao cot ban muon sap xep: ")
    method = input(
        """nhap "tang" de sap xep tang dan, nhap "giam" de sap xep giam dan:""")
    if method == "tang":
        sql = "SELECT id,longtitude,lathtitude,temperature,humidity,wind_speed, wind_direction, date_time FROM sensors ORDER BY " + column + " ASC "
    elif method == "giam":
        sql = "SELECT id,longtitude,lathtitude,temperature,humidity,wind_speed, wind_direction, date_time FROM sensors ORDER BY " + column + " DESC "
    else:

        exit()
    cursor.execute(sql)
    row = cursor.fetchone()
    db.commit()
    print("id longtitude lathtitude temperature humidity wind_speed wind_direction date_time")
    while row is not None:
        print(row)
        row = cursor.fetchone()
        db.commit()
except:
    print("Khong co du lieu")
#-------------------------------------------------------------------------------#

# disconnect from server
db.close()
