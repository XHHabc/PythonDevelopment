from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


def knn_iris_gscv():
    """
    用knn算法会鸢尾花进行分类，添加网格搜索、交叉验证
    :return:
    """
    # 1、获取数据
    iris = load_iris()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 3、特征工程：标准化
    # transfer = StandardScaler()
    # x_train = transfer.fit_transform(x_train)
    # x_test = transfer.transform(x_test)

    # 4、
    # 随机森林去进行预测
    rf = RandomForestClassifier()

    param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}

    # 超参数调优
    gc = GridSearchCV(rf, param_grid=param, cv=2)

    gc.fit(x_train, y_train)

    print("随机森林预测的准确率为：", gc.score(x_test, y_test))



    return None


knn_iris_gscv()
