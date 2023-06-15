from PyQt5.QtWidgets import QDialog, QPushButton, QTextEdit
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from winPyFiles.query import returnQuery, mySpeak, takeCommand

class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()
        loadUi('uiFiles/mainWin.ui', self)

        self.ChatView = self.findChild(QListWidget, 'listWidget')
        self.ChatEnter = self.findChild(QTextEdit, 'textEdit')
        self.btn = self.findChild(QPushButton, 'pushButton')
        self.btn2 = self.findChild(QPushButton, 'pushButton2')
        self.btn3 = self.findChild(QPushButton, 'pushButton3')
        self.btn4 = self.findChild(QPushButton, 'pushButton3_2')
        self.btn3.check = True

        self.btn.pressed.connect(self.btnPressed)
        self.btn.released.connect(self.btnReleased)
        self.btn2.clicked.connect(self.saveFile)
        # self.btn3.pressed.connect(self.btn3Pressed)
        # asynch function
        self.btn3.pressed.connect(self.btn3Pressed, Qt.QueuedConnection)
        self.btn3.released.connect(self.btn3Released)
        self.btn4.clicked.connect(self.ChatView.clear)

    def btnPressed(self):
        query = self.ChatEnter.toPlainText()
        if len(query) > 0:
            query = QListWidgetItem(f'User: {query}')
            self.ChatView.addItem(query)
            self.ChatView.setCurrentItem(query)
            self.ChatEnter.setPlainText('')

    def btnReleased(self):
        if self.ChatView.currentItem() is not None:
            qur = str(self.ChatView.currentItem().text())
            res = returnQuery(qur)
            res = QListWidgetItem(f'Ai Response: {res}')
            self.ChatView.addItem(res)
            self.ChatView.setCurrentItem(None)
        else:
            res = 'No Input given by user. Ask me Anything to get response'
            resItem = QListWidgetItem(res)
            self.ChatView.addItem(resItem)
            mySpeak(res)

    def btn3Pressed(self):
        if self.btn3.check:
            query = takeCommand().lower()
            if len(query) > 0:
                query = QListWidgetItem(f'User: {query}')
                self.ChatView.addItem(query)
                self.ChatView.setCurrentItem(query)
                self.btn3.check = False

    def btn3Released(self):
        if not self.btn3.check:
            if self.ChatView.currentItem() is not None:
                self.ChatEnter.setText('')
                qur = str(self.ChatView.currentItem().text())
                res = returnQuery(qur)
                res = QListWidgetItem(f'Ai Response: {res}')
                self.ChatView.addItem(res)
                self.ChatView.setCurrentItem(None)
            else:
                res = 'No Input given by user. Ask me Anything to get response'
                resItem = QListWidgetItem(res)
                self.ChatView.addItem(resItem)
                mySpeak(res)
            self.btn3.check = True

    def saveFile(self):
        if len(self.ChatView.selectedItems()) > 0:
            selectedItem = self.ChatView.selectedItems()[0]
            fltr = 'Text files (*.txt);;XML files (*.xml);;py files(*.py);;Html files(*.html)'
            filename, _ = QFileDialog.getSaveFileName(self, "Save File", 'arnav.txt', fltr)
            if filename != "":
                with open(filename, 'w') as f:
                    f.write(selectedItem.text())
                mySpeak(f'Saved file at {filename}')
            else:
                res = 'File not saved as you cancelled saving'
                resItem = QListWidgetItem(res)
                resItem.setBackground(Qt.color0)
                self.ChatView.addItem(resItem)
                mySpeak(res)
        else:
            res = 'Selected content to save into a file'
            resItem = QListWidgetItem(res)
            resItem.setBackground(Qt.color0)
            self.ChatView.addItem(resItem)
            mySpeak(res)
