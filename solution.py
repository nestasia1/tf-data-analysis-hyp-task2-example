import pandas as pd
import numpy as np
import scipy

chat_id = 1022895883 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    statistic, p_value = scipy.stats.ks_2samp(x, y)

    return p_value < alpha
