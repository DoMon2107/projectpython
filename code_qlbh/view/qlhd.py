import tkinter as tk
from tkinter import ttk

from code_qlbh.connection import ketnoidb
from tkinter import messagebox
from datetime import datetime


class QLHD(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QUẢN LÍ HÓA ĐƠN")
        self.geometry("1145x938")

        self.label = tk.Label(self, text="QUẢN LÍ HÓA ĐƠN", font=("Arial", 18, "bold"))
        self.label.place(x=420, y=30)

        self.pushButton_5 = tk.Button(self, text="KHÔI PHỤC", font=("Arial", 10), command=self.display_hd)
        self.pushButton_5.place(x=810, y=700)

        self.textEdit = tk.Text(self, font=("Arial", 10), width=55, height=2)
        self.textEdit.place(x=330, y=100)

        self.pushButton_2 = tk.Button(self, text="THÊM", font=("Arial", 10), command=self.add_hd)
        self.pushButton_2.place(x=230, y=700)

        self.pushButton_4 = tk.Button(self, text="XÓA", font=("Arial", 10), command=self.delete_hd)
        self.pushButton_4.place(x=610, y=700)

        self.label_2 = tk.Label(self, text="MÃ HÓA ĐƠN", font=("Arial", 10))
        self.label_2.place(x=200, y=110)

        self.tableWidget = ttk.Treeview(self)
        self.tableWidget["columns"] = ("Mã hóa đơn", "Mã nhân viên", "Mã khách hàng", "Ngày bán", "Tổng tiền")
        self.tableWidget.place(x=250, y=440)
        self.setup_columns()

        self.pushButton_3 = tk.Button(self, text="SỬA", font=("Arial", 10), command=self.update_hd)
        self.pushButton_3.place(x=420, y=700)

        self.pushButton = tk.Button(self, text="TÌM KIẾM", font=("Arial", 10), command=self.search_hd)
        self.pushButton.place(x=850, y=100)

        self.textEdit_2 = tk.Text(self, font=("Arial", 10), width=55, height=2)
        self.textEdit_2.place(x=330, y=300)

        self.label_3 = tk.Label(self, text="NGÀY BÁN", font=("Arial", 10))
        self.label_3.place(x=200, y=310)

        self.textEdit_3 = tk.Text(self, font=("Arial", 10), width=55, height=2)
        self.textEdit_3.place(x=330, y=360)

        self.label_4 = tk.Label(self, text="TỔNG TIỀN", font=("Arial", 10))
        self.label_4.place(x=200, y=370)

        self.comboBox = ttk.Combobox(self)
        self.comboBox.place(x=330, y=170)

        self.label_5 = tk.Label(self, text="MÃ NV", font=("Arial", 10))
        self.label_5.place(x=200, y=180)

        self.label_6 = tk.Label(self, text="MÃ KH", font=("Arial", 10))
        self.label_6.place(x=200, y=240)

        self.comboBox_2 = ttk.Combobox(self)
        self.comboBox_2.place(x=330, y=230)

        self.db_manager = ketnoidb.DatabaseManager(
            server='DUCKHEE\\SQLEXPRESS',
            database='QLBH',
            username='',  # Thay bằng tên người dùng thực tế của bạn
            password=''  # Thay bằng mật khẩu thực tế của bạn)
        )
        self.update_manv_combobox()
        self.update_makh_combobox()
        self.display_hd()
        self.tableWidget.bind("<<TreeviewSelect>>", self.on_treeview_select)

    def setup_columns(self):
        self.tableWidget.column("#0", width=0, stretch=tk.NO)
        self.tableWidget.column("Mã hóa đơn", anchor=tk.CENTER, width=150)
        self.tableWidget.column("Mã nhân viên", anchor=tk.CENTER, width=150)
        self.tableWidget.column("Mã khách hàng", anchor=tk.CENTER, width=150)
        self.tableWidget.column("Ngày bán", anchor=tk.CENTER, width=150)
        self.tableWidget.column("Tổng tiền", anchor=tk.CENTER, width=150)

        self.tableWidget.heading("#0", text="")
        self.tableWidget.heading("Mã hóa đơn", text="Mã hóa đơn")
        self.tableWidget.heading("Mã nhân viên", text="Mã nhân viên")
        self.tableWidget.heading("Mã khách hàng", text="Mã khách hàng")
        self.tableWidget.heading("Ngày bán", text="Ngày bán")
        self.tableWidget.heading("Tổng tiền", text="Tổng tiền")

        self.db_manager = ketnoidb.DatabaseManager(
            server='DUCKHEE\\SQLEXPRESS',
            database='QLBH',
            username='',  # Thay bằng tên người dùng thực tế của bạn
            password=''  # Thay bằng mật khẩu thực tế của bạn)
        )

        self.update_manv_combobox()
        self.update_makh_combobox()
        self.display_hd()
        self.tableWidget.bind("<<TreeviewSelect>>", self.on_treeview_select)

    def setup_columns(self):
        self.tableWidget.column("#0", width=0, stretch=tk.NO)
        self.tableWidget.column("Mã hóa đơn", anchor=tk.CENTER, width=150)
        self.tableWidget.column("Mã nhân viên", anchor=tk.CENTER, width=150)
        self.tableWidget.column("Mã khách hàng", anchor=tk.CENTER, width=150)
        self.tableWidget.column("Ngày bán", anchor=tk.CENTER, width=150)
        self.tableWidget.column("Tổng tiền", anchor=tk.CENTER, width=150)

        self.tableWidget.heading("#0", text="")
        self.tableWidget.heading("Mã hóa đơn", text="Mã hóa đơn")
        self.tableWidget.heading("Mã nhân viên", text="Mã nhân viên")
        self.tableWidget.heading("Mã khách hàng", text="Mã khách hàng")
        self.tableWidget.heading("Ngày bán", text="Ngày bán")
        self.tableWidget.heading("Tổng tiền", text="Tổng tiền")

    def add_hd(self):
        # Lấy thông tin từ các widget trong giao diện
        maHD = self.textEdit.get("1.0", "end-1c")  # Lấy dữ liệu từ Text widget
        maNV = self.comboBox.get()  # Lấy dữ liệu từ ComboBox
        maKH = self.comboBox_2.get()  # Lấy dữ liệu từ ComboBox
        ngayBan = self.textEdit_2.get("1.0", "end-1c")  # Lấy dữ liệu từ Text widget
        tongTien = self.textEdit_3.get("1.0", "end-1c")  # Lấy dữ liệu từ Text widget

        # Kiểm tra dữ liệu
        if not all([maHD, maNV, maKH, ngayBan, tongTien]):
            messagebox.showwarning("Warning", "Vui lòng nhập đầy đủ thông tin hóa đơn.")
            return

        # Gọi hàm insert_data_hoadon từ DatabaseManager
        success = self.db_manager.insert_data_hoadon(maHD, maNV, maKH, ngayBan, tongTien)

        # Kiểm tra kết quả và thông báo
        if success:
            messagebox.showinfo("Thông báo", "Thêm hóa đơn thành công.")
            self.display_hd()
        else:
            messagebox.showerror("Lỗi", "Không thể thêm hóa đơn.")

    def update_manv_combobox(self):
        data = self.db_manager.get_manv()
        result = [str(item[0]) for item in data]
        self.comboBox['values'] = ()
        self.comboBox['values'] = result

    def update_makh_combobox(self):
        data = self.db_manager.get_makh()
        result = [str(item[0]) for item in data]
        self.comboBox_2['values'] = ()
        self.comboBox_2['values'] = result

    def display_hd(self):
        for item in self.tableWidget.get_children():
            self.tableWidget.delete(item)
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = self.db_manager.display_data_hoadon()

        # Hiển thị dữ liệu trên Treeview
        for row in data:
            self.tableWidget.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

    def delete_hd(self):
        # Lấy dòng được chọn từ Treeview
        selected_item = self.tableWidget.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Vui lòng chọn hóa đơn cần xóa.")
            return

        # Lấy thông tin của hóa đơn từ dòng được chọn
        selected_hd = self.tableWidget.item(selected_item, "values")
        maHD = selected_hd[0]

        # Gọi hàm delete_data_hoadon từ DatabaseManager
        success = self.db_manager.delete_data_hoadon(maHD)

        # Kiểm tra kết quả và thông báo
        if success:
            # Xóa dòng khỏi Treeview
            self.tableWidget.delete(selected_item)
            messagebox.showinfo("Thông báo", "Xóa hóa đơn thành công.")
        else:
            messagebox.showerror("Lỗi", "Không thể xóa hóa đơn.")

    def search_hd(self):
        # Lấy thông tin từ ô nhập liệu hoặc ô Combobox
        maHD_search = self.textEdit.get("1.0", tk.END).strip()

        # Gọi hàm search_data_hoadon từ DatabaseManager
        result = self.db_manager.search_data_hoadon(maHD_search)

        # Hiển thị kết quả trên Treeview
        self.display_search_result(result)

    def display_search_result(self, row):
        # Xóa dữ liệu cũ trên Treeview
        for item in self.tableWidget.get_children():
            self.tableWidget.delete(item)
        if row is not None:
            messagebox.showinfo("Thông báo", "Tìm thấy hóa đơn có mã hóa đơn là " + str(row[0]))
            self.tableWidget.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]))
        else:
            messagebox.showerror("Lỗi", "Không tồn tại mã  hóa đơn.")

    def on_treeview_select(self, event):
        selected_item = self.tableWidget.selection()
        if selected_item:
            # Lấy thông tin của hóa đơn từ dòng được chọn
            selected_hd = self.tableWidget.item(selected_item, "values")

            # Hiển thị thông tin lên các widget
            self.textEdit.delete("1.0", tk.END)
            self.textEdit.insert(tk.END, selected_hd[0])  # Giả sử thông tin đầu tiên là mã hóa đơn

            self.textEdit_2.delete("1.0", tk.END)
            self.textEdit_2.insert(tk.END, selected_hd[3])  # Thay bằng thông tin thích hợp từ selected_hd

            self.textEdit_3.delete("1.0", tk.END)
            self.textEdit_3.insert(tk.END, selected_hd[4])  # Thay bằng thông tin thích hợp từ selected_hd

            # Tương tự cho các widget kiểu combobox
            self.comboBox.set(selected_hd[1])  # Giả sử selected_hd[3] là mã nhân viên
            self.comboBox_2.set(selected_hd[2])

    def update_hd(self):
        selected_item = self.tableWidget.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Vui lòng chọn hóa đơn cần cập nhật.")
            return
        selected_hd = self.tableWidget.item(selected_item, "values")
        mahd = selected_hd[0]
        new_mahd = self.textEdit.get("1.0", tk.END).strip()  # Provide the range "1.0" to tk.END
        new_manv = self.comboBox.get().strip()
        new_makh = self.comboBox_2.get().strip()
        new_ngayban = new_ngayban = datetime.strptime(self.textEdit_2.get("1.0", tk.END).strip(), "%Y-%m-%d %H:%M:%S")
        new_tongtien = self.textEdit_3.get("1.0", tk.END).strip()
        print(new_ngayban)
        # Thực hiện kiểm tra dữ liệu và xử lý lưu vào cơ sở dữ liệu
        success = self.db_manager.update_data_hoadon(mahd, new_manv, new_makh, new_ngayban, new_tongtien)
        print(success)
        # Nếu cập nhật thành công, cập nhật dữ liệu trong Treeview
        if success:
            self.tableWidget.item(selected_item, values=(new_mahd, new_manv, new_makh, new_ngayban, new_tongtien))
            messagebox.showinfo("Thông báo", "Cập nhật hóa đơn thành công.")
        else:
            messagebox.showerror("Lỗi", "Không thể cập nhật hóa đơn.")


if __name__ == "__main__":
    app = QLHD()
    app.mainloop()