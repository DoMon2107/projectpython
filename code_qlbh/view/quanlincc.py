import tkinter as tk
from tkinter import ttk

from code_qlbh.connection import ketnoidb
from tkinter import messagebox
class View_ncc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.db_manager = ketnoidb.DatabaseManager(
            server='DUCKHEE\\SQLEXPRESS',
            database='QLBH',
            username='',
            password=''
        )
    def start(self):
        self.root.mainloop()
    def setup_ui(self):
        self.geometry("906x662")
        self.title("QUẢN LÝ NHÀ CUNG CẤP")

        self.label = tk.Label(self, text="QUẢN LÝ NHÀ CUNG CẤP", font=("Arial", 18, "bold"))
        self.label.place(x=260, y=20)

        self.label_3 = tk.Label(self, text="Tên NCC:", font=("Arial", 10))
        self.label_3.place(x=160, y=180)

        self.table = ttk.Treeview(self, columns=("Mã NCC", "Tên NCC"), show="headings")
        self.table.heading("Mã NCC", text="Mã NCC")
        self.table.heading("Tên NCC", text="Tên NCC")
        self.table.place(x=160, y=250, width=251, height=331)
        self.table.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.button_add = tk.Button(self, text="THÊM", font=("Arial", 10), command=self.add_data)
        self.button_add.place(x=430, y=250)
        self.button_add.config(command=self.add_data)
        self.button_edit = tk.Button(self, text="SỬA", font=("Arial", 10), command=self.edit_data)
        self.button_edit.place(x=540, y=250)
        self.button_edit.config(command=self.edit_data)
        self.button_delete = tk.Button(self, text="XÓA", font=("Arial", 10), command=self.delete_data)
        self.button_delete.place(x=650, y=250)
        self.button_delete.config(command=self.delete_data)
        self.entry_1 = tk.Entry(self, font=("Arial", 12))
        self.entry_1.place(x=290, y=110, width=441)

        self.entry_2 = tk.Entry(self, font=("Arial", 12))
        self.entry_2.place(x=290, y=170, width=211)

        self.button_display = tk.Button(self, text="HIỂN THỊ", font=("Arial", 10), command=self.display_data)
        self.button_display.place(x=430, y=330)
        self.button_display.config(command=self.display_data)
        self.button_search = tk.Button(self, text="TÌM KIẾM", font=("Arial", 10))
        self.button_search.place(x=640, y=170)
        self.button_search.config(command=self.search_data)
        self.label_2 = tk.Label(self, text="Mã NCC:", font=("Arial", 10))
        self.label_2.place(x=160, y=120)
    def get_button_add(self):
        return self.button_add

    def set_add_button_command(self, command):
        self.button_add.config(command=command)
    
    def add_data(self):
        print("Add button pressed")
        maNCC = self.entry_1.get()
        tenNCC = self.entry_2.get()
        data = self.db_manager.display_data_ncc()
        print(data)
        success = self.db_manager.insert_data_ncc(maNCC, tenNCC)
        if success:
            messagebox.showinfo("Thông báo", "Thêm nhà cung cấp thành công!")
            self.display_data()  # Gọi hàm hiển thị dữ liệu từ controller
        else:
            messagebox.showerror("Lỗi", "Không thể thêm nhà cung cấp!")
    def display_data(self):
        data = self.db_manager.display_data_ncc()
        if data:
            self.table.delete(*self.table.get_children())  # Xóa dữ liệu cũ trên Treeview
            for row in data:
                mancc = row[0]
                tenncc = row[1]
                self.table.insert('', 'end', values=(str(mancc),str(tenncc)))
        
    def edit_data(self):
        selected_item = self.table.focus()  # Lấy dòng đang được chọn trong Treeview
        if selected_item:  # Kiểm tra xem có dòng nào được chọn không
            item = self.table.item(selected_item)
            row = item['values']  # Lấy giá trị của dòng được chọn

            if row:
                maNCC = row[0]  # Giả sử mã NCC được lưu ở cột đầu tiên
                new_tenNCC = self.entry_2.get()  # Giả sử sửa tên NCC qua entry_2

                success = self.db_manager.update_data_ncc(maNCC, new_tenNCC)

                if success:
                    messagebox.showinfo("Thông báo", "Sửa thông tin nhà cung cấp thành công!")
                    self.display_data()  # Hiển thị lại dữ liệu sau khi sửa
                else:
                    messagebox.showerror("Lỗi", "Không thể sửa thông tin nhà cung cấp!")
            else:
                messagebox.showerror("Lỗi", "Không có dữ liệu được chọn để sửa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn dữ liệu cần sửa!")


    def delete_data(self):
        selected_item = self.table.focus()  # Lấy dòng đang được chọn trong Treeview
        if selected_item:  # Kiểm tra xem có dòng nào được chọn không
            item = self.table.item(selected_item)
            row = item['values']  # Lấy giá trị của dòng được chọn

            if row:
                maNCC = row[0]  # Giả sử mã NCC được lưu ở cột đầu tiên
                success = self.db_manager.delete_data_ncc(maNCC)

                if success:
                    messagebox.showinfo("Thông báo", "Xóa nhà cung cấp thành công!")
                    self.display_data()  # Hiển thị lại dữ liệu sau khi xóa
                else:
                    messagebox.showerror("Lỗi", "Không thể xóa nhà cung cấp!")
            else:
                messagebox.showerror("Lỗi", "Không có dữ liệu được chọn để xóa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn dữ liệu cần xóa!")
    def on_tree_select(self, event):
        selected_item = self.table.focus()  # Lấy dòng đang được chọn trong Treeview
        if selected_item:  # Kiểm tra xem có dòng nào được chọn không
            item = self.table.item(selected_item)
            row = item['values']  # Lấy giá trị của dòng được chọn

            if row:
                maNCC = row[0]  # Giả sử mã NCC được lưu ở cột đầu tiên
                tenNCC = row[1]  # Giả sử tên NCC được lưu ở cột thứ hai (index 1)

                # Hiển thị dữ liệu tương ứng lên các Entry
                self.entry_1.delete(0, tk.END)  # Xóa dữ liệu cũ trong Entry 1
                self.entry_1.insert(0, maNCC)  # Hiển thị mã NCC
                self.entry_2.delete(0, tk.END)  # Xóa dữ liệu cũ trong Entry 2
                self.entry_2.insert(0, tenNCC)  # Hiển thị tên NCC
    def search_data(self):
        maNCC = self.entry_1.get()  # Lấy mã NCC từ entry hoặc widget tương ứng
        data = self.db_manager.search_data_ncc(maNCC)
        if data:
            self.table.delete(*self.table.get_children())  # Xóa dữ liệu cũ trên Treeview
            for row in data:
                mancc = row[0]
                tenncc = row[1]
                self.table.insert('', 'end', values=(str(mancc), str(tenncc)))
        else:
            messagebox.showinfo("Thông báo", "Không tìm thấy nhà cung cấp!")

# if __name__ == "__main__":
#     app = View_ncc()
#     app.mainloop()