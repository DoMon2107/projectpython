from View import *
from Controller import *
from Model import *

server = 'DUCKHEE\\SQLEXPRESS'
database = 'qlnv'

view=ViewCongTy(server,database)
model=CongTyModel(server,database)
controller=ControllerCongTy(view,model,server,database)

view.mainloop()