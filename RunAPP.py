from ViewcongTy import *
from ControllerCongty import *
from ModelCongTy import *

view = ViewCongTy()
model = CongTyModel()
controller = ControllerCongTy(view,model)

view.mainloop()