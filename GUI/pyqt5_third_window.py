# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt

class Ui_Widget(QtWidgets.QWidget):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1463, 766)



        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Widget.setFont(font)
        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(280, 100, 20, 671))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(110, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(430, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_4 = QtWidgets.QFrame(Widget)
        self.line_4.setGeometry(QtCore.QRect(-20, 140, 1581, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(10, 470, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(30, 580, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Widget)
        self.label_7.setGeometry(QtCore.QRect(30, 690, 81, 16))
        self.label_7.setObjectName("label_7")
        self.lcdNumber = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 170, 91, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(180, 450, 91, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(180, 560, 91, 51))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(180, 680, 91, 51))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(180, 330, 91, 51))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(1300, 10, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.line_5 = QtWidgets.QFrame(Widget)
        self.line_5.setGeometry(QtCore.QRect(0, 90, 1561, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_8 = QtWidgets.QLabel(Widget)
        self.label_8.setGeometry(QtCore.QRect(580, 20, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(Widget)
        self.line_2.setGeometry(QtCore.QRect(1020, 100, 20, 671))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Widget)
        self.line_3.setGeometry(QtCore.QRect(720, 60, 20, 711))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_6 = QtWidgets.QFrame(Widget)
        self.line_6.setGeometry(QtCore.QRect(730, 60, 20, 711))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_9 = QtWidgets.QLabel(Widget)
        self.label_9.setGeometry(QtCore.QRect(770, 190, 47, 13))
        self.label_9.setObjectName("label_9")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(920, 450, 91, 51))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(920, 560, 91, 51))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(920, 330, 91, 51))
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_9.setGeometry(QtCore.QRect(920, 170, 91, 51))
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.label_10 = QtWidgets.QLabel(Widget)
        self.label_10.setGeometry(QtCore.QRect(760, 340, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Widget)
        self.label_11.setGeometry(QtCore.QRect(770, 690, 81, 16))
        self.label_11.setObjectName("label_11")
        self.lcdNumber_10 = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber_10.setGeometry(QtCore.QRect(920, 680, 91, 51))
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.label_12 = QtWidgets.QLabel(Widget)
        self.label_12.setGeometry(QtCore.QRect(750, 470, 141, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Widget)
        self.label_13.setGeometry(QtCore.QRect(770, 580, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Widget)
        self.label_14.setGeometry(QtCore.QRect(1240, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Widget)
        self.label_15.setGeometry(QtCore.QRect(850, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.line_7 = QtWidgets.QFrame(Widget)
        self.line_7.setGeometry(QtCore.QRect(-10, 290, 1581, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Widget)
        self.line_8.setGeometry(QtCore.QRect(-20, 410, 1581, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Widget)
        self.line_9.setGeometry(QtCore.QRect(-10, 520, 1581, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Widget)
        self.line_10.setGeometry(QtCore.QRect(-40, 650, 1581, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.tableWidget = QtWidgets.QTableWidget(Widget)
        self.tableWidget.setGeometry(QtCore.QRect(290, 150, 421, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(6)
        item.setFont(font)
        self.tableWidget.setItem(3, 2, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_3.setGeometry(QtCore.QRect(290, 300, 421, 121))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        self.tableWidget_5 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_5.setGeometry(QtCore.QRect(290, 420, 421, 91))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        self.tableWidget_7 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_7.setGeometry(QtCore.QRect(290, 530, 421, 91))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        self.line_11 = QtWidgets.QFrame(Widget)
        self.line_11.setGeometry(QtCore.QRect(0, 50, 1561, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_16 = QtWidgets.QLabel(Widget)
        self.label_16.setGeometry(QtCore.QRect(330, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Widget)
        self.label_17.setGeometry(QtCore.QRect(1070, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.tableWidget_9 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_9.setGeometry(QtCore.QRect(290, 660, 421, 91))
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(1)
        self.tableWidget_9.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        self.tableWidget_10 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_10.setGeometry(QtCore.QRect(1030, 660, 421, 91))
        self.tableWidget_10.setObjectName("tableWidget_10")
        self.tableWidget_10.setColumnCount(1)
        self.tableWidget_10.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, item)
        self.tableWidget_6 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_6.setGeometry(QtCore.QRect(1030, 420, 421, 91))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        self.tableWidget_4 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_4.setGeometry(QtCore.QRect(1030, 300, 421, 121))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 0, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(1030, 150, 421, 151))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(6)
        item.setFont(font)
        self.tableWidget_2.setItem(3, 2, item)
        self.tableWidget_8 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_8.setGeometry(QtCore.QRect(1030, 530, 421, 91))
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(1)
        self.tableWidget_8.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)  # update every second

        self.showTime()

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Server"))
        self.label_2.setText(_translate("Widget", "Client"))
        self.label_3.setText(_translate("Widget", "ADCS"))
        self.label_4.setText(_translate("Widget", "Camera"))
        self.label_5.setText(_translate("Widget", "Communication"))
        self.label_6.setText(_translate("Widget", "OBC"))
        self.label_7.setText(_translate("Widget", "Power"))
        self.pushButton.setText(_translate("Widget", "Show"))
        self.label_8.setText(_translate("Widget", "Telemetry Subsystem"))
        self.label_9.setText(_translate("Widget", "ADCS"))
        self.label_10.setText(_translate("Widget", "Camera"))
        self.label_11.setText(_translate("Widget", "Power"))
        self.label_12.setText(_translate("Widget", "Communication"))
        self.label_13.setText(_translate("Widget", "OBC"))
        self.label_14.setText(_translate("Widget", "Client"))
        self.label_15.setText(_translate("Widget", "Server"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Gyro"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Accelerometer"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Widget", "Temp"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Widget", "Satalite angel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Widget", "X"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Widget", "Y"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Widget", "Z"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Widget", "kd"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Widget", ",jsd"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Status"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Mode"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Widget", "Temp"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("Widget", "32"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Status"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Temp"))
        item = self.tableWidget_7.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Status"))
        item = self.tableWidget_7.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Temp"))
        self.label_16.setText(_translate("Widget", "Sat 1"))
        self.label_17.setText(_translate("Widget", "Sat 2"))
        item = self.tableWidget_9.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Status"))
        item = self.tableWidget_9.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Temp"))
        item = self.tableWidget_10.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Status"))
        item = self.tableWidget_10.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Temp"))
        item = self.tableWidget_6.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Status"))
        item = self.tableWidget_6.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Temp"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Status"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Mode"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("Widget", "Temp"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.item(1, 0)
        item.setText(_translate("Widget", "32"))
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Gyro"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Accelerometer"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Widget", "Temp"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Widget", "Satalite angel"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Widget", "X"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Widget", "Y"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Widget", "Z"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("Widget", "kd"))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("Widget", ",jsd"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_8.verticalHeaderItem(0)
        item.setText(_translate("Widget", "Status"))
        item = self.tableWidget_8.verticalHeaderItem(1)
        item.setText(_translate("Widget", "Temp"))


        self.pushButton.clicked.connect(lambda: self.click())




    def click(self):


        newPath = os.path.join("\\".join(os.getcwd().split("\\")[:-1]), "txt_files")

        with open(newPath + "\\chosen_city.txt", "r") as f:
            xx=f.readline()


            # here change the values of all data
            self.item = self.tableWidget_2.item(1, 1)
            self.item.setText(xx)
            self.label_2.setText(xx)


    def showTime(self):
        currentTime = QTime.currentTime()

        displayTxt = currentTime.toString('hh:mm:ss')
        print(displayTxt)
        self.pushButton.click()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())