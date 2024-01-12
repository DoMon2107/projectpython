class ControllerCongTy:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.buttons["Nhập"].config(command=self.load_nhan_vien())
        self.view.buttons["Tính lương"].config(command=self.tinh_luong_nv())
        self.view.buttons["Cập Nhật"].config(command=self.cap_nhat_nv())

    def load_nhan_vien(self):
        print("Click load")
        self.model.load_data()

    def tinh_luong_nv(self):
        print("Click tính lương", sum(self.model.ds_nv))

    def cap_nhat_nv(self):
        print("Click cập nhật")