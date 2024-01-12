import tkinter as tk
from tkinter import ttk
from datetime import datetime

from code_qlbh.connection import ketnoidb
from tkinter import messagebox


class QLBH(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db_manager = ketnoidb.DatabaseManager(
            server='DUCKHEE\\SQLEXPRESS',
            database='QLBH',
            username='',  # Thay bằng tên người dùng thực tế của bạn
            password=''  # Thay bằng mật khẩu thực tế của bạn)
        )
        self.setup_ui()
        self.update_masp_combobox()
        self.update_tensp_combobox()
        self.update_manv_combobox()
        self.update_makh_combobox()

    def setup_ui(self):
        self.title("Quản lý bán hàng")
        self.geometry("1092x980")

        self.centralwidget = tk.Frame(self)
        self.centralwidget.pack(expand=True, fill=tk.BOTH)

        self.comboBox = ttk.Combobox(self.centralwidget, width=15)
        self.comboBox.place(x=270, y=280)
        self.label_2 = tk.Label(self.centralwidget, text="MÃ HÓA ĐƠN", font=("Arial", 10))
        self.label_2.place(x=110, y=140)
        self.comboBox_2 = ttk.Combobox(self.centralwidget, width=15)
        self.comboBox_2.place(x=270, y=210)
        self.entry_6 = tk.Entry(self.centralwidget, width=30)
        self.entry_6.place(x=700, y=200)
        self.label_7 = tk.Label(self.centralwidget, text="TỔNG TIỀN", font=("Arial", 10))
        self.label_7.place(x=550, y=210)
        self.label = tk.Label(self.centralwidget, text="QUẢN LÝ BÁN HÀNG", font=("Arial", 18, "bold"))
        self.label.place(x=420, y=50)
        self.label_4 = tk.Label(self.centralwidget, text="MÃ KHÁCH HÀNG", font=("Arial", 10))
        self.label_4.place(x=110, y=210)
        self.pushButton = tk.Button(self.centralwidget, text="TẠO HÓA ĐƠN", font=("Arial", 10),
                                    command=self.display_current_datetime)
        self.pushButton.place(x=550, y=270)
        self.entry_5 = tk.Entry(self.centralwidget, width=30)
        self.entry_5.place(x=700, y=130)
        self.entry = tk.Entry(self.centralwidget, width=15)
        self.entry.place(x=270, y=130)
        self.label_6 = tk.Label(self.centralwidget, text="NGÀY LẬP", font=("Arial", 10))
        self.label_6.place(x=550, y=140)
        self.label_5 = tk.Label(self.centralwidget, text="MÃ NHÂN VIÊN", font=("Arial", 10))
        self.label_5.place(x=110, y=280)
        self.pushButton_2 = tk.Button(self.centralwidget, text="THÊM HÓA ĐƠN", font=("Arial", 10), command=self.add_hd)
        self.pushButton_2.place(x=760, y=270)
        self.pushButton_3 = tk.Button(self.centralwidget, text="THÊM", command=self.add_cthd)
        self.pushButton_3.place(x=50, y=790)
        self.label_8 = tk.Label(self.centralwidget, text="Đơn giá", font=("Arial", 10))
        self.label_8.place(x=50, y=650)
        self.entry_3 = tk.Entry(self.centralwidget, width=15)
        self.entry_3.place(x=200, y=570)
        self.label_9 = tk.Label(self.centralwidget, text="Giảm giá", font=("Arial", 10))
        self.label_9.place(x=50, y=720)
        self.entry_7 = tk.Entry(self.centralwidget, width=15)
        self.entry_7.place(x=200, y=720)
        self.label_10 = tk.Label(self.centralwidget, text="Số lượng", font=("Arial", 10))
        self.label_10.place(x=50, y=570)
        self.comboBox_3 = ttk.Combobox(self.centralwidget, width=15)
        self.comboBox_3.place(x=200, y=430)
        self.comboBox_3.bind("<<ComboboxSelected>>", self.update_product_info)
        self.label_11 = tk.Label(self.centralwidget, text="Mã sản phẩm", font=("Arial", 10))
        self.label_11.place(x=50, y=430)
        self.comboBox_4 = ttk.Combobox(self.centralwidget, width=15)
        self.comboBox_4.place(x=200, y=500)
        self.entry_4 = tk.Entry(self.centralwidget, width=15)
        self.entry_4.place(x=200, y=640)
        self.pushButton_4 = tk.Button(self.centralwidget, text="TỔNG KẾT", command=self.update_tongtien)
        self.pushButton_4.place(x=860, y=790)
        self.label_12 = tk.Label(self.centralwidget, text="Tên sản phẩm", font=("Arial", 10))
        self.label_12.place(x=50, y=500)
        self.pushButton_5 = tk.Button(self.centralwidget, text="SỬA", command=self.edit_cthd)
        self.pushButton_5.place(x=650, y=790)
        self.tableWidget = ttk.Treeview(self.centralwidget)
        self.tableWidget["columns"] = ("Mã sản phẩm", "Tên sản phẩm", "Số lượng", "Đơn giá", "Giảm giá", "Thành tiền")
        self.tableWidget.place(x=440, y=430)
        self.tableWidget.column("#0", width=0, stretch=tk.NO)
        self.tableWidget.column("Mã sản phẩm", width=100, anchor=tk.CENTER)
        self.tableWidget.column("Tên sản phẩm", width=100, anchor=tk.CENTER)
        self.tableWidget.column("Số lượng", width=100, anchor=tk.CENTER)
        self.tableWidget.column("Đơn giá", width=100, anchor=tk.CENTER)
        self.tableWidget.column("Giảm giá", width=100, anchor=tk.CENTER)
        self.tableWidget.column("Thành tiền", width=100, anchor=tk.CENTER)
        self.tableWidget.heading("Mã sản phẩm", text="Mã sản phẩm")
        self.tableWidget.heading("Tên sản phẩm", text="Tên sản phẩm")
        self.tableWidget.heading("Số lượng", text="Số lượng")
        self.tableWidget.heading("Đơn giá", text="Đơn giá")
        self.tableWidget.heading("Giảm giá", text="Giảm giá")
        self.tableWidget.heading("Thành tiền", text="Thành tiền")
        self.tableWidget.bind('<<TreeviewSelect>>', self.on_treeview_select)

        self.pushButton_6 = tk.Button(self.centralwidget, text="XÓA", command=self.delete_cthd)
        self.pushButton_6.place(x=440, y=790)

    def display_current_datetime(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.entry_5.delete(0, tk.END)
        self.entry_5.insert(0, current_datetime)

    def update_masp_combobox(self):
        data = self.db_manager.get_masp()
        result = [str(item[0]) for item in data]
        self.comboBox_3['values'] = ()
        self.comboBox_3['values'] = result

    def update_manv_combobox(self):
        data = self.db_manager.get_manv()
        result = [str(item[0]) for item in data]
        self.comboBox['values'] = ()
        self.comboBox['values'] = result

    def update_tensp_combobox(self):
        data = self.db_manager.get_tensp()
        result = [str(item[0]) for item in data]
        self.comboBox_4['values'] = ()
        self.comboBox_4['values'] = result

    def update_makh_combobox(self):
        data = self.db_manager.get_makh()
        result = [str(item[0]) for item in data]
        self.comboBox_2['values'] = ()
        self.comboBox_2['values'] = result

    def add_cthd(self):
        mahd = self.entry.get()
        masp = self.comboBox_3.get()
        tensp = self.comboBox_4.get()
        soluong = self.entry_3.get()
        dongia = self.entry_4.get()
        giamgia = self.entry_7.get()
        thanhtien = str(float(soluong) * float(dongia) * (100 - int(giamgia)) / 100)
        self.tableWidget.insert('', 'end', values=(masp, tensp, soluong, dongia, giamgia, thanhtien))

        # Insert data into the database
        success = self.db_manager.insert_data_chitiethoadon(mahd, masp, soluong, dongia, giamgia, thanhtien)
        if success:
            messagebox.showinfo("Thông báo", "Thêm cthd thành công!")
        else:
            messagebox.showerror("Lỗi", "Không thể thêm cthd!")

    def delete_cthd(self):
        # Lấy item được chọn trong Treeview
        selected_item = self.tableWidget.selection()
        if not selected_item:
            messagebox.showerror("Lỗi", "Vui lòng chọn dòng cần xóa!")
            return

        # Lấy giá trị của các cột trong dòng được chọn
        values = self.tableWidget.item(selected_item)['values']
        masp = values[0]  # Giả sử cột 'Mã sản phẩm' là cột đầu tiên

        # Xóa dòng được chọn trong Treeview
        self.tableWidget.delete(selected_item)

        # Xóa dữ liệu trong cơ sở dữ liệu
        success = self.db_manager.delete_data_chitiethoadon(
            masp)  # Gọi phương thức xóa dữ liệu chi tiết hóa đơn trong cơ sở dữ liệu
        if success:
            messagebox.showinfo("Thông báo", "Xóa cthd thành công!")
        else:
            messagebox.showerror("Lỗi", "Không thể xóa cthd!")

    def on_treeview_select(self, event):
        selected_item = self.tableWidget.focus()
        values = self.tableWidget.item(selected_item)['values']

        # Hiển thị dữ liệu từ dòng đã chọn lên các entry và combobox tương ứng
        # Giả sử cột đầu tiên là mã sản phẩm

        self.comboBox_3.set(values[0])
        self.comboBox_4.set(values[1])
        self.entry_3.delete(0, tk.END)
        self.entry_3.insert(0, values[2])
        self.entry_4.delete(0, tk.END)
        self.entry_4.insert(0, values[3])
        self.entry_7.delete(0, tk.END)
        self.entry_7.insert(0, values[4])

    def edit_cthd(self):
        # Lấy dòng được chọn trong Treeview
        selected_item = self.tableWidget.focus()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn dòng cần sửa!")
            return
        mahd = self.entry.get()
        masp = self.comboBox_3.get()
        tensp = self.comboBox_4.get()
        soluong = self.entry_3.get()
        dongia = self.entry_4.get()
        giamgia = self.entry_7.get()

        thanhtien = str(float(soluong) * float(dongia) * (100 - float(giamgia)) / 100)

        # Cập nhật dữ liệu vào Treeview
        self.tableWidget.item(selected_item, values=(masp, tensp, soluong, dongia, giamgia, thanhtien))

        # Cập nhật dữ liệu vào cơ sở dữ liệu
        success = self.db_manager.update_data_chitiethoadon(mahd, masp, soluong, dongia, giamgia, thanhtien)
        if success:
            messagebox.showinfo("Thông báo", "Sửa cthd thành công!")
        else:
            messagebox.showerror("Lỗi", "Không thể sửa cthd!")

    def calculate_total(self):
        total = 0.0
        for child in self.tableWidget.get_children():
            thanhtien = self.tableWidget.item(child, 'values')[-1]  # Lấy giá trị của cột "Thành tiền"
            total += float(thanhtien) if thanhtien else 0.0
        self.entry_6.delete(0, tk.END)
        self.entry_6.insert(0, total)

    def add_hd(self):
        mahd = self.entry.get()
        makh = self.comboBox_2.get()
        manv = self.comboBox.get()
        ngaylap = self.entry_5.get()
        tongtien = 0
        success = self.db_manager.insert_data_hoadon(mahd, manv, makh, ngaylap, tongtien)
        if success:
            messagebox.showinfo("Thông báo", "Thêm hóa đơn thành công!")
        else:
            messagebox.showerror("Lỗi", "Không thể thêm hóa đơn!")

    def update_tongtien(self):
        total = 0
        for child in self.tableWidget.get_children():
            thanhtien = self.tableWidget.item(child, 'values')[-1]  # Lấy giá trị của cột "Thành tiền"
            total += float(thanhtien) if thanhtien else 0
            self.db_manager.update_data_hoadon(self.entry.get(), int(total))
        for child in self.tableWidget.get_children():
            self.tableWidget.delete(child)
        self.comboBox['values'] = ()
        self.comboBox.set('')
        self.comboBox_2['values'] = ()
        self.comboBox_2.set('')
        self.comboBox_3['values'] = ()
        self.comboBox_3.set('')
        self.comboBox_4['values'] = ()
        self.comboBox_4.set('')
        self.entry.delete(0, tk.END)
        self.entry_3.delete(0, tk.END)
        self.entry_4.delete(0, tk.END)
        self.entry_5.delete(0, tk.END)
        self.entry_6.delete(0, tk.END)
        self.entry_7.delete(0, tk.END)

    def update_product_info(self, event):
        selected_masp = self.comboBox_3.get()
        tensp = self.db_manager.get_tensp_from_masp(selected_masp)
        dongiaban = self.db_manager.get_dongiaban_from_masp(selected_masp)
        if tensp is not None and dongiaban is not None:
            self.comboBox_4.set(tensp)
            self.entry_4.delete(0, tk.END)
            self.entry_4.insert(0, dongiaban)


if __name__ == "__main__":
    app = QLBH()
    app.mainloop()
