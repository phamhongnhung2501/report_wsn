import pymysql

# Open database connection
db = pymysql.connect("localhost","mqtt","123456","mqtt" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS sensors")

# Create table as per requirement
sql = """CREATE TABLE sensors(
         id  INT(10) PRIMARY KEY AUTO_INCREMENT,
         SensorID char(10) NOT NULL,
         Longtitude INT(3) NOT NULL,
         Lathtitude INT(3) NOT NULL,
         Temperature INT(3) NOT NULL,
         Humidity INT(3) NOT NULL,
         Wind_Speed NVARCHAR(10) NOT NULL,
         Wind_Direction NVARCHAR(10) NOT NULL,
         Date_and_Time char(30) NOT NULL )"""

cursor.execute(sql)

# disconnect from server
db.close()
