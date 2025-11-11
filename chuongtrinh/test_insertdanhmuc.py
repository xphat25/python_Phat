from common.insertdanhmuc import insert_danhmuc

while True:
    ten = input("Nhập vào tên danh mục: ").strip()
    mota = input("Nhập vào mô tả: ").strip()

    insert_danhmuc(ten, mota)

    con = input("Tiếp tục? (y để tiếp tục, phím khác để thoát): ").strip().lower()
    if con != "y":
        print("Thoát chương trình...")
        break
