import tkinter as tk
from tkinter import ttk, messagebox
from sql.ketnoi import KetNoi
from sql.database import CongTy, server, database


class UI:
    def __init__(self, master):
        self.master = master
        master.title("Quản lý Nhân viên")

        # Tạo instance của class KetNoi
        self.ket_noi = KetNoi(server, database)

        # Tạo instance của class CongTy
        self.ct = CongTy(server, database, self.ket_noi)


        # Tạo nút "Load Nhân viên"
        self.btn_load_nv = tk.Button(master, text="Load Nhân viên", command=self.load_nhan_vien_callback)
        self.btn_load_nv.pack(side=tk.LEFT, padx=10)


        # Tạo nút "Tính lương hàng tháng"
        self.btn_tinh_luong = tk.Button(master, text="Tính lương hàng tháng", command=self.tinh_luong_hang_thang)
        self.btn_tinh_luong.pack(side=tk.LEFT, padx=10)

        # Tạo nút "Thêm nhân viên"
        self.btn_them_nv = tk.Button(master, text="Thêm nhân viên", command=self.them_nhan_vien_callback)
        self.btn_them_nv.pack(side=tk.LEFT, padx=10)

        # Tạo Treeview để hiển thị dữ liệu Nhân viên
        self.treeview = ttk.Treeview(master, columns=('MaNV', 'HoTen', 'LuongCoBan', 'LuongHangThang'))
        self.treeview.heading('MaNV', text='Mã NV')
        self.treeview.heading('HoTen', text='Họ Tên')
        self.treeview.heading('LuongCoBan', text='Lương Cơ Bản')
        self.treeview.heading('LuongHangThang', text='Lương Hàng Tháng')
        self.treeview.pack(pady=10)

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

            if loaiNV == 'NhanVienKinhDoanh':
                soNgay = int(self.entry_so_ngay.get())
                self.ct.themNhanVien(maNV, hoTen, luongCoBan, loaiNV, soNgayLam=soNgay)
            elif loaiNV == 'NhanVienSanXuat':
                soSanPham = int(self.entry_so_san_pham.get())
                self.ct.themNhanVien(maNV, hoTen, luongCoBan, loaiNV, soSanPham=soSanPham)

            # Load lại dữ liệu sau khi thêm Nhân viên
            self.load_nhan_vien_callback()

            messagebox.showinfo("Thành công", "Thêm nhân viên thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()