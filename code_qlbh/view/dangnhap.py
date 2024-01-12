import tkinter as tk
from code_qlbh.connection import ketnoidb
from tkinter import messagebox
from admin import MainWindow_admin
from nhanvien import Employee
class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ĐĂNG NHẬP")
        self.geometry("686x501")

        self.label = tk.Label(self, text="ĐĂNG NHẬP", font=("Arial", 18, "bold"))
        self.label.place(x=250, y=40)
        self.label_username = tk.Label(self, text="TÊN ĐĂNG NHẬP", font=("Arial", 10, "bold"))
        self.label_username.place(x=120, y=150)
        self.entry_username = tk.Entry(self, font=("Arial", 10, "bold"))
        self.entry_username.place(x=320, y=140, width=291, height=41)

        self.label_password = tk.Label(self, text="MẬT KHẨU", font=("Arial", 10, "bold"))
        self.label_password.place(x=120, y=240)
        self.entry_password = tk.Entry(self, show="*", font=("Arial", 10, "bold"))
        self.entry_password.place(x=320, y=230, width=291, height=41)

        self.button_login = tk.Button(self, text="ĐĂNG NHẬP", font=("Arial", 12, "bold"), command=self.login)
        self.button_login.place(x=110, y=320, width=211, height=51)

        self.button_exit = tk.Button(self, text="THOÁT", font=("Arial", 12, "bold"), command=self.destroy)
        self.button_exit.place(x=400, y=320, width=211, height=51)

        self.db_manager = ketnoidb.DatabaseManager(
            server='DUCKHEE\\SQLEXPRESS',
            database='QLBH',
            username='',  # Thay bằng tên người dùng thực tế của bạn
            password=''  # Thay bằng mật khẩu thực tế của bạn)
        )

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        result = self.db_manager.login_check(username, password)
        if result == "admin":
            messagebox.showinfo("Thông báo", "Đăng nhập thành công với vai trò admin")
            root_admin = MainWindow_admin()  # Tạo một cửa sổ con
            root_admin.mainloop()
        elif result == "nhanvien":
            messagebox.showinfo("Thông báo", "Đăng nhập thành công với vai trò nhân viên")
            root_ad = Employee()  # Tạo một cửa sổ con
            root_ad.mainloop()
        else:
            messagebox.showerror("Lỗi", result)

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
