from PyQt5.QtWidgets import QDialog, QPushButton, QTextEdit, QLabel
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from winPyFiles.query import returnQuery, mySpeak, takeCommand
from winPyFiles.ChatOwnData import queryData, query


class yourDataUI(QDialog):
    def __init__(self, S_widgets):
        super(yourDataUI, self).__init__()
        loadUi('uiFiles/yourDataWin.ui', self)

        self.S_widgets = S_widgets
        self.chromeVs = None
        self.chain = None

        self.ChatView = self.findChild(QListWidget, 'listWidget')
        self.ChatEnter = self.findChild(QTextEdit, 'textEdit')
        self.enterButton = self.findChild(QPushButton, 'enterButton')
        self.saveButton = self.findChild(QPushButton, 'saveButton')
        self.voiceButton = self.findChild(QPushButton, 'voiceButton')
        self.clearButton = self.findChild(QPushButton, 'clearButton')
        self.pushBack = self.findChild(QPushButton, 'pushBack')
        self.pushUpload = self.findChild(QPushButton, 'pushUpload')
        self.label = self.findChild(QLabel, 'label')
        self.voiceButton.check = True

        self.label.setText('Press Button --> `Upload file to Chat`. To chat with your data')
        self.enterButton.pressed.connect(self.enterButtonPressed)
        self.enterButton.released.connect(self.enterButtonReleased)
        self.saveButton.clicked.connect(self.saveFile)
        # asynch function
        self.voiceButton.pressed.connect(self.voiceButtonPressed, Qt.QueuedConnection)
        self.voiceButton.released.connect(self.voiceButtonReleased)
        self.clearButton.clicked.connect(self.ChatView.clear)
        self.pushBack.clicked.connect(self.winChg)
        self.pushUpload.clicked.connect(self.initiate_fileuload)

    def initiate_fileuload(self):
        self.ChatView.clear()
        self.chromeVs, self.chain = None, None
        fltr = 'PDF files(*.pdf);;Text files (*.txt)'
        fileName, _ = QFileDialog.getOpenFileName(caption='Open File', filter=fltr)
        self.S_widgets.setWindowTitle(f'RePaLK - {fileName.split(sep="/")[-1].capitalize()}')
        self.chromeVs, self.chain = queryData(fileName)
        self.label.setText(
            f'{fileName.split(sep="/")[-1].capitalize()} uploaded. Now Chat with your uploaded file Data.')
        mySpeak(f'{fileName.split(sep="/")[-1].capitalize()} uploaded. Now Chat with your uploaded file Data.')

    def winChg(self):
        self.ChatView.clear()
        self.chromeVs, self.chain = None, None
        self.label.setText('Press Button -> <<Upload file to Chat>>. To chat with your data')
        self.S_widgets.setCurrentIndex(1)
        self.S_widgets.setWindowTitle('RePaLK - Main Window')

    def enterButtonPressed(self):
        query = self.ChatEnter.toPlainText()
        if len(query) > 0:
            query = QListWidgetItem(f'User: {query}')
            self.ChatView.addItem(query)
            self.ChatView.setCurrentItem(query)
            self.ChatEnter.setPlainText('')

    def enterButtonReleased(self):
        if self.chromeVs is not None:
            if self.ChatView.currentItem() is not None:
                qur = str(self.ChatView.currentItem().text())
                res, pageNumber = query(vectorDb=self.chromeVs, prompt_chain=self.chain, q=qur)
                res = QListWidgetItem(f'Ai Response: {res} \nOn Page Number: {pageNumber}')
                self.ChatView.addItem(res)
                self.ChatView.setCurrentItem(None)
            else:
                res = 'No Input given by user. Ask me Anything to get response'
                resItem = QListWidgetItem(res)
                self.ChatView.addItem(resItem)
                mySpeak(res)
        else:
            res = 'No File found. Press <<Upload file to Chat or Ctrl+U>> button to Interact '
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
                res, pageNumber = query(vectorDb=self.chromeVs, prompt_chain=self.chain, q=qur)
                res = QListWidgetItem(f'Ai Response: {res} \nOn Page Number: {pageNumber}')
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
