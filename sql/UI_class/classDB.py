# nhanvien.py
from abc import ABC, abstractmethod
from sql.UI_class.Connect import KetNoi

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
        if self.__soNgayLam is not None:
            luong = self._luongCoBan + self.__soNgayLam * 180_000
            self._luongHT = luong
            return luong
        else:
            return 0

class NVSanXuat(NhanVien):
    def __init__(self, maNV, hoTen, luongCoBan, soSanPham):
        NhanVien.__init__(self, maNV, hoTen, luongCoBan)
        self.__soSanPham = soSanPham

    def tinhluongHT(self):
        if self.__soSanPham is not None:
            luong = self._luongCoBan + self.__soSanPham * 18_000
            self._luongHT = luong
            return luong
        else:
            return 0
class CongTy:
    def __init__(self, server, database, username='ASUS', password=None):
        # Kết nối đến SQL Server
        self.ket_noi = KetNoi(server, database, username, password)
        self.ds = []
    def loadNV(self):
        try:
            query = """
                SELECT NhanVien.MaNhanVien, HoTen, LuongCoBan, SoNgayLam, SoSanPham
                FROM NhanVien
                LEFT JOIN ChamCongTongHop ON NhanVien.MaNhanVien = ChamCongTongHop.MaNhanVien
            """
            result = self.ket_noi.execute_query(query).fetchall()

            self.ds = []
            for row in result:
                maNV, hoTen, luongCoBan, soNgayLam, soSanPham = row
                if soNgayLam is not None:
                    nv = NVVanPhong(maNV, hoTen, luongCoBan, soNgayLam)
                elif soSanPham is not None:
                    nv = NVSanXuat(maNV, hoTen, luongCoBan, soSanPham)
                else:
                    nv = NhanVien(maNV, hoTen, luongCoBan)
                self.ds.append(nv)

            print("Load employees data successfully.")
        except Exception as e:
            print(f"Error loading employees data: {e}")



    def tinhluongHT(self):
        try:
            for nv in self.ds:
                nv.tinhluongHT()

            print("Calculate salaries successfully.")

        except Exception as e:
            print(f"Error calculating salaries: {e}")

    def themNhanVien(self, maNV, hoTen, luongCoBan, loaiNV, soNL=None, soSP=None):
        try:
            if loaiNV == 'NhanVienVanPhong':
                nv = NVVanPhong(maNV, hoTen, luongCoBan, soNL)
            elif loaiNV == 'NhanVienSanXuat':
                nv = NVSanXuat(maNV, hoTen, luongCoBan, soSP)
            else:
                nv = NhanVien(maNV, hoTen, luongCoBan)

            self.ds.append(nv)

            # queryadd = """
            # INSERT INTO NhanVien
            # VALUES(MaNhanVien= ,HoTen= ,LuongCoBan= ,SoNgayLam= ,SoSanPham= )
            # """

            print(f"Thêm nhân viên {maNV} thành công.")
        except Exception as e:
            print(f"Lỗi khi thêm nhân viên {maNV}: {e}")

    def themCotLuongHangThang(self):
        try:
            # Thêm cột LuongHangThang vào bảng NhanVien
            add_column_query = """
                ALTER TABLE NhanVien
                ADD LuongHangThang DECIMAL(10, 2)
            """
            self.ket_noi.execute_query(add_column_query)
            self.ket_noi.commit()
            print("Column 'LuongHangThang' Thêm thành công.")

        except Exception as e:
            print(f"Error adding column 'LuongHangThang': {e}")

    def capNhatLuongHangThang(self):
        try:
            # Cập nhật giá trị của cột LuongHangThang
            for nv in self.ds:
                maNV = nv._maNV
                luong = nv._luongHT

                update_query = f"""
                    UPDATE NhanVien
                    SET LuongHangThang = {luong}
                    WHERE MaNhanVien = '{maNV}'
                """
                self.ket_noi.execute_query(update_query)
                self.ket_noi.commit()

            print("Update 'LuongHangThang' successfully.")

        except Exception as e:
            print(f"Error updating 'LuongHangThang': {e}")

    def print(self):
        """In toàn bộ DS"""
        for nv in self.ds:
            print(nv)

# Kết nối đến SQL Server
server = 'DUCKHEE\\SQLEXPRESS'
database = 'qlnv'

# Tạo đối tượng CongTy và thực hiện các bước
ct = CongTy(server, database)
ct.loadNV()
ct.tinhluongHT()
ct.themCotLuongHangThang()
ct.capNhatLuongHangThang()
ct.print()
