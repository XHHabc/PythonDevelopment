from sklearn.datasets import load_boston
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
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
    # 使用线性模型进行预测
    # 使用正规方程求解==============================================
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    y_lr_predict = std_y.inverse_transform(lr.predict(x_test))

    # 5、得出模型
    print("正规方程的权重参数为：", lr.coef_)
    print("正规方程预测的结果为：", y_lr_predict)
    # 6、模型评估
    print("正规方程的均方误差为：", mean_squared_error(y_test, y_lr_predict))

    # 梯度下降进行预测===============================================
    # SGD：随机梯度下降，是GD梯度下降得一个优化方法。（GD<SGD<SAD）
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)

    y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))

    # 5、得出模型
    print("SGD的权重参数为：", sgd.coef_)
    print("SGD的预测的结果为：", y_sgd_predict)
    # 6、模型评估
    print("SGD的均方误差为：", mean_squared_error(y_test, y_sgd_predict))

    return None


linear()
