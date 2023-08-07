from winPyFiles.mainWindow import UI
from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from winPyFiles.yourDatawin import yourDataUI

class welComeWindow(QDialog):
    def __init__(self):
        super(welComeWindow, self).__init__()
        loadUi('uiFiles/welWind.ui', self)
        timer = QTimer()
        timer.setSingleShot(True)
        # self.btn = self.findChild(QPushButton, 'pushButton')
        # self.btn.clicked.connect(self.winChg)
        timer.singleShot(5000, self.winChg)

    @staticmethod
    def winChg():
        S_widgets.setCurrentIndex(S_widgets.currentIndex() + 1)
        S_widgets.setWindowTitle('RePaLK Main Window')


app = QApplication(sys.argv)
S_widgets = QStackedWidget()
welWindow = welComeWindow()
mainWindow = UI(S_widgets)
yourDataWindow = yourDataUI(S_widgets)
S_widgets.addWidget(welWindow)
S_widgets.addWidget(mainWindow)
S_widgets.addWidget(yourDataWindow)
S_widgets.setFixedWidth(800)
S_widgets.setFixedHeight(600)
S_widgets.setWindowTitle('RePaLK')
S_widgets.show()
try:
    app.exec_()
except:
    exit()


