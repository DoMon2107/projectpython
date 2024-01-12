import pyodbc
from abc import ABC, abstractmethod

class abcNhanVien(ABC):

    @abstractmethod
    def tinhluongHT(self):
        pass


class NhanVien(abcNhanVien):
    def __init__(self, maNV, hoTen, luongCoBan):
        self._maNV = maNV
        self._hoTen = hoTen
        self._luongCoBan = luongCoBan
        self._luongHT = 0

    def __str__(self):
        return str([self._maNV, self._hoTen, self._luongCoBan, self._luongHT])


class NVVanPhong(NhanVien):
    def __init__(self, maNV, hoTen, luongCoBan, soNgayLam):
        NhanVien.__init__(self, maNV, hoTen, luongCoBan)
        self.__soNgayLam = soNgayLam

    def tinhluongHT(self):
        luong = self._luongCoBan + self.__soNgayLam * 180_000
        self._luongHT = luong
        return luong

class NVSanXuat(NhanVien):
    def __init__(self, maNV, hoTen, luongCoBan, soSanPham):
        NhanVien.__init__(self, maNV, hoTen, luongCoBan)
        self.__soSanPham = soSanPham

    def tinhluongHT(self):
        luong = self._luongCoBan + self.__soSanPham * 18_000
        self._luongHT = luong
        return luong

class CongTy:
    def __init__(self, server, database, username='ASUS', password=None):
        # Kết nối đến SQL Server
        if username and password:
            str_sql = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        else:
            str_sql = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"

        self.connection = pyodbc.connect(str_sql)
        self.cursor = self.connection.cursor()

    def loadNV(self):
        try:
            query = """
                SELECT NhanVien.MaNhanVien, HoTen, LuongCoBan, SoNgayLam, SoSanPham
                FROM NhanVien
                LEFT JOIN ChamCongTongHop ON NhanVien.MaNhanVien = ChamCongTongHop.MaNhanVien
            """
            result = self.cursor.execute(query).fetchall()

            self.__ds = []
            for row in result:
                maNV, hoTen, luongCoBan, soNgayLam, soSanPham = row
                if soNgayLam is not None:
                    nv = NVVanPhong(maNV, hoTen, luongCoBan, soNgayLam)
                elif soSanPham is not None:
                    nv = NVSanXuat(maNV, hoTen, luongCoBan, soSanPham)
                else:
                    nv = NhanVien(maNV, hoTen, luongCoBan)
                self.__ds.append(nv)

            print("Load employees data successfully.")

        except Exception as e:
            print(f"Error loading employees data: {e}")

    def tinhluongHT(self):
        try:
            for nv in self.__ds:
                nv.tinhluongHT()

            print("Calculate salaries successfully.")

        except Exception as e:
            print(f"Error calculating salaries: {e}")

    def themCotLuongHangThang(self):
        try:
            # Thêm cột LuongHangThang vào bảng NhanVien
            add_column_query = """
                ALTER TABLE NhanVien
                ADD LuongHangThang DECIMAL(10, 2)
            """
            self.cursor.execute(add_column_query)
            self.connection.commit()
            print("Column 'LuongHangThang' Thêm thành công.")

        except Exception as e:
            print(f"Error adding column 'LuongHangThang': {e}")

    def capNhatLuongHangThang(self):
        try:
            # Cập nhật giá trị của cột LuongHangThang
            for nv in self.__ds:
                maNV = nv._maNV
                luong = nv._luongHT

                if luong is not None:
                    update_query = f"""
                        UPDATE NhanVien
                        SET LuongHangThang = {luong}
                        WHERE MaNhanVien = '{maNV}'
                    """
                    self.cursor.execute(update_query)
                    self.connection.commit()

            print("Update 'LuongHangThang' successfully.")

        except Exception as e:
            print(f"Error updating 'LuongHangThang': {e}")

    def print(self):
        """In toàn bộ DS"""
        for nv in self.__ds:
            print(nv)


# Kết nối đến SQL Server
server = 'DUCKHEE'
database = 'qlnv'


# Tạo đối tượng CongTy và thực hiện các bước
ct = CongTy(server, database)
ct.loadNV()
ct.tinhluongHT()
ct.themCotLuongHangThang()
ct.capNhatLuongHangThang()
ct.print()
