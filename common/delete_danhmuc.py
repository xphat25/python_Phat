from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def delete_danhmuc(madm):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()

        # Kiểm tra tồn tại
        check_sql = "SELECT madm FROM danhmuc WHERE madm = %s"
        cursor.execute(check_sql, (madm,))
        result = cursor.fetchone()

        if not result:
            print(f"⚠️ Không tồn tại danh mục với madm = {madm}")
            return

        # Xóa danh mục
        sql = "DELETE FROM danhmuc WHERE madm = %s"
        cursor.execute(sql, (madm,))
        connection.commit()

        print(f"✅ Đã xóa danh mục có madm = {madm}")

    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
