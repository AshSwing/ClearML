import re

import numpy as np
import pandas as pd

from ..base import SupervisedLearning

class KNearestNeighbor(SupervisedLearning):
    """K近邻模型
    k: 近邻数量
    distance_function: Ln or function
    decision_function: voting, mean or function
    """

    def __init__(self, k, distance_function='L2', decision_function='voting'):
        pass

    def fit(self, X_train, y_train, X_valid=None, y_valid=None):
        """模型训练
        构造KD树
        """
        pass

    def predict(self, X, y_true):
        """模型预测
        搜索KD树
        """
        pass