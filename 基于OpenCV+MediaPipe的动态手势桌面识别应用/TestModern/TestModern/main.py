import os
import sys

from PySide6.QtWidgets import QMessageBox

from modules import *
from modules import Settings

from modules.hands.hands_operate import GesturePage
import re
from modules.database import Database
from qt_material import apply_stylesheet
import tkinter as tk

from modules.manage_pages import ManagePages

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None


class MainWindow(QMainWindow):
    def __init__(self, username=None, sheet=None):
        QMainWindow.__init__(self)

        # 设置全局widgets
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # main窗口的用户信息
        self.username = username
        self.sheet = sheet
        self.lineData = None
        self.db = Database('localhost', 3306, 'root', '123456', 'handsData')
        if username:
            self.ui.label_nameshow.setText(self.username)
            if sheet == 1:
                self.lineData = self.db.select_data('user', condition=f"username='{username}'")
            else:
                self.lineData = self.db.select_data('adaccount', condition=f"username='{username}'")

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # 应用名字
        self.setWindowTitle("手势识别")

        # 切换菜单
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # 设置UI定义
        UIFunctions.uiDefinitions(self)

        # 按钮的点击事件
        # ///////////////////////////////////////////////////////////////
        # 左侧菜单的点击事件====================================================
        widgets.btn_home.clicked.connect(self.buttonClick)

        # 个人信息页面逻辑===================================================
        widgets.btn_user.clicked.connect(self.buttonClick)
        self.ui.btn_save_user.clicked.connect(lambda: AppFunctions.btnSaveUser(self, self.username))
        self.ui.lineEdit_username.setText(self.username)
        if username:
            self.ui.lineEdit_phone.setText(self.lineData[0][3])
            self.ui.lineEdit_email.setText(self.lineData[0][4])

        # 修改密码页面逻辑===================================================
        widgets.btn_re_password.clicked.connect(self.buttonClick)
        self.ui.re_save.clicked.connect(lambda: AppFunctions.btnRepassword(self, self.username))
        self.ui.lineEdit_re_username.setText(self.username)

        # 手势画面页面逻辑=================================================
        widgets.btn_new.clicked.connect(self.buttonClick)
        # 为了将八个comboBox传入手势类中能识别
        controls = {
            'comboBox_101': self.ui.comboBox_101,
            'comboBox_102': self.ui.comboBox_102,
            'comboBox_201': self.ui.comboBox_201,
            'comboBox_202': self.ui.comboBox_202,
            'comboBox_301': self.ui.comboBox_301,
            'comboBox_302': self.ui.comboBox_302,
            'comboBox_401': self.ui.comboBox_401,
            'comboBox_402': self.ui.comboBox_402
        }

        self.new_page = GesturePage(controls)
        self.new_page.setObjectName("new_page")
        self.ui.stackedWidget.addWidget(self.new_page)

        # 设置页面逻辑======================================================
        widgets.btn_new_2.clicked.connect(self.buttonClick)
        self.ui.pushButton_default.clicked.connect(lambda: AppFunctions.btnDefault(self.ui, sheet='operate_default'))
        self.ui.pushButton_saveSet.clicked.connect(lambda: AppFunctions.btnSave(self.ui))
        # 如果没有值，则初始化各combox的值为历史保存的点值
        if self.ui.comboBox_101.currentText():
            AppFunctions.btnDefault(self.ui, sheet='operate')

        # 右边设置按钮区域==============================================
        # 切换皮肤功能
        widgets.btn_message.clicked.connect(self.buttonClick)
        # 帮助与反馈
        widgets.btn_help_feedback.clicked.connect(self.buttonClick)
        self.ui.btn_save_feedback.clicked.connect(lambda: AppFunctions.btnSaveFeedback(self, self.username))
        # 关于我们
        widgets.btn_we.clicked.connect(self.buttonClick)
        # 管理员页面
        widgets.btn_administrators.clicked.connect(self.buttonClick)
        self.administrators_page = ManagePages()
        self.administrators_page.setObjectName("administrators_page")
        self.ui.stackedWidget.addWidget(self.administrators_page)
        # 设置退出回登录页面逻辑
        widgets.btn_logout.clicked.connect(lambda: self.return_login_window())

        # 左列表框
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # 右边左列表框
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)


        # 设置自定义主题====================================================================
        # 锁定好路径，防止在打包成exe后路径错乱
        if getattr(sys, 'frozen', False):
            absPath = os.path.dirname(os.path.abspath(sys.executable))
        elif __file__:
            absPath = os.path.dirname(os.path.abspath(__file__))

        useCustomTheme = False  # 默认为黑色皮肤

        # 使其全局可用
        self.useCustomTheme = useCustomTheme
        self.absPath = absPath
        self.themeFile = "themes/py_dracula_light.qss"

        # 设置初始选择主页和对应按钮
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # 按钮点击后跳转的页面
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # 切换-home页面
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换-摄像头画面页面
        if btnName == "btn_new":
            self.ui.stackedWidget.setCurrentWidget(self.new_page)  # 切换至所需页面
            UIFunctions.resetStyle(self, btnName)  # 并重置其他按钮的样式
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # 选择的按钮附上样式

        # 切换-设置页面
        if btnName == "btn_new_2":
            widgets.stackedWidget.setCurrentWidget(widgets.set_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换-个人信息设置页面
        if btnName == "btn_user":
            widgets.stackedWidget.setCurrentWidget(widgets.user_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换-密码修改页面
        if btnName == "btn_re_password":
            widgets.stackedWidget.setCurrentWidget(widgets.re_password_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换-帮助与反馈页面
        if btnName == "btn_help_feedback":
            widgets.stackedWidget.setCurrentWidget(widgets.help_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换-关于我们页面
        if btnName == "btn_we":
            widgets.stackedWidget.setCurrentWidget(widgets.we_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换-管理员页面页面
        if btnName == "btn_administrators":
            datalen = len(self.lineData[0])
            if datalen != 8:
                QMessageBox.warning(self, "提醒", "非管理员无法使用该功能")
                return
            else:
                userLevel = int(self.lineData[0][6])
                if userLevel != 1:
                    QMessageBox.warning(self, "提醒", "该账号权限不足")
                    return
            QMessageBox.warning(self, "提醒", "成功进入")
            self.ui.stackedWidget.setCurrentWidget(self.administrators_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换皮肤功能逻辑
        if btnName == "btn_message":
            if self.useCustomTheme:
                self.themeFile = os.path.abspath(os.path.join(self.absPath, "themes/py_dracula_dark.qss"))
                UIFunctions.theme(self, self.themeFile, True)

                self.useCustomTheme = False
            else:
                self.themeFile = os.path.abspath(os.path.join(self.absPath, "themes/py_dracula_light.qss"))
                UIFunctions.theme(self, self.themeFile, True)

                self.useCustomTheme = True

    # 窗口大小调整事件
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)  # 更新窗口大小调整

    # 鼠标的点击事件
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()  # 返回当前鼠标事件发生时的全局坐标
        # 加个鼠标点击反馈
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


    # 返回登录页面方法
    def return_login_window(self):
        root = tk.Tk()
        screen_width = int((root.winfo_screenwidth() - 400) / 2)
        screen_height = int((root.winfo_screenheight() - 200) / 2) - 200

        self.login_window = LoginWindow()
        apply_stylesheet(self.login_window, theme='dark_cyan.xml')
        self.login_window.setGeometry(screen_width, screen_height, 400, 200)  # 设置注册窗口位置和大小与登录窗口相同
        self.login_window.show()
        self.close()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("登录")
        self.username_label = QLabel("用户名:".rjust(8, ' '))
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("color: white;")
        self.password_label = QLabel("密码:".rjust(8, ' '))
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("color: white;")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("登录")
        self.register_button = QPushButton("注册")

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)  # 设置左右留白

        form_layout = QFormLayout()
        form_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)  # 设置字段在宽度上相等

        form_layout.addRow(self.username_label, self.username_input)
        form_layout.addRow(self.password_label, self.password_input)
        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.register_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.show_register_window)

    def login(self):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')
        username = self.username_input.text()
        password = self.password_input.text()

        if username == '' or password == '':
            QMessageBox.warning(self, "错误", "用户名或密码不能为空")
            return
        if username:
            result = db.select_data('user', condition=f"username='{username}'")
            result02 = db.select_data('adaccount', condition=f"username='{username}'")
            relen = len(result)+len(result02)
            # print(result)
            if relen == 0:
                QMessageBox.warning(self, "错误", "用户名或密码有误")
                return
            else:
                if len(result) != 0:
                    if password != result[0][2]:
                        QMessageBox.warning(self, "错误", "用户名或密码有误")
                        return
                    sheet = 1
                elif len(result02) != 0:
                    if password != result02[0][2]:
                        QMessageBox.warning(self, "错误", "用户名或密码有误")
                        return
                    sheet = 2
        QMessageBox.warning(self, "登录成功", "登录成功")
        self.show_main_window(username, sheet)

    def show_register_window(self):
        self.register_window = RegisterWindow()
        apply_stylesheet(self.register_window, theme='dark_cyan.xml')
        self.register_window.setGeometry(self.geometry())  # 设置注册窗口位置和大小与登录窗口相同
        self.register_window.show()
        self.close()

    def show_main_window(self, username, sheet):
        self.main_window = MainWindow(username, sheet)
        self.main_window.show()
        self.close()


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("注册")
        self.username_label = QLabel("用户名:".rjust(8, ' '))
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("color: white;")
        self.password_label = QLabel("密码:".rjust(8, ' '))
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("color: white;")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_label = QLabel("确认密码:".rjust(8, ' '))
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setStyleSheet("color: white;")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.phone_label = QLabel("手机号:".rjust(8, ' '))
        self.phone_input = QLineEdit()
        self.phone_input.setStyleSheet("color: white;")
        self.email_label = QLabel("邮箱:".rjust(8, ' '))
        self.email_input = QLineEdit()
        self.email_input.setStyleSheet("color: white;")
        self.register_button = QPushButton("注册")
        self.login_button = QPushButton("返回登录")

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)  # 设置左右留白

        form_layout = QFormLayout()
        form_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)  # 设置字段在宽度上相等

        form_layout.addRow(self.username_label, self.username_input)
        form_layout.addRow(self.password_label, self.password_input)
        form_layout.addRow(self.confirm_password_label, self.confirm_password_input)
        form_layout.addRow(self.phone_label, self.phone_input)
        form_layout.addRow(self.email_label, self.email_input)
        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.register_button)
        button_layout.addWidget(self.login_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.register_button.clicked.connect(self.register)
        self.login_button.clicked.connect(lambda: self.show_login_window())

    def register(self):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()

        if username == '' or password == '' or phone == '' or email == '':
            QMessageBox.warning(self, "错误", "不能有空缺")
            return
        if self.userName_check(username):
            QMessageBox.warning(self, "错误", "用户名已存在")
            return
        if len(username) <= 5:
            QMessageBox.warning(self, "错误", "用户名长度需大于6位")
            return
        if len(password) <= 5 or not(any(char.isdigit() for char in password)) or not(any(char.isalpha() for char in password)):
            # 通过遍历每个字符判断是否同时存在一个以上的字母和数字
            QMessageBox.warning(self, "错误", "密码长度需大于6位且包含数字和字母")
            return
        if password != confirm_password:
            QMessageBox.warning(self, "错误", "密码不一致")
            return
        if not self.isValidPhone(phone):
            QMessageBox.warning(self, "错误", "手机号格式有误")
            return
        if not self.isValidEmail(email):
            QMessageBox.warning(self, "错误", "邮箱格式有误")
            return
        data = [self.newData_id(), username, password, phone, email]
        db.insert_data('user', data)
        db.commit_changes()

        QMessageBox.warning(self, "完成", "注册成功，返回登录窗口。")
        self.show_login_window(username=username)

    # 验证手机号格式
    def isValidPhone(self, phone):
        # 使用正则表达式匹配手机号的格式
        pattern = r'^1[3456789]\d{9}$'
        if re.match(pattern, phone):
            return True
        else:
            return False

    # 验证邮箱格式
    def isValidEmail(self, email):
        # 使用正则表达式匹配邮箱的格式
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False

    # 给新数据赋予id值
    def newData_id(self):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')
        result = db.select_data('user', "MAX(id)")
        max_id = result[0][0]
        if max_id is None:
            return 1
        else:
            return max_id + 1

    # 查看用户名是否存在
    def userName_check(self, newNmae):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')
        result = db.select_data('user', condition=f"username='{newNmae}'")
        if len(result) != 0:
            return True

        result02 = db.select_data('adaccount', condition=f"username='{newNmae}'")
        if len(result02) != 0:
            return True

        return False

    def show_login_window(self, username=''):
        root = tk.Tk()
        screen_width = int((root.winfo_screenwidth() - 400) / 2)
        screen_height = int((root.winfo_screenheight() - 200) / 2) - 200

        self.login_window = LoginWindow()
        apply_stylesheet(self.login_window, theme='dark_cyan.xml')
        self.login_window.setGeometry(screen_width, screen_height, 400, 200)  # 设置注册窗口位置和大小与登录窗口相同
        self.login_window.username_input.setText(username)
        self.login_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 获取屏幕画面用于计算窗口出现位置
    root = tk.Tk()
    screen_width = int((root.winfo_screenwidth() - 400) / 2)
    screen_height = int((root.winfo_screenheight() - 200) / 2) - 200

    login_window = LoginWindow()
    login_window.setGeometry(screen_width, screen_height, 400, 200)  # 设置登录窗口位置和大小
    apply_stylesheet(login_window, theme='dark_cyan.xml')
    login_window.show()

    window = MainWindow()
    absIconFile = os.path.abspath(os.path.join(window.absPath, "images/images/PyDracula.png"))
    app.setWindowIcon(QIcon(absIconFile))

    sys.exit(app.exec_())
