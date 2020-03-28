import os
import sys
from ClienUI.ClientProgram import ClienLogin
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clien = ClienLogin()
    sys.exit(app.exec_())
