import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='sqlanor@2004',
        database='clientconnect'  # Make sure this is correct
    )
    print("Connected successfully")
except pymysql.Error as e:
    print(f"Error connecting to MySQL: {e}")
