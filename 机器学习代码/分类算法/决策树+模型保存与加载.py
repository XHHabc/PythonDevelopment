from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import joblib


def decision_iris():
    """
    用决策树对鸢尾花进行分类
    :return:
    """
    # 1、获取数据集
    iris = load_iris()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
    # 3、决策树预估器
    estimator = DecisionTreeClassifier(criterion="entropy")
    estimator.fit(x_train, y_train)

    # 保存训练完结束的模型
    joblib.dump(estimator, "决策树test.pkl")

    # 加载模型文件（加载模型文件则前三步骤不用）
    # estimator= joblib.load("决策树test.pkl")

    # 4、模型评估
    # 方法一：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)

    # 方法二：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率：", score)

    # 5、可视化决策树
    export_graphviz(estimator, out_file="鸢尾花_决策树.dot", feature_names=iris.feature_names)
    return None


decision_iris()
