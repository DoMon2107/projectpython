import tkinter as tk
from quanlincc import View_ncc
from quanlisp import ProductView
from quanlinv import EmployeeView
from qlbh1 import QLBH
from qlhd import QLHD


class MainWindow_admin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TRANG ADMIN")
        self.geometry("444x400")

        self.central_frame = tk.Frame(self)
        self.central_frame.pack(expand=True, fill=tk.BOTH)

        self.label = tk.Label(self.central_frame, text="ADMIN", font=("Arial", 18, "bold"))
        self.label.pack(pady=20)
        self.button_2 = tk.Button(self.central_frame, text="QUÁN LÝ NHÂN VIÊN", font=("Arial", 14, "bold"),
                                  command=self.go_to_nv)
        self.button_2.pack(pady=10)

        self.button = tk.Button(self.central_frame, text="QUÁN LÝ BÁN HÀNG", font=("Arial", 14, "bold"),
                                command=self.go_to_bh)
        self.button.pack(pady=10)

        self.button_3 = tk.Button(self.central_frame, text="QUẢN LÝ NHÀ CUNG CẤP", font=("Arial", 14, "bold"),
                                  command=self.go_to_ncc)
        self.button_3.pack(pady=10)

        self.button_4 = tk.Button(self.central_frame, text="QUÁN LÝ SẢN PHẨM", font=("Arial", 14, "bold"),
                                  command=self.go_to_sp)
        self.button_4.pack(pady=10)

        self.button_5 = tk.Button(self.central_frame, text="QUÁN LÝ HÓA ĐƠN", font=("Arial", 14, "bold"),
                                  command=self.go_to_hd)
        self.button_5.pack(pady=10)

    def go_to_ncc(self):
        root_ncc = View_ncc()  # Tạo một cửa sổ con
        root_ncc.mainloop()

    def go_to_sp(self):
        root_sp = ProductView()  # Tạo một cửa sổ con
        root_sp.mainloop()

    def go_to_nv(self):
        root_nv = EmployeeView()  # Tạo một cửa sổ con
        root_nv.mainloop()

    def go_to_bh(self):
        root_bh = QLBH()  # Tạo một cửa sổ con
        root_bh.mainloop()

    def go_to_hd(self):
        root_bh = QLHD()  # Tạo một cửa sổ con
        root_bh.mainloop()


if __name__ == "__main__":
    app = MainWindow_admin ()
    app.mainloop()

