import numpy as np
import pandas as pd
from scipy.stats import f_oneway

# Dữ liệu
data = {
    'Nhóm 1': [3.52, 3.36, 3.57, 4.19, 3.88, 3.76, 3.94],
    'Nhóm 2': [3.47, 3.73, 3.38, 3.87, 3.69, 3.51, 3.35, 3.64],
    'Nhóm 3': [3.54, 3.52, 3.61, 3.76, 3.65, 3.51],
    'Nhóm 4': [3.74, 3.83, 3.87, 4.08, 4.31, 3.98, 3.86, 3.71]
}

# Chuyển đổi dữ liệu thành DataFrame
df = pd.DataFrame(data)

# Kiểm định ANOVA
f_stat, p_value = f_oneway(df['Nhóm 1'], df['Nhóm 2'], df['Nhóm 3'], df['Nhóm 4'])

# In kết quả
print(f'Giá trị F: {f_stat}')
print(f'Giá trị p: {p_value}')

# Kết luận
alpha = 0.05
if p_value < alpha:
    print('Có bằng chứng để bác bỏ giả định về sự đồng nhất về phương sai giữa các nhóm.')
else:
    print('Không có bằng chứng để bác bỏ giả định về sự đồng nhất về phương sai giữa các nhóm.')
