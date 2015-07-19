__author__ = 'jean'

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QToolTip, QPushButton, QMessageBox, QDesktopWidget,\
    qApp, QHBoxLayout, QVBoxLayout, QMenuBar, QStatusBar, QToolBar
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class PhotosUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget.')
        quitBtn = QPushButton('Quit', self)
        #quitBtn.clicked.connect(self.quitBtnEvent())
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        quitBtn.setToolTip('This is a <b>QPushButton</b> widget.')
        quitBtn.resize(quitBtn.sizeHint())

        exitAction = QAction(QIcon(None), '&Exit', self)
        exitAction.setShortcut('Alt+F4')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        menuBar = QMenuBar(self)
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.resize(fileMenu.sizeHint())

        toolBar = QToolBar(self)
        toolBar.addAction(exitAction)
        #toolBar.resize(toolBar.sizeHint())
        toolBar.setAttribute()
        toolBar.setFixedHeight(50)

        statusBar = QStatusBar(self)
        statusBar.showMessage('Ready')

        vbox = QVBoxLayout()
        vbox.addWidget(toolBar)
        vbox.addStretch(1)
        vbox.addWidget(statusBar)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Photos')
        self.setWindowIcon(QIcon('camera_32.png'))
        self.center()
        self.show()

    def quitBtnEvent(self):
        reply = QMessageBox.question(self, 'Quit?', 'Are you sure to quit?',
                                     QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit
        else:
            return

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit?', 'Are you sure to quit?',
                                     QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = PhotosUI()
    sys.exit(app.exec_())