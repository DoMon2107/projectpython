# connect voi SQL

from SQL_Server import SQL
from abc import ABC, abstractmethod

connect = SQL()

connect.connect()

class abcNhanVien(ABC):
    @abstractmethod
    def TinhluongHT(self):
        pass

class NhanVien(abcNhanVien):
    def __init__(self, Manv, HoTen, LuongCoBan, LoaiNhanVien, SoNgayLam, SoSanPham):
        self.Manv = Manv
        self.HoTen = HoTen
        self.LuongCoBan = LuongCoBan
        self.LoaiNhanVien = LoaiNhanVien
        self.SoNgayLam = SoNgayLam
        self.SoSanPham = SoSanPham
        self.LuongHT = 0  # Khởi tạo lương hàng tháng là 0
        self.DanhsachNV = {"Văn Phòng": [], "Bán Hàng": [], "Không Loại": []}
    def loadNV(self):
        query = ("SELECT ChamCongTongHop.MaNhanVien, HoTen, LuongCoBan, LoaiNhanVien, SoNgayLam, SoSanPham FROM NhanVien, ChamCongTongHop WHERE NhanVien.MaNhanVien = ChamCongTongHop.MaNhanVien")
        rows = connect.execute_query(query)
        for row in rows:
            self.Manv = row[0]
            self.HoTen = row[1]
            self.LuongCoBan = row[2]
            self.LoaiNhanVien = row[3]
            self.SoNgayLam = row[4]
            self.SoSanPham = row[5]
            self.TinhluongHT()

            loainv = self.LoaiNhanVien
            self.DanhsachNV[loainv].append({
                "MaNV": self.Manv,
                "HoTen": self.HoTen,
                "LuongCoBan": self.LuongCoBan,
                "SoNgayLam": self.SoNgayLam,
                "SoSanPham": self.SoSanPham,
                "LoaiNhanVien": self.LoaiNhanVien,
                "LuongHT": self.LuongHT
            })

            # show ra tung dong
            # print(f"MaNV: {self.Manv}, HoTen: {self.HoTen}, LuongCoBan: {self.LuongCoBan}, "
            #       f"LoaiNhanVien: {self.LoaiNhanVien}, SoNgayLam: {self.SoNgayLam}, SoSanPham: {self.SoSanPham}, LuongHT: {self.LuongHT}")
    def TinhluongHT(self):
        if self.LoaiNhanVien == 'Văn Phòng':
            self.LuongHT = self.LuongCoBan + self.SoNgayLam * 150_000

        elif self.LoaiNhanVien == 'Bán Hàng':
            self.LuongHT = self.LuongCoBan + self.SoSanPham * 18_000

    def xoa_table(self,table_name):
        query = f"DROP TABLE {table_name}"
        connect.execute_update(query)

    # tao bang theo loai nhan vien
    def tao_bang_theo_loai_nv(self, tenbang, loainv):
        self.tenbang = tenbang
        self.loainv = loainv
        connect.tao_table(self.tenbang, self.loainv)
        for nv in self.DanhsachNV[self.loainv]:
            connect.them_data(self.tenbang, nv, self.loainv)

nhanvienmoi = NhanVien(Manv='', HoTen='', LuongCoBan='', LoaiNhanVien='', SoNgayLam='', SoSanPham='')
nhanvienmoi.loadNV()
# nhanvienmoi.drop_table('NhanVienVanPhong')
nhanvienmoi.xoa_table("NhanVienVanPhong")
nhanvienmoi.tao_bang_theo_loai_nv("NhanVienVanPhong","Văn Phòng")
nhanvienmoi.xoa_table("NhanVienBanHang")
nhanvienmoi.tao_bang_theo_loai_nv("NhanVienBanHang","Bán Hàng")
nhanvienmoi.xoa_table("NhanVienBinhThuong")
nhanvienmoi.tao_bang_theo_loai_nv("NhanVienBinhThuong","Không Loại")

# nhanvienmoi.create_table()
# nhanvienmoi.update_SQL()

