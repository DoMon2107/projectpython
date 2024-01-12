from duchuy.connect import Connect
from tkinter import ttk, messagebox
class ControllerCongTy:
    def __init__(self,view,model,server,database, username=None, password=None):
        self.view=view
        self.model=model
        super().__init__()

        self.ket_noi = Connect(server, database, username, password)
        self.ds = []
        self.view.buttons["Load"].config(command=self.load_nhan_vien_callback)
        self.view.buttons["Tính lương"].config(command=self.tinh_luong_hang_thang)
        self.view.buttons["Thêm NV"].config(command=self.them_nhan_vien_callback)

    def load_nhan_vien_callback(self):
        try:
            # Load Nhân viên từ cơ sở dữ liệu
            self.model.loadNV()

            # Xóa dữ liệu cũ trong Treeview (nếu có)
            for row in self.view.treeview.get_children():
                self.view.treeview.delete(row)

            # Hiển thị dữ liệu mới trong Treeview
            for index, nv in enumerate(self.model.ds, start=1):
                self.view.treeview.insert('', 'end', values=(index, nv._maNV, nv._hoTen, nv._luongCoBan, nv._luongHT))

            # Cập nhật dữ liệu trong Treeview
            self.cap_nhat_du_lieu_treeview()

            messagebox.showinfo("Thành công", "Load Nhân viên thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def tinh_luong_hang_thang(self):
        try:
            # Tính lương hàng tháng
            self.model.tinhluongHT()

            # Cập nhật dữ liệu trong Treeview sau khi tính lương
            for row in self.view.treeview.get_children():
                self.view.treeview.delete(row)

            for index, nv in enumerate(self.model.ds, start=1):
                self.view.treeview.insert('', 'end', values=(index, nv._maNV, nv._hoTen, nv._luongCoBan, nv._luongHT))

            messagebox.showinfo("Thành công", "Tính lương hàng tháng thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Error: {e}")

    def cap_nhat_du_lieu_treeview(self):
        print("Cập nhật dữ liệu trong Treeview")
        # Xóa dữ liệu cũ trong Treeview
        for row in self.view.treeview.get_children():
            self.view.treeview.delete(row)

        # Hiển thị dữ liệu mới trong Treeview
        for index, nv in enumerate(self.model.ds, start=1):
            print(f"Thêm dữ liệu mới vào Treeview: {nv._maNV}, {nv._hoTen}, {nv._luongCoBan}, {nv._luongHT}")
            self.view.treeview.insert('', 'end', values=(index, nv._maNV, nv._hoTen, nv._luongCoBan, nv._luongHT))

    def them_nhan_vien_callback(self):
        try:
            maNV = self.view.efManv.get()
            hoTen = self.view.efHoten.get()
            luongCoBan = float(self.view.efLuongCB.get())
            loaiNV = ""

            if self.view.check_VP.get():
                loaiNV = "Văn Phòng"
            elif self.view.check_BH.get():
                loaiNV = "Bán Hàng"

            # Thêm nhân viên bằng cách gọi hàm themNhanVien
            self.model.themNhanVien(maNV, hoTen, luongCoBan, loaiNV)

            # Load lại dữ liệu sau khi thêm Nhân viên
            self.load_nhan_vien_callback()

            self.cap_nhat_du_lieu_treeview()

            self.view.messagebox.showinfo("Thành công", "Thêm nhân viên thành công.")
        except Exception as e:
            self.view.messagebox.showerror("Lỗi", f"Error: {e}")