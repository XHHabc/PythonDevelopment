import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import silhouette_score


def variance_demo():
    """
    K-means算法-无监督学习-聚合
    :return: None
    """
    # 缺数据
    data = None
    print(data)

    km = KMeans(n_clusters=4)
    km.fit(data)
    pre = km.predict(data)
    print(pre)

    # Kmeans性能评估指标-轮廓系数
    print(silhouette_score(data, pre))

    return None


variance_demo()
