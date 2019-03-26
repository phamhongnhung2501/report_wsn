import pymysql
import json


def Sensor(jsonData):
    # Parse Data
    json_Dict = json.loads(jsonData)
    print(json_Dict)
    SensorID = json_Dict['Sensor_ID']
    Longtitude = json_Dict['Longtitude']
    Lathtitude = json_Dict['Lathtitude']
    Temperature = json_Dict['Temperature']
    Humidity = json_Dict['Humidity']
    Wind_Speed = json_Dict['Wind_Speed']
    Wind_Direction = json_Dict['Wind_Direction']
    Data_and_Time = json_Dict['Date']

    # Open database connection
    db = pymysql.connect("localhost", "mqtt", "123456", "mqtt")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Execute the SQL command
    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO sensors (SensorID,Longtitude,lathtitude,Temperature,Humidity,Wind_Speed,Wind_Direction,Date_and_Time) 
			 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    val = (SensorID, Longtitude, Lathtitude, Temperature, Humidity, Wind_Speed, Wind_Direction, Data_and_Time)
    cursor.execute(sql, val)
    db.commit()
    print("Sensor created new value")
    print("-------------------------")

    # disconnect from server
    db.close()
