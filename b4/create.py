import pymysql

# Open database connection
db = pymysql.connect("localhost","wsn","123456","wsn" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS sensors")

# Create table as per requirement
sql = """CREATE TABLE sensors(
         id  INT(10) PRIMARY KEY AUTO_INCREMENT,
         -- SensorID char(10) NOT NULL,
         longtitude INT(3) NOT NULL,
         lathtitude INT(3) NOT NULL,
         temperature INT(3) NOT NULL,
         humidity INT(3) NOT NULL,
         wind_speed NVARCHAR(10) NOT NUll,
         wind_direction NVARCHAR(10) NOT NUll,
         date_time char(30) NOT NULL )"""

cursor.execute(sql)

# disconnect from server
db.close()
