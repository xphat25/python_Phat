from common.get_danhmuc import get_all_danhmuc

data = get_all_danhmuc()

print("✅ Danh sách danh mục:\n")

for row in data:
    print(f"ID: {row[0]}, Tên: {row[1]}, Mô tả: {row[2]}")
