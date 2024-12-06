import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QSizePolicy
from modules.database import Database

class ManagePages(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("测试")
        self.db = Database('localhost', 3306, 'root', '123456', 'handsData')
        self.lineData = self.db.select_data('user')
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', '用户名', '密码', '手机号', '邮箱'])
        self.update_table()

        # 创建按钮和文本框
        self.add_button = QPushButton("添加")
        self.delete_button = QPushButton("删除")
        self.update_button = QPushButton("修改")
        self.query_button = QPushButton("查找")
        self.refresh_button = QPushButton("刷新")
        self.id_text = QLineEdit()
        self.username_text = QLineEdit()
        self.password_text = QLineEdit()
        self.phone_text = QLineEdit()
        self.email_text = QLineEdit()

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("id:"))
        form_layout.addWidget(self.id_text)
        form_layout.addWidget(QLabel("用户名:"))
        form_layout.addWidget(self.username_text)
        form_layout.addWidget(QLabel("密码:"))
        form_layout.addWidget(self.password_text)
        form_layout.addWidget(QLabel("手机号:"))
        form_layout.addWidget(self.phone_text)
        form_layout.addWidget(QLabel("邮箱:"))
        form_layout.addWidget(self.email_text)
        layout.addLayout(form_layout)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.query_button)
        button_layout.addWidget(self.refresh_button)
        layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # 按钮绑定事件
        self.add_button.clicked.connect(self.add_data)
        self.update_button.clicked.connect(self.update_data)
        self.delete_button.clicked.connect(self.delete_data)
        self.query_button.clicked.connect(self.query_data)
        self.refresh_button.clicked.connect(self.update_table)

    def update_table(self, lineData = None):
        self.db = Database('localhost', 3306, 'root', '123456', 'handsData')
        if lineData:
            self.lineData = lineData
        else:
            self.lineData = self.db.select_data('user')
        self.tableWidget.setRowCount(len(self.lineData))
        for row, data in enumerate(self.lineData):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
                # if col == 0:  # 第一列设置为只读
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.tableWidget.setCurrentCell(-1, -1)  # 取消选择任何单元格，删除部分

    def add_data(self):
        id = self.id_text.text()
        username = self.username_text.text()
        password = self.password_text.text()
        phone = self.phone_text.text()
        email = self.email_text.text()

        if id != '':
            QMessageBox.warning(self, "错误", "id不可自定义")
            return
        if username == '' or password == '' or phone == '' or email == '':
            QMessageBox.warning(self, "错误", "除id栏，不能有空缺")
            return
        if self.userName_check(username):
            QMessageBox.warning(self, "错误", "用户名已存在")
            return
        if not self.isValidPhone(phone):
            QMessageBox.warning(self, "错误", "手机号格式有误")
            return
        if not self.isValidEmail(email):
            QMessageBox.warning(self, "错误", "邮箱格式有误")
            return

        self.db.insert_data('user', (self.newData_id(), username, password, phone, email))
        self.username_text.clear()
        self.password_text.clear()
        self.phone_text.clear()
        self.email_text.clear()

        QMessageBox.warning(self, "提示", "添加账户成功")
        self.db.commit_changes()
        self.update_table()

    def delete_data(self):
        selected_row = self.tableWidget.currentRow()
        print(selected_row)
        if selected_row >= 0:
            # 获取id
            data_id = self.lineData[selected_row][0]
            reply = QMessageBox.question(self, "确认删除", "是否确认删除？", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.db.delete_data('user', f"id={data_id}")
                self.db.commit_changes()
                QMessageBox.information(self, "提示", "删除成功")
                self.update_table()
        else:
            QMessageBox.warning(self, "警告", "请选择要删除的行")

    def update_data(self):
        selected_row = self.tableWidget.currentRow()
        print(selected_row)
        if selected_row >= 0:
            data_id = self.lineData[selected_row][0]

            id = self.id_text.text()
            username = self.username_text.text()
            password = self.password_text.text()
            phone = self.phone_text.text()
            email = self.email_text.text()

            # 检查每个字段的值是否非空，只修改有新值的列
            update_data = {}
            if id != '':
                QMessageBox.warning(self, "警告", "id不可修改")
                return
            if username:
                if self.userName_check(username):
                    QMessageBox.warning(self, "错误", "用户名已存在")
                    return
                update_data['username'] = username
            if password:
                update_data['password'] = password
            if phone:
                if not self.isValidPhone(phone):
                    QMessageBox.warning(self, "错误", "手机号格式有误")
                    return
                update_data['phone'] = phone
            if email:
                if not self.isValidEmail(email):
                    QMessageBox.warning(self, "错误", "邮箱格式有误")
                    return
                update_data['email'] = email

            set_values = ', '.join([f"{key} = '{value}'" for key, value in update_data.items()])

            print(data_id)
            print(set_values)

            # db文件中方法不适用，直接重写
            update_query = f"UPDATE user SET {set_values} WHERE id = {data_id}"
            self.db.cursor.execute(update_query)
            self.db.commit_changes()
            QMessageBox.warning(self, "提示", "修改成功")

            # self.username_text.clear()
            # self.password_text.clear()
            # self.phone_text.clear()
            # self.email_text.clear()
            self.update_table()
        else:
            QMessageBox.warning(self, "警告", "请选择要修改的行")

    def query_data(self):
        id = self.id_text.text()
        username = self.username_text.text()
        password = self.password_text.text()
        phone = self.phone_text.text()
        email = self.email_text.text()

        # 检查每个字段的值是否非空，只修改有新值的列
        select_data = {}
        if id:
            select_data['id'] = id
        if username:
            select_data['username'] = username
        if password:
            select_data['password'] = password
        if phone:
            select_data['phone'] = phone
        if email:
            select_data['email'] = email

        select_values = ' and '.join([f"{key} = '{value}'" for key, value in select_data.items()])
        print(select_values)
        print(self.db.select_data('user', condition=select_values))

        # db文件中方法不适用，直接重写
        # self.db.select_data('user', condition=select_values)
        # self.db.commit_changes()
        QMessageBox.warning(self, "提示", "查询完成")

        self.update_table(self.db.select_data('user', condition=select_values))

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
        return False

if __name__ == "__main__":
    app = QApplication([])
    window = ManagePages()
    window.show()
    app.exec()
