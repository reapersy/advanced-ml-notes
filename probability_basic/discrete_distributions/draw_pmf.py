from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


def bernoulli_pmf(p=0.0):
    """
    伯努利分布，只有一个参数
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bernoulli.html#scipy.stats.bernoulli
    :param p: 试验成功的概率，或结果为1的概率
    :return:
    """
 