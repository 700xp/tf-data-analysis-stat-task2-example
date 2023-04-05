import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 689327667 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    stat = (x ** 2).sum()
    left_edge_chi_squared = chi2.ppf(1 - p, 2 * len(x) - 1)
    sigma_edge = np.sqrt(stat / (31 * left_edge_chi_squared))
    return (-sigma_edge, sigma_edge)
