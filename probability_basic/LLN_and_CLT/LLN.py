import random
import matplotlib.pyplot as plt


def flip_plot(min_exp, max_exp):
    """
    Assumes min_exp and min_exp positive integers; min_exp < max_exp
    Plots results of 2**min_exp to 2**max_exp coin flips
    抛硬币的次数为2的min_exp次方到2的max_exp次方
    一共进行了 2**max_exp - 2**min_exp 轮实验，每轮实验抛硬币次数逐渐增加
    """

    ratios = []
    x_axis = []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for numFlips in x_axis:
        num_heads