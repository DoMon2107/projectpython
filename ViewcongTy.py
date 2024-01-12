import tkinter as tk
from tkinter import ttk

class ViewCongTy(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly cong ty")
        self.geometry("350x150")

        self.buttons={
            "Nhập":tk.Button(self,text="Nhập"),
            "Tính lương": tk.Button(self,text="Tính lương"),
            "Cập Nhật": tk.Button(self,text="Cập Nhật")
        }

        self.buttons["Nhập"].grid(row=1, column=0)
        self.buttons["Tính lương"].grid(row=2,column=0)
        self.buttons["Cập Nhật"].grid(row=3,column=0)