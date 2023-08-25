import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def logisticregression():
    """
    逻辑回归进行癌症预测
    :return: None
    """
    # 1、读取数据，处理缺失值以及标准化
    column_name = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                   'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                   'Normal Nucleoli', 'Mitoses', 'Class']

    data = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
        names=column_name)

    # 删除缺失值
    data = data.replace(to_replace='?', value=np.nan)

    data = data.dropna()

    # 取出特征值
    x = data[column_name[1:10]]

    y = data[column_name[10]]

    # 分割数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # 进行标准化
    std = StandardScaler()

    x_train = std.fit_transform(x_train)

    x_test = std.transform(x_test)

    # 使用逻辑回归
    lr = LogisticRegression()

    lr.fit(x_train, y_train)

    print("得出来的权重：", lr.coef_)

    # 预测类别
    print("预测的类别：", lr.predict(x_test))

    # 得出准确率
    print("预测的准确率:", lr.score(x_test, y_test))

    print("精确率和召回率为：",
          classification_report(y_test, lr.predict(x_test), labels=[2, 4], target_names=['良性', '恶性']))

    # AUC指标
    # 0.5~1之间，越接近于1约好
    y_test = np.where(y_test > 2.5, 1, 0)
    print("AUC指标：", roc_auc_score(y_test, lr.predict(x_test)))

    return None


logisticregression()
