import pyodbc


class DatabaseManager:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def create_connection(self):
        conn_str = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        try:
            conn = pyodbc.connect(conn_str)
            return conn
        except pyodbc.Error as e:
            print(f"Error creating connection: {e}")
            return None

    def close_connection(self, conn):
        try:
            conn.close()
        except pyodbc.Error as e:
            print(f"Error closing connection: {e}")

    def login_check(self, username, password):
        conn = self.create_connection()
        if conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM TaiKhoan WHERE TenTaiKhoan = '{username}'"
            cursor.execute(query)
            row = cursor.fetchone()

            if row:
                stored_password = row.MatKhau
                role = row.VaiTro

                if password == stored_password:
                    self.close_connection(conn)
                    if role == "admin":
                        return "admin"
                    elif role == "nhanvien":
                        return "nhanvien"
                else:
                    self.close_connection(conn)
                    return "wrong"
            else:
                self.close_connection(conn)
                return "not exist"

        return "loi ket noi"

    def display_data_ncc(self):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NhaCungCap")
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows  # Trả về dữ liệu từ bảng NhaCungCap
            except pyodbc.Error as e:
                print(f"Error executing query: {e}")
                self.close_connection(conn)
                return None
        return None

    def display_data_nv(self):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NhanVien")
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows  # Trả về dữ liệu từ bảng NhaCungCap
            except pyodbc.Error as e:
                print(f"Error executing query: {e}")
                self.close_connection(conn)
                return None
        return None

    def insert_data_ncc(self, maNCC, tenNCC):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO NhaCungCap (MaNCC, TenNCC) VALUES (?, ?)"
                cursor.execute(query, (maNCC, tenNCC))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error inserting data: {e}")
                self.close_connection(conn)
                return False
        return False

    def delete_data_ncc(self, maNCC):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM NhaCungCap WHERE MaNCC = ?"
                cursor.execute(query, (maNCC,))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error deleting data: {e}")
                self.close_connection(conn)
                return False
        return False

    def update_data_ncc(self, maNCC, tenNCC):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE NhaCungCap SET TenNCC = ? WHERE MaNCC = ?"
                cursor.execute(query, (tenNCC, maNCC))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error updating data: {e}")
                self.close_connection(conn)
                return False
        return False

    def search_data_ncc(self, maNCC):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM NhaCungCap WHERE MaNCC = ?"
                cursor.execute(query, (maNCC,))
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows
            except pyodbc.Error as e:
                print(f"Error searching data: {e}")
                self.close_connection(conn)
                return None
        return None

    def get_ncc_data(self):
        conn = self.create_connection()
        maNCC_list = []
        if conn:
            cursor = conn.cursor()
            query = "SELECT MaNCC FROM NhaCungCap"  # Lấy danh sách MaNCC từ bảng NhaCungCap
            cursor.execute(query)
            rows = cursor.fetchall()
            maNCC_list = [row[0] for row in rows] if rows else []  # Lấy danh sách MaNCC từ kết quả truy vấn
            self.close_connection(conn)
        return maNCC_list

        return None

    def insert_data_nhanvien(self, maNV, tenNV, ngaySinh, gioiTinh, diaChi, sdt):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO NhanVien (MaNV, TenNV, NgaySinh, GioiTinh, DiaChi, SDT) VALUES (?, ?, ?, ?, ?, ?)"
                cursor.execute(query, (maNV, tenNV, ngaySinh, gioiTinh, diaChi, sdt))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error inserting data: {e}")
                self.close_connection(conn)
                return False
        return False

    def delete_data_nhanvien(self, maNV):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM NhanVien WHERE MaNV = ?"
                cursor.execute(query, (maNV,))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error deleting data: {e}")
                self.close_connection(conn)
                return False
        return False

    def update_data_nhanvien(self, maNV, tenNV, ngaySinh, gioiTinh, diaChi, sdt):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE NhanVien SET TenNV = ?, NgaySinh = ?, GioiTinh = ?, DiaChi = ?, SDT = ? WHERE MaNV = ?"
                cursor.execute(query, (tenNV, ngaySinh, gioiTinh, diaChi, sdt, maNV))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error updating data: {e}")
                self.close_connection(conn)
                return False
        return False

    def search_data_nhanvien(self, maNV):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM NhanVien WHERE MaNV = ?"
                cursor.execute(query, (maNV,))
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows
            except pyodbc.Error as e:
                print(f"Error searching data: {e}")
                self.close_connection(conn)
                return None
        return None

    def get_nhanvien_data(self, id_):
        conn = self.create_connection()
        if conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM NhanVien WHERE MaNV = ?"
            cursor.execute(query, (id_,))
            row = cursor.fetchone()

            if row:
                self.close_connection(conn)
                return row
            else:
                self.close_connection(conn)
                return None

    def insert_data_sanpham(self, maSP, maNCC, tenSP, soLuong, donGiaNhap, donGiaBan):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO SanPham (MaSP, MaNCC, TenSP, SoLuong, DonGiaNhap, DonGiaBan) VALUES (?, ?, ?, ?, ?, ?)"
                cursor.execute(query, (maSP, maNCC, tenSP, soLuong, donGiaNhap, donGiaBan))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error inserting data: {e}")
                self.close_connection(conn)
                return False
        return False

    def delete_data_sanpham(self, maSP):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM SanPham WHERE MaSP = ?"
                cursor.execute(query, (maSP,))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error deleting data: {e}")
                self.close_connection(conn)
                return False
        return False

    def update_data_sanpham(self, maSP, maNCC, tenSP, soLuong, donGiaNhap, donGiaBan):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE SanPham SET MaNCC = ?, TenSP = ?, SoLuong = ?, DonGiaNhap = ?, DonGiaBan = ? WHERE MaSP = ?"
                cursor.execute(query, (maNCC, tenSP, soLuong, donGiaNhap, donGiaBan, maSP))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error updating data: {e}")
                self.close_connection(conn)
                return False
        return False

    def search_data_sanpham(self, maSP):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM SanPham WHERE MaSP = ?"
                cursor.execute(query, (maSP,))
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows
            except pyodbc.Error as e:
                print(f"Error searching data: {e}")
                self.close_connection(conn)
                return None
        return None

    def get_sanpham_data(self, maSP):
        conn = self.create_connection()
        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM SanPham WHERE MaSP = ?"
            cursor.execute(query, (maSP,))
            row = cursor.fetchone()

            if row:
                self.close_connection(conn)
                return row
            else:
                self.close_connection(conn)
                return None

    def display_data_sp(self):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM SanPham")
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows  # Trả về dữ liệu từ bảng NhaCungCap
            except pyodbc.Error as e:
                print(f"Error executing query: {e}")
                self.close_connection(conn)
                return None
        return None

    def get_masp(self):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT MaSP FROM SanPham")
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows  # Trả về dữ liệu từ bảng NhaCungCap
            except pyodbc.Error as e:
                print(f"Error executing query: {e}")
                self.close_connection(conn)
                return None
        return None

    def get_tensp(self):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT TenSP FROM SanPham")
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows  # Trả về dữ liệu từ bảng NhaCungCap
            except pyodbc.Error as e:
                print(f"Error executing query: {e}")
                self.close_connection(conn)
                return None
        return None

    def get_manv(self):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT MaNV FROM NhanVien")
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows  # Trả về dữ liệu từ bảng NhaCungCap
            except pyodbc.Error as e:
                print(f"Error executing query: {e}")
                self.close_connection(conn)
                return None
        return None

    def get_makh(self):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT MaKH FROM KhachHang")
                rows = cursor.fetchall()
                self.close_connection(conn)
                return rows  # Trả về dữ liệu từ bảng NhaCungCap
            except pyodbc.Error as e:
                print(f"Error executing query: {e}")
                self.close_connection(conn)
                return None
        return None

    def get_dongiaban_from_masp(self, ma_sp):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT DonGiaBan FROM SanPham WHERE MaSP = ?"
                cursor.execute(query, (ma_sp,))
                row = cursor.fetchone()
                self.close_connection(conn)

                if row:
                    return row[0]  # Trả về giá trị DonGiaBan nếu có
                else:
                    return None  # Trả về None nếu không tìm thấy MaSP tương ứng
            except pyodbc.Error as e:
                print(f"Error retrieving DonGiaBan: {e}")
                self.close_connection(conn)
                return None
        return None

    def insert_data_chitiethoadon(self, maHD, maSP, soLuong, donGia, giamGia, thanhTien):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO ChiTietHoaDon (MaHD, MaSP, SoLuong, DonGia, GiamGia, ThanhTien) VALUES (?, ?, ?, ?, ?, ?)"
                cursor.execute(query, (maHD, maSP, soLuong, donGia, giamGia, thanhTien))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error inserting data: {e}")
                self.close_connection(conn)
                return False
        return False

    def delete_data_chitiethoadon(self, maHD):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM ChiTietHoaDon WHERE MaHD = ?"
                cursor.execute(query, (maHD,))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error deleting data: {e}")
                self.close_connection(conn)
                return False
        return False

    def update_data_chitiethoadon(self, maHD, maSP, soLuong, donGia, giamGia, thanhTien):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE ChiTietHoaDon SET MaSP = ?, SoLuong = ?, DonGia = ?, GiamGia = ?, ThanhTien = ? WHERE MaHD = ?"
                cursor.execute(query, (maSP, soLuong, donGia, giamGia, thanhTien, maHD))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error updating data: {e}")
                self.close_connection(conn)
                return False
        return False

    def insert_data_hoadon(self, maHD, maNV, maKH, ngayBan, tongTien):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO HoaDon (MaHD, MaNV, MaKH, NgayBan, TongTien) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(query, (maHD, maNV, maKH, ngayBan, tongTien))
                conn.commit()
                self.close_connection(conn)
                return True
            except pyodbc.Error as e:
                print(f"Error inserting data: {e}")
                self.close_connection(conn)
                return False
        return False

