import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


norm_dis = stats.norm(5, 3) # 利用相应的分布函数及参数，创建一个冻结的正态分布(frozen distribution)
x = np.linspace(-5, 15, 101)  # 在