# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from inference import start_infer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start_button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_button.setGeometry(QtCore.QRect(230, 280, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Start_button.setFont(font)
        self.Start_button.setObjectName("Start_button")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(130, 140, 391, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setScaledContents(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Input_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Input_box.setGeometry(QtCore.QRect(320, 230, 171, 31))
        self.Input_box.setPlainText("")
        self.Input_box.setObjectName("Input_box")
        self.Fall_icon = QtWidgets.QLabel(self.centralwidget)
        self.Fall_icon.setGeometry(QtCore.QRect(350, 50, 91, 111))
        self.Fall_icon.setText("")
        self.Fall_icon.setPixmap(QtGui.QPixmap("./media/fall_icon.png"))
        self.Fall_icon.setScaledContents(True)
        self.Fall_icon.setObjectName("Fall_icon")
        self.Camera_icon = QtWidgets.QLabel(self.centralwidget)
        self.Camera_icon.setGeometry(QtCore.QRect(190, 40, 121, 121))
        self.Camera_icon.setText("")
        self.Camera_icon.setPixmap(QtGui.QPixmap("./media/video_icon.png"))
        self.Camera_icon.setScaledContents(True)
        self.Camera_icon.setObjectName("Camera_icon")
        self.Input_note = QtWidgets.QLabel(self.centralwidget)
        self.Input_note.setGeometry(QtCore.QRect(160, 230, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Input_note.setFont(font)
        self.Input_note.setObjectName("Input_note")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # additional function
        self.Start_button.clicked.connect(self.start_btn_clicked)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start_button.setText(_translate("MainWindow", "Start Monitoring"))
        self.Title.setText(_translate("MainWindow", "Detect falls, save lives"))
        self.Input_note.setText(_translate("MainWindow", "Emergency Contact:"))

    def start_btn_clicked(self):
        phone_number = self.Input_box.toPlainText()
        start_infer(phone_number)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
