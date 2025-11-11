from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def get_all_danhmuc():
    try:
        connection = connect_mysql()
        if connection is None:
            return []

        cursor = connection.cursor()

        sql = "SELECT madm, tendm, mota FROM danhmuc"
        cursor.execute(sql)

        result = cursor.fetchall()

        return result

    except Error as e:
        print("❌ Lỗi khi lấy danh mục:", e)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
