from tkinter import *
from tkinter import ttk
import tkinter as tk
#Tạo cửa sổ giao diện
window=tk.Tk()
#w=Tk()

#Tạo Treeview
tree= ttk.Treeview(window)

#Tạo các cột trong Treeview
tree["columns"]=("column1","column2","column3")

#Đặt tên cho từng cột
tree.heading("column1", text="Cột 1")
tree.heading("column2", text="Cột 2")
tree.heading("column3", text="Cột 3")

#thêm dữ liệu vào bảng
tree.insert("", tk.END, text="Dòng 1", values=("giá trị 1","giá trị 2","giá trị 3"))
tree.insert("", tk.END, text="Dòng 2",values=("giá trị 4","giá trị 5","giá trị 6"))

#Hiển thị Treeview
tree.pack()

#Chạy giao diện
window.mainloop()