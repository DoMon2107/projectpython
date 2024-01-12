import tkinter as tk
from tkinter import messagebox
from code_qlbh.view import qlbh1
class Employee(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("664x403")
        self.title("NHÂN VIÊN")
        self.label = tk.Label(self, text="NHÂN VIÊN", font=("Arial", 18, "bold"))
        self.label.place(x=240, y=80)
        self.button_invoice = tk.Button(self, text="QUẢN LÝ HÓA ĐƠN", font=("Arial", 14, "bold"), command=self.open_invoice_management)
        self.button_invoice.place(x=180, y=180, width=301, height=61)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def open_invoice_management(self):
        root_sp = qlbh1.QLBH()  # Tạo một cửa sổ con
        root_sp.mainloop()
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

# if __name__ == "__main__":
#     app = Employee()
#     app.mainloop()
