import tkinter as tk
from tkinter import ttk
from duchuy.connect import Connect
from duchuy.Model import CongTyModel
from tkinter import font
from tkinter import ttk, messagebox

class ViewCongTy(tk.Tk):
    def __init__(self, server, database, username=None, password=None):
        super().__init__()
        self.title("Quan ly cong ty")
        self.geometry("350x150")

        self.stt_counter = 0

        self.ket_noi = Connect(server, database)

        self.ct = CongTyModel(server, database, self.ket_noi)

        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.lbTitle = tk.Label(text="TÍNH LƯƠNG NHÂN VIÊN", font=title_font)
        self.lbTitle.grid(row=0, column=1, pady=5, columnspan=2)

        # Label và Entry nằm cùng một dòng trên bảng
        self.lbManv = tk.Label(text="Mã nhân viên:")
        self.lbManv.grid(row=1, column=1)

        self.efManv = tk.Entry()
        self.efManv.grid(row=1, column=2)

        self.lbHoten = tk.Label(text="Họ tên:")
        self.lbHoten.grid(row=2, column=1)

        self.efHoten = tk.Entry()
        self.efHoten.grid(row=2, column=2)

        self.lbLoaiNV = tk.Label(text="Loại NV:")
        self.lbLoaiNV.grid(row=3, column=1)

        self.check_VP = tk.BooleanVar()
        self.checkbutton_VP = tk.Checkbutton(text="VP", variable=self.check_VP)
        self.checkbutton_VP.grid(row=3, column=2)

        self.check_BH = tk.BooleanVar()
        self.checkbutton_BH = tk.Checkbutton(text="BH", variable=self.check_BH)
        self.checkbutton_BH.grid(row=3, column=3)

        self.lbLuongCB = tk.Label(text="Lương CB:")
        self.lbLuongCB.grid(row=4, column=1)

        self.efLuongCB = tk.Entry()
        self.efLuongCB.grid(row=4, column=2)

        # Tạo Treeview để hiển thị dữ liệu Nhân viên
        self.treeview = ttk.Treeview(columns=('', 'MaNV', 'HoTen', 'LuongCoBan', 'LuongHangThang'),
                                     show=["headings"])
        self.treeview.heading('', text='')
        self.treeview.heading('MaNV', text='Mã NV')
        self.treeview.heading('HoTen', text='Họ Tên')
        self.treeview.heading('LuongCoBan', text='Lương Cơ Bản')
        self.treeview.heading('LuongHangThang', text='Lương Hàng Tháng')
        self.treeview.grid(row=7, column=0, columnspan=5)

        # Tạo Frame để chứa nút
        self.btn_frame = tk.Frame()
        self.btn_frame.grid(row=8, column=0, columnspan=4, pady=10)

        self.buttons = {
            "Load": tk.Button(self, text="Load"),
            "Tính lương": tk.Button(self, text="Tính lương"),
            "Thêm NV": tk.Button(self, text="Cập Nhật")
        }

        # self.buttons["Load"].grid(row=3, column=0)
        self.buttons["Load"].grid(row=9, column=1, padx=10)
        self.buttons["Tính lương"].grid(row=9, column=2, padx=10)
        self.buttons["Thêm NV"].grid(row=9, column=3, padx=10)

