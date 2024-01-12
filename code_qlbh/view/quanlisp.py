import tkinter as tk
from tkinter import ttk

from code_qlbh.connection import ketnoidb
from tkinter import messagebox


class ProductView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1018x843")
        self.title("QUẢN LÝ SẢN PHẨM")
        self.db_manager = ketnoidb.DatabaseManager(
            server='DUCKHEE\\SQLEXPRESS',
            database='QLBH',
            username='',  # Thay bằng tên người dùng thực tế của bạn
            password=''  # Thay bằng mật khẩu thực tế của bạn)
        )
        self.create_table()
        self.create_input_fields()
        self.create_buttons()
        self.update_ncc_combobox()

    def create_table(self):
        self.table = ttk.Treeview(self, columns=("Mã SP", "Mã NCC", "Tên SP", "Số lượng", "Giá nhập", "Giá bán",))
        self.table.heading("#0", text="", anchor=tk.CENTER)
        self.table.heading("Mã SP", text="Mã sản phẩm")
        self.table.heading("Mã NCC", text="Mã nhà cung cấp")
        self.table.heading("Tên SP", text="Tên sản phẩm")
        self.table.heading("Số lượng", text="Số lượng")
        self.table.heading("Giá nhập", text="Giá nhập")
        self.table.heading("Giá bán", text="Giá bán")
        self.table.column("#0", stretch=tk.NO, minwidth=0, width=0)
        self.table.column("Mã SP", anchor=tk.CENTER, width=120)
        self.table.column("Mã NCC", anchor=tk.CENTER, width=120)
        self.table.column("Tên SP", anchor=tk.CENTER, width=200)
        self.table.column("Số lượng", anchor=tk.CENTER, width=120)
        self.table.column("Giá nhập", anchor=tk.CENTER, width=120)
        self.table.column("Giá bán", anchor=tk.CENTER, width=120)
        self.table.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.table.pack(padx=20, pady=20)

    # def create_input_fields(self):
    #     labels = ["MÃ SẢN PHẨM", "MÃ NCC", "TÊN SẢN PHẨM", "SỐ LƯỢNG", "GIÁ NHẬP", "GIÁ BÁN"]
    #     self.entries = []
    #     for i, text in enumerate(labels):
    #         label = tk.Label(self, text=text + ":", font=("Arial", 10))
    #         label.place(x=100, y=380 + i * 60)
    #         if text == "MÃ NCC":
    #             combobox = ttk.Combobox(self, values=["Option 1", "Option 2", "Option 3"])  # Replace with actual values
    #             combobox.place(x=240, y=380 + i * 60, width=200)
    #             self.entries.append(combobox)
    #         else:
    #             entry = tk.Entry(self)
    #             entry.place(x=240, y=380 + i * 60, width=200)
    #             self.entries.append(entry)
    def create_input_fields(self):
        labels = ["MÃ SẢN PHẨM", "MÃ NCC", "TÊN SẢN PHẨM", "SỐ LƯỢNG", "GIÁ NHẬP", "GIÁ BÁN"]
        self.entries = []

        for i, text in enumerate(labels):
            label = tk.Label(self, text=text + ":", font=("Arial", 10))
            label.place(x=100, y=380 + i * 60)

            if text == "MÃ NCC":
                ncc_values = ["NCC 1", "NCC 2", "NCC 3"]  # Thay thế bằng danh sách Mã Nhà cung cấp thực tế
                ma_ncc_combobox = ttk.Combobox(self, values=ncc_values)
                ma_ncc_combobox.place(x=240, y=380 + i * 60, width=200)
                self.entries.append(ma_ncc_combobox)
            else:
                entry = tk.Entry(self)
                entry.place(x=240, y=380 + i * 60, width=200)
                self.entries.append(entry)

    def create_buttons(self):
        button_add = tk.Button(self, text="THÊM", font=("Arial", 12), command=self.add_sp)
        button_add.place(x=100, y=730)
        button_edit = tk.Button(self, text="SỬA", font=("Arial", 12), command=self.edit_sp)
        button_edit.place(x=250, y=730)

        button_delete = tk.Button(self, text="XÓA", font=("Arial", 12), command=self.delete_sp)
        button_delete.place(x=400, y=730)

        button_restore = tk.Button(self, text="KHÔI PHỤC", font=("Arial", 12), command=self.display_sp)
        button_restore.place(x=550, y=730)

    def add_sp(self):
        maSP = self.entries[0].get()
        maNCC = self.entries[1].get()  # Assuming MÃ NCC is the last entry
        tenSP = self.entries[2].get()
        soLuong = self.entries[3].get()
        donGiaNhap = self.entries[4].get()
        donGiaBan = self.entries[5].get()

        # Add data to the tree view
        self.table.insert('', 'end', values=(maSP, maNCC, tenSP, soLuong, donGiaNhap, donGiaBan))

        # Insert data into the database
        success = self.db_manager.insert_data_sanpham(maSP, maNCC, tenSP, soLuong, donGiaNhap, donGiaBan)
        if success:
            messagebox.showinfo("Thông báo", "Thêm sản phẩm thành công!")
        else:
            messagebox.showerror("Lỗi", "Không thể thêm sản phẩm!")

    def get_entry_values(self):
        entry_values = [entry.get() for entry in self.entries]
        return entry_values

    def display_sp(self):
        for record in self.table.get_children():
            self.table.delete(record)
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = self.db_manager.display_data_sp()

        # Hiển thị dữ liệu trên Treeview
        for row in data:
            self.table.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5]))

    def delete_sp(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Thông báo", "Vui lòng chọn một sản phẩm để xóa!")
            return

        confirmation = messagebox.askyesno("Xác nhận xóa", "Bạn có chắc chắn muốn xóa sản phẩm này?")
        if confirmation:
            # Lấy mã sản phẩm được chọn để xóa
            selected_id = self.table.item(selected_item)['values'][0]  # Giả sử cột đầu tiên chứa mã sản phẩm

            # Xóa sản phẩm từ cơ sở dữ liệu
            success = self.db_manager.delete_data_sanpham(selected_id)

            if success:
                # Xóa dòng tương ứng trong Treeview
                self.table.delete(selected_item)
                messagebox.showinfo("Thông báo", "Đã xóa sản phẩm thành công!")
            else:
                messagebox.showerror("Lỗi", "Không thể xóa sản phẩm!")

    def on_tree_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            values = self.table.item(selected_item)['values']
            for i, entry in enumerate(self.entries):
                if i < len(values):
                    entry.delete(0, tk.END)
                    entry.insert(0, values[i])

    def edit_sp(self):
        selected_item = self.table.selection()
        if selected_item:
            sp_id = self.table.item(selected_item)['values'][0]  # Lấy ID sản phẩm từ dòng được chọn

            # Lấy thông tin mới từ các Entry
            maSP = self.entries[0].get()
            maNCC = self.entries[1].get()  # Assuming MÃ NCC is the last entry
            tenSP = self.entries[2].get()
            soLuong = self.entries[3].get()
            donGiaNhap = self.entries[4].get()
            donGiaBan = self.entries[5].get()

            # Gọi hàm cập nhật dữ liệu trong cơ sở dữ liệu với các giá trị mới từ Entry
            success = self.db_manager.update_data_sanpham(maSP, maNCC, tenSP, soLuong, donGiaNhap, donGiaBan)
            if success:
                messagebox.showinfo("Thông báo", "Sửa sản phẩm thành công!")
                self.display_sp()  # Hiển thị lại danh sách sản phẩm sau khi sửa
            else:
                messagebox.showerror("Lỗi", "Không thể sửa sản phẩm!")

    def update_ncc_combobox(self):
        maNCC_list = self.db_manager.get_ncc_data()  # Đây là hàm bạn cần viết trong DatabaseManager để lấy danh sách MaNCC
        self.entries[1]['values'] = []
        self.entries[1]['values'] = maNCC_list


if __name__ == "__main__":
    app = ProductView()
    app.mainloop()

