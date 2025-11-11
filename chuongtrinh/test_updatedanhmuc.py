from common.update_danhmuc import update_danhmuc

madm = input("Nhập mã danh mục cần sửa: ").strip()
tendm = input("Nhập tên danh mục mới: ").strip()
mota = input("Nhập mô tả mới: ").strip()

if madm.isdigit():
    update_danhmuc(int(madm), tendm, mota)
else:
    print("⚠️ Mã danh mục phải là số!")
