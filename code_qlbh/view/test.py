import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        # Button để mở cửa sổ con
        self.open_window_button = tk.Button(root, text="Open Window", command=self.go_to_ncc)
        self.open_window_button.pack(pady=10)

    def go_to_ncc(self):
        # Tạo một cửa sổ con
        root_ncc = tk.Toplevel()
        root_ncc.title("Child Window")

        # Thêm các thành phần giao diện người dùng vào cửa sổ con
        label = tk.Label(root_ncc, text="This is a child window.")
        label.pack(pady=10)

        # Thêm một button đóng cửa sổ con
        close_button = tk.Button(root_ncc, text="Close", command=root_ncc.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()