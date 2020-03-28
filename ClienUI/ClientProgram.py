import sys
import pymongo
import threading

from ClienUI import ExtendedComboBox
from multiprocessing import shared_memory
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont, QBrush
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QApplication, QTableWidget, QHeaderView,
                             QGridLayout, QTableWidgetItem, QLineEdit,
                             QFileDialog, QCheckBox, QMessageBox, QMenu, QInputDialog)


# # noinspection PyArgumentList
# class A(object):
#     name = 12
#
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     @staticmethod  # 此装饰器是将类方法装饰为静态类，不能传入实例属性
#     def test(name: str):
#         print(name)
#
#     @classmethod  # 将类方法装饰为一个
#     def test1(cls, name: str):
#         print(cls.name)
#
#     @property  # 此装饰器是将类方法装饰为类属性
#     def test2(self):
#         return 0
#
#
# # noinspection PyArgumentList
# class B(A):
#     def __init__(self, name):
#         super(A).__init__()
#         self.name = name
#
#
# b = B('liuriu')
# print(b.test1('sdf'))
# noinspection PyArgumentList
class ClienLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.headline = None
        self.username = None
        self.usernameline = None
        self.password = None
        self.passwordline = None
        self.login = None
        self.grid = None
        self.InitUI()
        self.UIset()

    def InitUI(self):
        self.setWindowTitle("数据管理客户端")  # 设定窗口名字
        self.setWindowIcon(QIcon("Icon/Main.ico"))  # 指定图标
        self.setWindowOpacity(0.9)  # 透明度
        palette = QPalette()  # 设置背景颜色
        self.setPalette(palette)  # 主窗口设置颜色为white
        self.setPalette(palette)
        desktop = QApplication.desktop()  # 获取显示器分辨率大小
        screenrect = desktop.screenGeometry()
        height = screenrect.height()
        width = screenrect.width()
        self.setMinimumSize(QSize(int(width / 4), int(height / 4)))
        self.setMaximumSize(QSize(int(width / 4), int(height / 4)))

        self.show()  # 启动最大化

    def UIset(self):
        self.headline = QLabel('数据管理系统客户端')
        self.headline.setFont(QFont("宋体", 15, QFont.Bold))  # 设置字体
        self.username = QLabel('用户名')
        self.username.setFont(QFont("宋体", 10, QFont.Bold))  # 设置字体
        self.usernameline = ExtendedComboBox.ExtendedComboBox()  # 自定义的文本搜素框
        self.password = QLabel('密  码')
        self.password.setFont(QFont("宋体", 10, QFont.Bold))  # 设置字体
        self.passwordline = QLineEdit()  # 建立文本框
        self.login = QPushButton('登录')
        self.grid = QGridLayout()  # 创建了一个网格布局
        self.setLayout(self.grid)  # 设置窗口的布局界面
        self.grid.addWidget(self.headline, 0, 0, 1, 6, Qt.AlignCenter | Qt.AlignCenter)
        self.grid.addWidget(self.username, 1, 2, 1, 1, Qt.AlignCenter | Qt.AlignRight)
        self.grid.addWidget(self.usernameline, 1, 3, 1, 1)  # 这里不要限制位置，否则会导致文本框变短
        self.grid.addWidget(self.password, 2, 2, 1, 1, Qt.AlignCenter | Qt.AlignRight)
        self.grid.addWidget(self.passwordline, 2, 3, 1, 1, Qt.AlignCenter | Qt.AlignLeft)
        self.grid.addWidget(self.login, 3, 3, 1, 1, Qt.AlignCenter | Qt.AlignLeft)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ClienLogin()
    sys.exit(app.exec_())
