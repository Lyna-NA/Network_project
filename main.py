from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore, QtWidgets
from Ui_browserUI import Ui_Form
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *


class moWidget(QtWidgets.QWidget):
    def __init__(self):
        super(moWidget, self).__init__()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


class browserApp(moWidget, Ui_Form):
    def __init__(self):
        super(browserApp, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_2.clicked.connect(self.winShowMaximized)
        self.pushButton_3.clicked.connect(sys.exit)
        self.lineEdit.returnPressed.connect(self.load)
        self.pushButton_4.clicked.connect(self.backword)
        self.pushButton_5.clicked.connect(self.forward)
        self.pushButton_6.clicked.connect(self.reload)
        

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    def backword(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    

    def winShowMaximized(self):

        if self.pushButton_2.isChecked():

            self.widget.setStyleSheet(
                "QWidget#widget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));border:0px solid rgb(45,45,45);border-radius:0px;}")
            self.showMaximized()
        else:
            self.widget.setStyleSheet(
                "QWidget#widget{border:4px solid rgb(45,45,45);border-radius:20px;}")

            self.showNormal()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = browserApp()
    Form.show()
    sys.exit(app.exec_())
