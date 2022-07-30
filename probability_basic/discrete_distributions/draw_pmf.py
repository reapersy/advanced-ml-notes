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
    ber_dist = stats.bernoulli(p)
    x = [0, 1]
    x_name = ['0', '1']
    pmf = [ber_dist.pmf(x[0]), ber_dist.pmf(x[1])]
    plt.bar(x, pmf, width=0.15)
    plt.xticks(x, x_name)
    plt.ylabel('Probability')
    plt.title('PMF of bernoulli distribution')
    plt.show()

# bernoulli_pmf(p=0.3)


def binom_pmf(n=1, p=0.1):
    """
    二项分布有两个参数
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html#scipy.stats.binom
    :param n:试验次数
    :param p:单次实验成功的概率
    :return:
    """
    binom_dis = stats.binom(n, p)
    x = np.arange(binom_dis.p