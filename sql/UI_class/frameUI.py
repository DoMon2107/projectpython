import tkinter as tk
from tkinter import ttk, messagebox
from sql.UI_class.Connect import KetNoi
from sql.UI_class.classDB import CongTy, server, database


class UI:
    def __init__(self, master):
        self.master = master
        master.title("Quản lý Nhân viên")

        # Tạo instance của class KetNoi
        self.ket_noi = KetNoi(server, database)

        # Tạo instance của class CongTy
        self.ct = CongTy(server, database, self.ket_noi)

        entry_frame = tk.Frame(master)
        entry_frame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.W)

        # Entry widgets for entering employee information
        tk.Label(entry_frame, text="Mã Nhân Viên:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_ma_nv = tk.Entry(entry_frame, width=20)
        self.entry_ma_nv.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(entry_frame, text="Họ Và Tên:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_ho_ten = tk.Entry(entry_frame, width=20)
        self.entry_ho_ten.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(entry_frame, text="Lương Cơ Bản:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_luong_co_ban = tk.Entry(entry_frame, width=20)
        self.entry_luong_co_ban.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(entry_frame, text="Loại Nhân Viên:").grid(row=3, column=0, padx=5, pady=5)
        self.var_loai_nv = tk.StringVar()
        self.combo_loai_nv = ttk.Combobox(entry_frame, textvariable=self.var_loai_nv,
                                          values=['NhanVienVanPhong', 'NhanVienSanXuat'])
        self.combo_loai_nv.set('NhanVienVanPhong')  # Set default value
        self.combo_loai_nv.grid(row=3, column=1, padx=5, pady=5)

        # Entry NgayLam
        tk.Label(entry_frame, text="Ngày làm :").grid(row=4, column=0, padx=5, pady=5)
        self.entry_ngay_lam = tk.Entry(entry_frame, width=20)
        self.entry_ngay_lam.grid(row=4, column=1, padx=5, pady=5)

        # Entry SanPham
        tk.Label(entry_frame, text="Sản phẩm :").grid(row=5, column=0, padx=5, pady=5)
        self.entry_san_pham = tk.Entry(entry_frame, width=20)
        self.entry_san_pham.grid(row=5, column=1, padx=5, pady=5)

        # Button for adding employee
        self.btn_add_employee = tk.Button(entry_frame, text="Thêm Nhân viên", command=self.them_nhan_vien_callback)
        self.btn_add_employee.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Tạo một frame để chứa ba nút
        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.N)
        # LOAD
        self.btn_load_nv = tk.Button(button_frame, text="Load Nhân viên", command=self.load_nhan_vien_callback)
        self.btn_load_nv.pack(side=tk.LEFT, padx=10, pady=10)
        # THEM
        self.btn_them_nv = tk.Button(button_frame, text="Thêm nhân viên", command=self.them_nhan_vien_callback)
        self.btn_them_nv.pack(side=tk.LEFT, padx=10, pady=10)
        # TINH LUONG
        self.btn_tinh_luong = tk.Button(button_frame, text="Tính lương hàng tháng", command=self.tinh_luong_hang_thang)
        self.btn_tinh_luong.pack(side=tk.LEFT, padx=10, pady=10)

        # Tạo Treeview để hiển thị dữ liệu Nhân viên
        self.treeview = ttk.Treeview(master, columns=('MaNV', 'HoTen', 'LuongCoBan', 'LuongHangThang'))
        self.treeview.heading('#0',text='',anchor=tk.W)
        self.treeview.heading('MaNV', text='Mã Nhân Viên')
        self.treeview.heading('HoTen', text='Họ Và Tên')
        self.treeview.heading('LuongCoBan', text='Lương Cơ Bản')
        self.treeview.heading('LuongHangThang', text='Lương Hàng Tháng')
        self.treeview.column('#0',width=0,stretch=tk.NO)
        self.treeview.column('MaNV',width=120)
        self.treeview.column('HoTen', width=120)
        self.treeview.column('LuongCoBan', width=120)
        self.treeview.column('LuongHangThang', width=120)
        self.treeview.pack(pady=5)


    def load_nhan_vien_callback(self):
        try:
            # Load Nhân viên từ cơ sở dữ liệu
            self.ct.loadNV()

            # Xóa dữ liệu cũ trong Treeview (nếu có)
            for row in self.treeview.get_children():
                self.treeview.delete(row)

            # Hiển thị dữ liệu mới trong Treeview
            for nv in self.ct.ds:
                self.treeview.insert('', 'end', values=(nv._maNV, nv._hoTen, nv._luongCoBan, nv._luongHT))

            messagebox.showinfo("Thành công", "Load Nhân viên thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def tinh_luong_hang_thang(self):
        try:
             # Tính lương hàng tháng
            self.ct.tinhluongHT()

               # Cập nhật dữ liệu trong Treeview sau khi tính lương
            for i, nv in enumerate(self.ct.ds):
                self.treeview.item(self.treeview.get_children()[i],
                                    values=(nv._maNV, nv._hoTen, nv._luongCoBan, nv._luongHT))

            messagebox.showinfo("Thành công", "Tính lương hàng tháng thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def them_nhan_vien_callback(self):
        try:
            maNV = self.entry_ma_nv.get()
            hoTen = self.entry_ho_ten.get()
            luongCoBan = float(self.entry_luong_co_ban.get())
            loaiNV = self.var_loai_nv.get()
            if loaiNV == 'NhanVienVanPhong':
                soNL = self.entry_ngay_lam.get()
                self.ct.themNhanVien(maNV, hoTen, luongCoBan, loaiNV, soNL)
                print(maNV, hoTen, luongCoBan, loaiNV, soNL)
            elif loaiNV == 'NhanVienSanXuat':
                soSP = self.entry_san_pham.get()
                self.ct.themNhanVien(maNV, hoTen, luongCoBan, loaiNV, soSP)
                print(maNV, hoTen, luongCoBan, loaiNV, soSP)

            messagebox.showinfo("Thành công", "Thêm nhân viên thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()