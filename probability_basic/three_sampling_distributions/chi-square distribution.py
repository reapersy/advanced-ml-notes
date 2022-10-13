import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def chi2_distribution(df=1):
    """
    卡方分布，在实际的定义中只有一个参数df，即定义中的n
    :param df: 自由度，也就是该分布中独立变量的个数
    :return:
    """

    fig, ax = plt.subplots(1, 1)

    # 直接传入参数, Display the probability density function (pdf)
    x = np.linspace(stats.chi2.ppf(0.001, df),
                    stats.chi2.ppf(0.999, df), 200)
    ax.plot(x, stats.chi2.pdf(x, df), 'r-',
            lw=5, alpha=0.6, label=r'$\chi^2$ pdf')

    # 从冻结的均匀分布取值, Freeze the distribution and display the frozen pdf
    chi2_dis = stats.chi2(df=df)
    ax.plot(x, chi2_dis.pdf(x), 'k-',
            lw=2, label='frozen pdf')

    # 计算ppf分别等于0.001, 0.5, 0.999时的x值
    vals = chi2_dis.ppf([0.001, 0.5, 0.999])
    print(vals)  # [ 2.004  4.     5.996]

    # Check accuracy of cdf and ppf
    print(np.allclose([0.001, 0.5, 0.999], chi2_dis.cdf(vals)))  # Ture

    # Generate random numbers
    r = chi2_dis.rvs(size=10000)
    ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
    plt.ylabel('Probability')
    plt.title(r'PDF of $\chi