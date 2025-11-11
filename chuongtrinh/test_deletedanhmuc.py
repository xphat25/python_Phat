from common.delete_danhmuc import delete_danhmuc

madm = input("Nhập vào mã danh mục cần xóa: ").strip()

if madm.isdigit():
    delete_danhmuc(int(madm))
else:
    print("⚠️ Mã danh mục phải là số!")
