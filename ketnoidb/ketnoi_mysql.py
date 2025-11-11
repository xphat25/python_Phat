import mysql.connector
from mysql.connector import Error

def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='qlthuocankhang',
            port=3307,
            charset='utf8mb4'
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi kết nối MySQL:", e)
        return None
