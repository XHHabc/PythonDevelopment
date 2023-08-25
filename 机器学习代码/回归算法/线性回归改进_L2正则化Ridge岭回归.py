from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def linear():
    """
    线性回归预测房子价格

    线性回归的损失函数-均方误差
    线性回归的优化方法
        正规方程
        梯度下降
    线性回归的性能衡量方法-均方误差
    :return:
    """
    # 1、获取数据
    lb = load_boston()
    #
    # print(lb.data)
    # print(lb.target)

    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.3, random_state=24)

    # 3、标准化处理
    # 对于特征值处理
    std_x = StandardScaler()

    x_train = std_x.fit_transform(x_train)
    x_test = std_x.fit_transform(x_test)
    # print(x_train)

    # 对于目标值进行标准化
    std_y = StandardScaler()

    y_train = std_y.fit_transform(y_train)
    y_test = std_y.transform(y_test)
    y_test = std_y.inverse_transform(y_test)

    # 4、预估器
    # 岭回归使用SAD。（GD<SGD<SAD）
    rd = Ridge(alpha=1.0)
    rd.fit(x_train, y_train)


    # 5、得出模型
    print("岭回归的权重参数为：", rd.coef_)

    y_rd_predict = std_y.inverse_transform(rd.predict(x_test))
    print("岭回归的预测的结果为：", y_rd_predict)

    # 6、模型评估
    print("岭回归的均方误差为：", mean_squared_error(y_test, y_rd_predict))
    return None


linear()
