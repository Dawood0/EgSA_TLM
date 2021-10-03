# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt


class Ui_Widget(QtWidgets.QWidget):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 451)
        self.textBrowser = QtWidgets.QTextBrowser(Widget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 150, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(470, 150, 256, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(-50, 40, 881, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Widget)
        self.line_2.setGeometry(QtCore.QRect(-10, 80, 881, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(290, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(Widget)
        self.line_3.setGeometry(QtCore.QRect(390, 50, 20, 571))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(180, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(470, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(580, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 370, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(550, 350, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Widget)
        self.label_7.setGeometry(QtCore.QRect(535, 390, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(1300, 10, 141, 41))
        self.pushButton.setObjectName("pushButton")

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)  # update every second
        self.showTime()

        self.pushButton.clicked.connect(lambda: self.send())
        self.cnt = 0

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "DRTF Subsystem"))
        self.label_2.setText(_translate("Widget", "Packet to send:"))
        self.label_3.setText(_translate("Widget", "Send"))
        self.label_4.setText(_translate("Widget", "Packet Recieved:"))
        self.label_5.setText(_translate("Widget", "Recieve"))
        self.pushButton.setText(_translate("Widget", "Send to SAT"))
        self.label_6.setText(_translate("Widget", "Sent to telemetry"))
        self.label_7.setText(_translate("Widget", "Sent to satallite control"))

    def showTime(self):
        currentTime = QTime.currentTime()

        displayTxt = currentTime.toString('hh:mm:ss')
        # print(displayTxt)
        self.pushButton.click()

    def send(self):
        import os
        import time
        newPath = os.path.join("\\".join(os.getcwd().split("\\")[:-2]), "txt_files")
        self.l = []



        with open(newPath + "\\commands.txt", "r") as f:
            self.l = f.readline().split(",")
            if self.l == [""]: self.l = []
        if len(self.l) != 0:
            try:
                self.textBrowser.append(self.l[self.cnt])

            except:
                pass
            self.cnt += 1

        else:
            self.cnt = 0

        print(self.l)

        if self.cnt == len(self.l):
            # print("skdfjkdjfdkfjdkfjdfk")
            with open(newPath + "\\commands.txt", "w") as f:
                f.write("")

            # time.sleep(1)

        #         time.sleep(1000)
        # with open(newPath + "\\commands.txt", "w") as f:
        #     f.write("")




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
