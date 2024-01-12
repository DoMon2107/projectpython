from duchuy.connect import Connect
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
class CongTyModel:
    def __init__(self, server, database, username=None, password=None):
        # Kết nối đến SQL Server
        self.ket_noi = Connect(server, database, username, password)
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

    def kiemTraTonTaiMaNhanVien(self, ma_nv):
        query = "SELECT COUNT(*) FROM NhanVien WHERE MaNhanVien = ?"
        result = self.ket_noi.insert_(query, (ma_nv,))

        # Kiểm tra xem result có giá trị hay không trước khi sử dụng
        if result and result[0] > 0:
            return True
        else:
            return False

    def themNhanVien(self, ma_nv, ho_ten, luong_co_ban, loai_nv, so_ngay_lam=0, so_san_pham=0):
        try:
            count_result = self.ket_noi.insert_("SELECT COUNT(*) FROM NhanVien WHERE MaNhanVien = ?", (ma_nv,))

            if count_result and count_result.fetchone()[0] > 0:
                print(f"Mã nhân viên {ma_nv} đã tồn tại. Không thể thêm.")
                return

            # Thêm vào bảng NhanVien
            query_nhan_vien = "INSERT INTO NhanVien (MaNhanVien, HoTen, LuongCoBan) VALUES (?, ?, ?)"
            self.ket_noi.insert_(query_nhan_vien, (ma_nv, ho_ten, luong_co_ban))

            # Thêm vào bảng ChamCongTongHop
            query_cham_cong = "INSERT INTO ChamCongTongHop (MaNhanVien, LoaiNhanVien, SoNgayLam, SoSanPham) VALUES (?, ?, ?, ?)"
            self.ket_noi.insert_(query_cham_cong, (ma_nv, loai_nv, so_ngay_lam, so_san_pham))

            # Cập nhật xuống cơ sở dữ liệu
            self.ket_noi.commit()

            print(f"Thêm nhân viên {ma_nv} thành công.")
        except Exception as e:
            print(f"Lỗi khi thêm nhân viên {ma_nv}: {e}")

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


server = 'DUCKHEE\\SQLEXPRESS'
database = 'qlnv'
ct = CongTyModel(server, database)
ct.loadNV()
ct.tinhluongHT()
ct.themCotLuongHangThang()
ct.capNhatLuongHangThang()
ct.print()

