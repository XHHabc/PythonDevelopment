# PythonDevelopment

<h3>基于OpenCV+MediaPipe的动态手势桌面识别应用文件包含：</h3>

1、可以用pyinstaller打包成exe文件，直接运行。（建立好数据库信息后）

2、dump-handsdata.sql：项目所使用的各基础数据表代码。

3、TestModern.zip：完整项目文件。

​	3.1、项目UI：基于已有项目进行的二次开发，使用PySide6，利用Qt Designer进行可视化设计。

​	原UI设计作者：[Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6 (github.com)](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6)

​	3.2、数据库：使用MySQL为基础，用DBDBeaver进行管理与操作。

​	3.3、主要技术：使用MediaPipe库与OpenCV库。

<h4>手势操作说明：==============================================</h4>

模拟键盘：具体查看自定义表。
默认为
（蓝色）
复制			4+16
粘贴			4+13
（橙色）
返回桌面		4+20
截图			4+17

模拟鼠标：
左键双击		8+12
左键			4+8

右键			12+16

<h4>文件备注==============================================</h4>
手势操作：
	手势识别：hands_identify.py
	手势操作：hands_operate.py

数据库：database.py
管理员页面：manage_pages.py



<h4>功能补充说明==============================================</h4>

手势切换页面时摄像头开关：
在上面的代码中，我们添加了`hideEvent`方法来关闭摄像头。当页面隐藏时（切换到其他页面），它会停止定时器并释放摄像头资源。
这样，当你切换到其他页面时，`GesturePage`页面会自动关闭摄像头，以避免不必要的资源占用。当再次切换回`GesturePage`页面时，它会重新打开摄像头并开始处理图像。记得根据你的实际需求进行适当的调整。

主窗口控件传递给GesturePage类===============================================================
我们在`GesturePage`类的构造函数中添加了一个名为`controls`的参数，用于接收一个字典，其中包含了所有需要传递的控件。

然后，我们将整个字典存储在`self.controls`属性中，并根据控件的名称从字典中获取相应的控件对象。例如，`self.controls['comboBox_101']`表示主窗口中名为`comboBox_101`的控件对象。

最后，我们可以使用`self.controls['comboBox_101'].currentText()`和`self.controls['comboBox_102'].currentText()`来获取这些控件的当前文本值。

在主窗口中实例化`GesturePage`类时，需要将包含所有需要传递的控件的字典作为参数传递给`GesturePage`类。


控制粘贴功能频率==============================================================================
我们添加了一个名为 `last_paste_time` 的实例变量，用于跟踪上一次粘贴操作的时间。在 `test_hands` 方法中，我们获取当前时间，并计算与上一次粘贴操作的时间差 `time_diff`。如果时间差大于等于 5 秒（可以根据需要调整时间间隔），则调用 `fun_paste` 方法执行粘贴操作，并更新 `last_paste_time` 为当前时间。

通过这种方式，即使 `test_hands` 方法在循环中频繁执行，也可以通过限制时间间隔来避免过快地多次调用粘贴操作。







### 机器学习文件包含：  

1、K-近邻算法+网格搜索+交叉验证；  
2、决策树；  
3、朴素贝叶斯算法；  
4、逻辑回归算法+AUC指标；  
5、随机森林；  
6、线性回归算法+岭回归；  
7、特征提取+预处理+降维；  
8、聚类-k-means算法。  