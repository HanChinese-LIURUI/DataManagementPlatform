import sys
import pymongo
import threading
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont, QBrush
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QApplication, QTableWidget, QHeaderView,
                             QGridLayout, QTableWidgetItem, QLineEdit,
                             QFileDialog, QCheckBox, QMessageBox, QMenu, QInputDialog)


class Windows(object):
    def __init__(self):
        super().__init__()

    def Test(self, win):
        win.setWindowTitle("数据分析")  # 设定窗口名字
        win.setWindowIcon(QIcon("Icon/Main.ico"))  # 指定图标
        win.setWindowOpacity(0.9)  # 透明度
        palette = QPalette()  # 设置背景颜色
        palette.setColor(QPalette.Background, Qt.black)  # 颜色设置
        win.setPalette(palette)  # 主窗口设置颜色为white
        desktop = QApplication.desktop()  # 获取显示器分辨率大小
        screenRect = desktop.screenGeometry()
        height = screenRect.height()
        width = screenRect.width()
        win.setMinimumSize(QSize(int(width / 2), int(height / 2)))
        win.setMaximumSize(QSize(int(width / 2), int(height / 2)))
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("Icon/timg.jpg")))
        # palette.setColor(QPalette.Background,Qt.red)
        win.setPalette(palette)
        win.show()  # 启动最大化


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    # w = Windows()
    # w.Test(win)
    Windows.Test(,win)
    sys.exit(app.exec_())
