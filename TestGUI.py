__author__ = 'jean'

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QToolTip, QPushButton, QMessageBox, QDesktopWidget,\
    qApp, QHBoxLayout, QVBoxLayout, QGridLayout, QMenuBar, QStatusBar, QToolBar, QLabel, QFrame, QSizePolicy, \
    QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class PhotosUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget.')

        exitAction = QAction(QIcon('application-exit-4.png'), '&Exit', self)
        exitAction.setShortcut('Alt+F4')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        grid = QGridLayout()
        lbl_1 = QLabel('1,1')
        lbl_2 = QLabel('1,2')
        lbl_3 = QLabel('2,1')
        lbl_4 = QLabel('2,2')
        grid.addWidget(lbl_1, 1, 1)
        grid.addWidget(lbl_2, 1, 2)
        grid.addWidget(lbl_3, 2, 1)
        grid.addWidget(lbl_4, 2, 2)

        mainW = QWidget()
        mainW.setLayout(grid)

        self.setCentralWidget(mainW)
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Photos')
        self.setWindowIcon(QIcon('camera-photo-5.png'))
        self.center()
        self.show()

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