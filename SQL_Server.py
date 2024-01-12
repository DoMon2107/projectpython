import pyodbc

class SQL:
    def __init__(self, drive='SQL Server', server='DUCKHEE\SQLEXPRESS', database='qlnv', username='', password=''):
        self.drive = 'SQL Server'
        self.server = 'DUCKHEE\SQLEXPRESS'
        self.database = 'BikeStores'
        self.username = 'ASUS'
        self.password = ''
    def connect(self):
        str_sql = 'DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}'.format(self.drive,
                                                                      self.server,
                                                                      self.database,
                                                                      self.username,
                                                                      self.password)
        self.cnxn = pyodbc.connect(str_sql)
        self.cursor = self.cnxn.cursor()

    def execute_query(self,query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row
    def execute_update(self, query):
        self.cursor.execute(query)
        self.cnxn.commit()

    def xoa_table(self,table_name):
        query = f"DROP TABLE {table_name}"
        self.cursor.execute(query)
        self.cnxn.commit()

    def tao_table(self, table_name, loainv):
        if loainv == "Văn Phòng":
            query = f'''
                CREATE TABLE {table_name} (
                    MaNV VARCHAR(50),
                    HoTen NVARCHAR(255),
                    LoaiNhanVien NVARCHAR(255),
                    LuongCoBan FLOAT,
                    SoNgayLam FLOAT,
                    LuongHT FLOAT
                    )
                 '''
            self.cursor.execute(query)
            self.cnxn.commit()
        if loainv == "Bán Hàng":
            query = f'''
                CREATE TABLE {table_name} (
                    MaNV VARCHAR(50),
                    HoTen NVARCHAR(255),
                    LoaiNhanVien NVARCHAR(255),
                    SoSanPham FLOAT,
                    LuongCoBan FLOAT,
                    LuongHT FLOAT
                    )
                '''
            self.cursor.execute(query)
            self.cnxn.commit()
        if loainv == "Không Loại":
            query = f'''
                CREATE TABLE {table_name} (
                    MaNV VARCHAR(50),
                    HoTen NVARCHAR(255),
                    LoaiNhanVien NVARCHAR(255),
                    LuongCoBan FLOAT,
                    LuongHT FLOAT
                    )
                '''
            self.cursor.execute(query)
            self.cnxn.commit()
    def them_data(self, table_name, data, loainv):
        if loainv == "Văn Phòng":
            query = f"INSERT INTO {table_name} (MaNV, HoTen, LoaiNhanVien, SoNgayLam, LuongCoBan, LuongHT) " \
                "VALUES (?, ?, ?, ? ,? ,?)"
            values = (data['MaNV'], data['HoTen'],data['LoaiNhanVien'], data['SoNgayLam'], data['LuongCoBan'], data['LuongHT'])
            self.cursor.execute(query,values)
            self.cnxn.commit()
        if loainv == "Bán Hàng":
            query = f"INSERT INTO {table_name} (MaNV, HoTen, LoaiNhanVien, SoSanPham, LuongCoBan, LuongHT) " \
                    "VALUES (?, ?, ?, ? ,? ,?)"
            values = (data['MaNV'], data['HoTen'], data['LoaiNhanVien'], data['SoSanPham'], data['LuongCoBan'], data['LuongHT'])
            self.cursor.execute(query, values)
            self.cnxn.commit()
        if loainv == "Không Loại":
            query = f"INSERT INTO {table_name} (MaNV, HoTen, LoaiNhanVien, LuongCoBan, LuongHT) " \
                    "VALUES (?, ?, ?, ?, ?)"
            values = (data['MaNV'], data['HoTen'], data['LoaiNhanVien'],data['LuongCoBan'], data['LuongHT'])
            self.cursor.execute(query, values)
            self.cnxn.commit()