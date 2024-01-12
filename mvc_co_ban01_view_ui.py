# Model
class CongTyModel:
    def __init__(self):
        self.dsNV = []

    def get_ds_nhan_vien(self):
        return self.dsNV

    def load_nhan_vien(self):
        self.dsNV.append({"maNV": 123, "hoTen": 'Văn A', "luongHT": 10_000_000})
        self.dsNV.append({"maNV": 124, "hoTen": 'Văn B', "luongHT": 11_000_000})
        self.dsNV.append({"maNV": 125, "hoTen": 'Văn C', "luongHT": 12_000_000})
        self.dsNV.append({"maNV": 126, "hoTen": 'Văn D', "luongHT": 13_000_000})
        self.dsNV.append({"maNV": 127, "hoTen": 'Văn E', "luongHT": 14_000_000})

# View
import tkinter as tk
from tkinter import ttk
class CongTyView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.geometry('600x300')

        self.ds_nhan_vien = ttk.Treeview()
        self.ds_nhan_vien.pack()

        self.button = tk.Button(self, text="Load NV",
                                command=self.controller.load_nhan_vien)
        self.button.pack()

    def show_ds_nhan_vien(self, ds_nhan_vien: list):
        self.ds_nhan_vien.delete(*self.ds_nhan_vien.get_children())
        self.ds_nhan_vien['columns'] = ('maNV', 'hoTen', 'luongHT')
        # Đặt tên cho các cột
        self.ds_nhan_vien.column("#0", width=50, minwidth=50)
        self.ds_nhan_vien.column("maNV", width=100, minwidth=100)
        self.ds_nhan_vien.column("hoTen", width=200, minwidth=100)
        self.ds_nhan_vien.column("luongHT", width=200, minwidth=100)

        # Đặt tiêu đề cho các cột
        self.ds_nhan_vien.heading("#0", text="STT")
        self.ds_nhan_vien.heading("maNV", text="Mã NV")
        self.ds_nhan_vien.heading("hoTen", text="Họ và tên")
        self.ds_nhan_vien.heading("luongHT", text="Lương hằng tháng")

        # Thêm dữ liệu vào bảng

        for index, nv in enumerate(ds_nhan_vien):
            self.ds_nhan_vien.insert("", tk.END, text=index+1,
                                     values=tuple(nv.values()))

        # Hiển thị bảng
        #self.ds_nhan_vien.pack(
        #self.mainloop()

    def update_view(self, data):
        self.show_ds_nhan_vien(data)

# Controller
class CongTyController:
    def __init__(self, model: CongTyModel, view: CongTyView):
        self.model = model
        self.view = view

    def load_nhan_vien(self):
        self.model.load_nhan_vien()
        self.view.show_ds_nhan_vien(self.model.get_ds_nhan_vien())

# Main application
if __name__ == "__main__":
    model = CongTyModel()
    controller = CongTyController(model=model, view=None)  # View sẽ được cung cấp sau khi khởi tạo
    view = CongTyView(controller=controller)
    controller.view = view
    #Show view
    view.mainloop()




