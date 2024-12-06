from PySide6.QtWidgets import QMessageBox

from main import *
from modules import Settings
from .database import Database
import re

class AppFunctions(MainWindow):

    # 设置页面——按钮操作数据保存与读取数据库的方法
    def btnSave(self):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')

        db.update_data('operate', f"trigger_num1 = {self.comboBox_101.currentText()}", condition="id = 1")
        db.update_data('operate', f"trigger_num2 = {self.comboBox_102.currentText()}", condition="id = 1")

        db.update_data('operate', f"trigger_num1 = {self.comboBox_201.currentText()}", condition="id = 2")
        db.update_data('operate', f"trigger_num2 = {self.comboBox_202.currentText()}", condition="id = 2")

        db.update_data('operate', f"trigger_num1 = {self.comboBox_301.currentText()}", condition="id = 3")
        db.update_data('operate', f"trigger_num2 = {self.comboBox_302.currentText()}", condition="id = 3")

        db.update_data('operate', f"trigger_num1 = {self.comboBox_401.currentText()}", condition="id = 4")
        db.update_data('operate', f"trigger_num2 = {self.comboBox_402.currentText()}", condition="id = 4")
        db.commit_changes()

        new_portData = db.select_data('operate', condition="id IN (1,2,3,4)")
        print(new_portData)
        pass

    def btnDefault(self, sheet):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')
        portData = db.select_data(sheet, condition="id IN (1,2,3,4)")
        # 1、复制
        self.comboBox_101.setCurrentText(str(portData[0][2]))
        self.comboBox_102.setCurrentText(str(portData[0][3]))
        # 2、粘贴
        self.comboBox_201.setCurrentText(str(portData[1][2]))
        self.comboBox_202.setCurrentText(str(portData[1][3]))
        # 3、返回桌面
        self.comboBox_301.setCurrentText(str(portData[2][2]))
        self.comboBox_302.setCurrentText(str(portData[2][3]))
        # 4、截图
        self.comboBox_401.setCurrentText(str(portData[3][2]))
        self.comboBox_402.setCurrentText(str(portData[3][3]))
        print("已恢复默认设置")

    # 个人信息页保存
    def btnSaveUser(self, username):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')

        phone = self.ui.lineEdit_phone.text()
        email = self.ui.lineEdit_email.text()

        if phone == '' or email == '':
            QMessageBox.warning(self, "保存修改错误", "不能有空缺")
            return
        if not re.match(r'^1[3456789]\d{9}$', phone):
            QMessageBox.warning(self, "保存修改错误", "手机号格式有误")
            print('aaaaa')
            return
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            QMessageBox.warning(self, "保存修改错误", "邮箱格式有误")
            return
        db.update_data('user', f"phone = '{phone}'", condition=f"username ='{username}'")
        db.update_data('user', f"email = '{email}'", condition=f"username ='{username}'")
        db.commit_changes()
        QMessageBox.warning(self, "提醒", "保存成功")

    # 密码修改页保存
    def btnRepassword(self, username):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')

        oldPW = self.ui.lineEdit_re_oldpw.text()
        newPW = self.ui.lineEdit_re_newpw.text()
        aNewPW = self.ui.lineEdit_re_snewpw.text()
        if oldPW == '' or newPW == '':
            QMessageBox.warning(self, "错误", "不能有空")
            return
        if newPW != aNewPW:
            QMessageBox.warning(self, "错误", "新密码与确认密码不同")
            return
        result = db.select_data('user', condition=f'username={username}')
        if oldPW != result[0][2]:
            QMessageBox.warning(self, "错误", "密码有误")
            return
        db.update_data('user', f"password = '{newPW}'", condition=f"username ='{username}'")
        db.commit_changes()
        QMessageBox.warning(self, "提醒", "修改密码成功")

        self.ui.lineEdit_re_oldpw.setText('')
        self.ui.lineEdit_re_newpw.setText('')
        self.ui.lineEdit_re_snewpw.setText('')

    # 建议反馈页保存
    def btnSaveFeedback(self, username):
        db = Database('localhost', 3306, 'root', '123456', 'handsData')

        title = self.ui.lineEdit_title.text()
        content = self.ui.lineEdit_content.text()
        email = self.ui.lineEdit_call_email.text()

        # 编写id
        result = db.select_data('feedback', "MAX(id)")
        max_id = result[0][0]
        if max_id is None:
            max_id = 1
        else:
            max_id += 1

        if title == '' or content == '' or email == '':
            QMessageBox.warning(self, "提交修改错误", "不能有空缺")
            return
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            QMessageBox.warning(self, "提交修改错误", "邮箱格式有误")
            return

        data = [max_id, username, title, content, email]
        db.insert_data('feedback', data)
        db.commit_changes()

        QMessageBox.warning(self, "提醒", "提交成功")

        self.ui.lineEdit_title.setText('')
        self.ui.lineEdit_content.setText('')


    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")
