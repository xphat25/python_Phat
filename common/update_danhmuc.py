from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def update_danhmuc(madm, tendm, mota):
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

        # Câu lệnh update
        sql = "UPDATE danhmuc SET tendm = %s, mota = %s WHERE madm = %s"
        data = (tendm, mota, madm)
        cursor.execute(sql, data)
        connection.commit()

        print(f"✅ Đã cập nhật danh mục madm = {madm}")

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
