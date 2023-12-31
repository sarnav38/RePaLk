from PyQt5.QtWidgets import QDialog, QPushButton, QTextEdit
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from winPyFiles.query import returnQuery, mySpeak, takeCommand

class UI(QDialog):
    def __init__(self, S_widgets):
        super(UI, self).__init__()
        loadUi('uiFiles/mainWin.ui', self)
        self.S_widgets = S_widgets

        self.ChatView = self.findChild(QListWidget, 'listWidget')
        self.ChatEnter = self.findChild(QTextEdit, 'textEdit')
        self.enterButton = self.findChild(QPushButton, 'enterButton')
        self.saveButton = self.findChild(QPushButton, 'saveButton')
        self.voiceButton = self.findChild(QPushButton, 'voiceButton')
        self.clearButton = self.findChild(QPushButton, 'clearButton')
        self.goToChatDataWin = self.findChild(QPushButton, 'pushData')
        self.voiceButton.check = True

        self.enterButton.pressed.connect(self.enterButtonPressed)
        self.enterButton.released.connect(self.enterButtonReleased)
        self.saveButton.clicked.connect(self.saveFile)

        # asynch function
        self.voiceButton.pressed.connect(self.voiceButtonPressed, Qt.QueuedConnection)
        self.voiceButton.released.connect(self.voiceButtonReleased)
        self.clearButton.clicked.connect(self.ChatView.clear)
        self.goToChatDataWin.clicked.connect(self.winChg)

    def winChg(self):
        self.S_widgets.setCurrentIndex(2)
        self.S_widgets.setWindowTitle('RePaLK - Upload File to Chat')

    def enterButtonPressed(self):
        query = self.ChatEnter.toPlainText()
        if len(query) > 0:
            query = QListWidgetItem(f'User: {query}')
            self.ChatView.addItem(query)
            self.ChatView.setCurrentItem(query)
            self.ChatEnter.setPlainText('')

    def enterButtonReleased(self):
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

    def voiceButtonPressed(self):
        if self.voiceButton.check:
            query = takeCommand().lower()
            if len(query) > 0:
                query = QListWidgetItem(f'User: {query}')
                self.ChatView.addItem(query)
                self.ChatView.setCurrentItem(query)
                self.voiceButton.check = False

    def voiceButtonReleased(self):
        if not self.voiceButton.check:
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
            self.voiceButton.check = True

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
