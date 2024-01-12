import tkinter as tk

from tkinter import ttk
from code_qlbh.connection import ketnoidb

from tkinter import messagebox


class EmployeeView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("978x762")
        self.title("QUẢN LÝ NHÂN VIÊN")
        self.create_labels_and_entries()
        self.create_table()
        self.create_buttons()
        self.db_manager = ketnoidb.DatabaseManager(
            server='DUCKHEE\\SQLEXPRESS',
            database='QLBH',
            username='',  # Thay bằng tên người dùng thực tế của bạn
            password=''   # Thay bằng mật khẩu thực tế của bạn)
        )
    def create_labels_and_entries(self):
        label_frame = tk.Frame(self)
        label_frame.pack()

        labels = ["Mã NV", "Họ và tên", "Ngày sinh", "Giới tính", "Số ĐT", "Địa chỉ"]
        self.entries = []

        for i, text in enumerate(labels):
            label = tk.Label(label_frame, text=text + ":", font=("Arial", 10))
            label.grid(row=i, column=0, padx=10, pady=5)

            entry = tk.Entry(label_frame, font=("Arial", 10))
            entry.grid(row=i, column=1, padx=10, pady=5)

            self.entries.append(entry)

    def create_table(self):
        frame = tk.Frame(self)
        frame.pack(pady=20)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.table = ttk.Treeview(frame, columns=("ID", "Name", "DOB", "Gender", "Phone", "Address"),
                                  yscrollcommand=scrollbar.set)
        self.table.pack()

        self.table.heading("#0", text="", anchor=tk.CENTER)
        self.table.heading("ID", text="Mã NV")
        self.table.heading("Name", text="Họ và tên")
        self.table.heading("DOB", text="Ngày sinh")
        self.table.heading("Gender", text="Giới tính")
        self.table.heading("Phone", text="Số ĐT")
        self.table.heading("Address", text="Địa chỉ")

        self.table.column("#0", stretch=tk.NO, minwidth=0, width=0)
        self.table.column("ID", anchor=tk.CENTER, width=80)
        self.table.column("Name", anchor=tk.W, width=200)
        self.table.column("DOB", anchor=tk.CENTER, width=120)
        self.table.column("Gender", anchor=tk.CENTER, width=80)
        self.table.column("Phone", anchor=tk.CENTER, width=120)
        self.table.column("Address", anchor=tk.W, width=250)
        self.table.bind("<<TreeviewSelect>>", self.on_tree_select)
        scrollbar.config(command=self.table.yview)

    def create_buttons(self):
        button_frame = tk.Frame(self)
        button_frame.pack()

        button_add = tk.Button(button_frame, text="THÊM", font=("Arial", 10), command=self.add_nv)
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(button_frame, text="SỬA", font=("Arial", 10), command=self.edit_nv)
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(button_frame, text="XÓA", font=("Arial", 10), command=self.delete_nv)
        button_delete.pack(side=tk.LEFT, padx=10)

        button_display = tk.Button(button_frame, text="HIỂN THỊ", font=("Arial", 10), command=self.display_nv)
        button_display.pack(side=tk.LEFT, padx=10)

    def convert_date_format(date_string):
        parts = date_string.split('/')
        return f"{parts[2]}-{parts[1]}-{parts[0]}"

    def add_nv(self):
        # Lấy dữ liệu từ entry hoặc các widget tương ứng
        maNV = self.entries[0].get()
        tenNV = self.entries[1].get()
        ngaySinh = self.entries[2].get()
        gioiTinh = self.entries[3].get()
        diaChi = self.entries[4].get()
        sdt = self.entries[5].get()
        # Gọi hàm insert_data_nhanvien từ DatabaseManager để thêm dữ liệu
        success = self.db_manager.insert_data_nhanvien(maNV, tenNV, ngaySinh, gioiTinh, diaChi, sdt)
        if success:
            # Thông báo thêm thành công
            messagebox.showinfo("Thành công", "Thêm nhân viên thành công!")
            self.display_nv()
        else:
            # Thông báo thêm không thành công
            messagebox.showerror("Lỗi", "Không thể thêm nhân viên!")

    def edit_nv(self):
        pass

    def delete_nv(self):
        # Lấy dòng được chọn từ Treeview
        selected_item = self.table.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Vui lòng chọn nhân viên cần xóa.")
            return

        # Lấy thông tin của nhân viên từ dòng được chọn
        selected_nhanvien = self.table.item(selected_item, "values")

        # Lấy mã nhân viên từ thông tin
        maNV = selected_nhanvien[0]

        # Xóa dữ liệu từ cơ sở dữ liệu
        success = self.db_manager.delete_data_nhanvien(maNV)

        if success:
            # Xóa dòng từ Treeview nếu xóa thành công
            self.table.delete(selected_item)
            messagebox.showinfo("Thông báo", "Xóa nhân viên thành công.")
        else:
            messagebox.showerror("Lỗi", "Không thể xóa nhân viên.")

    def display_nv(self):
        # Xóa dữ liệu cũ trong Treeview (nếu có)
        for record in self.table.get_children():
            self.table.delete(record)

        # Lấy dữ liệu nhân viên từ cơ sở dữ liệu bằng phương thức get_all_nhanvien trong db_manager
        nhanviens = self.db_manager.display_data_nv()

        # Hiển thị dữ liệu lên Treeview
        for row in nhanviens:
            self.table.insert("", "end", values=(
            row[0], row[1], row[2], row[3], row[4], row[5]))  # Thêm dòng mới vào Treeview với thông tin của nhân viên

    def on_tree_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            values = self.table.item(selected_item)['values']
            for i, entry in enumerate(self.entries):
                if i < len(values):
                    entry.delete(0, tk.END)
                    entry.insert(0, values[i])

    def edit_nv(self):
        selected_item = self.table.focus()
        if selected_item:
            item_values = self.table.item(selected_item, "values")
            maNV = item_values[0]  # Assuming the first column contains the employee ID

            tenNV = self.entries[1].get()
            ngaySinh = self.entries[2].get()
            gioiTinh = self.entries[3].get()
            diaChi = self.entries[4].get()
            sdt = self.entries[5].get()

            success = self.db_manager.update_data_nhanvien(maNV, tenNV, ngaySinh, gioiTinh, diaChi, sdt)
            if success:
                # Refresh the displayed data after updating
                self.display_nv()
                messagebox.showinfo("Success", "Cập nhập nhân viên thành công!")
            else:
                messagebox.showerror("Error", "Cập nhập nhân viên thất bại!")

# if __name__ == "__main__":
#     app = EmployeeView()
#     app.mainloop()

