import tkinter as tk
from tkinter import ttk, messagebox

from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from common.delete_danhmuc import delete_danhmuc
from common.get_danhmuc import get_all_danhmuc


def load_data():
    for row in tree.get_children():
        tree.delete(row)

    data = get_all_danhmuc()
    for row in data:
        tree.insert("", tk.END, values=row)


def insert_dm():
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()

    if ten == "" or mota == "":
        messagebox.showwarning("Lỗi", "Không được để trống!")
        return

    insert_danhmuc(ten, mota)
    load_data()


def update_dm():
    try:
        madm = tree.item(tree.selection()[0])["values"][0]
        ten = entry_ten.get().strip()
        mota = entry_mota.get().strip()
        update_danhmuc(madm, ten, mota)
        load_data()

    except:
        messagebox.showerror("Lỗi", "Hãy chọn dòng cần sửa!")


def delete_dm():
    try:
        madm = tree.item(tree.selection()[0])["values"][0]
        delete_danhmuc(madm)
        load_data()

    except:
        messagebox.showerror("Lỗi", "Hãy chọn dòng cần xóa!")


def on_select(event):
    try:
        vals = tree.item(tree.selection()[0])["values"]
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_ten.insert(0, vals[1])
        entry_mota.insert(0, vals[2])
    except:
        pass


# GIAO DIỆN TKINTER
root = tk.Tk()
root.title("Quản lý Danh mục thuốc")
root.geometry("700x400")
root.resizable(False, False)

# Frame nhập dữ liệu
frame_input = tk.Frame(root)
frame_input.pack(fill="x", padx=10, pady=5)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5)
entry_ten = tk.Entry(frame_input, width=40)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5)
entry_mota = tk.Entry(frame_input, width=40)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# Nút chức năng
frame_btn = tk.Frame(root)
frame_btn.pack(fill="x", padx=10, pady=5)

btn_them = tk.Button(frame_btn, text="➕ Thêm", width=12, command=insert_dm)
btn_them.pack(side="left", padx=5)

btn_sua = tk.Button(frame_btn, text="✏️ Sửa", width=12, command=update_dm)
btn_sua.pack(side="left", padx=5)

btn_xoa = tk.Button(frame_btn, text="🗑️ Xóa", width=12, command=delete_dm)
btn_xoa.pack(side="left", padx=5)

btn_hienthi = tk.Button(frame_btn, text="🔄 Làm mới", width=12, command=load_data)
btn_hienthi.pack(side="left", padx=5)

# Bảng hiển thị dữ liệu
frame_table = tk.Frame(root)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("madm", "tendm", "mota")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)

tree.heading("madm", text="Mã DM")
tree.heading("tendm", text="Tên danh mục")
tree.heading("mota", text="Mô tả")

tree.column("madm", width=70)
tree.column("tendm", width=200)
tree.column("mota", width=350)

tree.pack(fill="both", expand=True)
tree.bind("<<TreeviewSelect>>", on_select)

# Load dữ liệu ban đầu
load_data()

root.mainloop()
