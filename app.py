from winPyFiles.mainWindow import UI
from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class welComeWindow(QDialog):
    def __init__(self):
        super(welComeWindow, self).__init__()
        loadUi('uiFiles/welWind.ui', self)
        timer = QTimer()
        timer.setSingleShot(True)
        timer.singleShot(5000, self.winChg)

    @staticmethod
    def winChg():
        widgets.setCurrentIndex(widgets.currentIndex() + 1)


app = QApplication([sys.argv])
widgets = QStackedWidget()
welWindow = welComeWindow()
mainWindow = UI()
widgets.addWidget(welWindow)
widgets.addWidget(mainWindow)
widgets.setFixedWidth(800)
widgets.setFixedHeight(600)
widgets.show()
try:
    app.exec_()
except:
    ...
