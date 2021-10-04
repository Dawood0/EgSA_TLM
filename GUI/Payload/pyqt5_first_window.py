# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import os

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(300, 377)
        Widget.setWindowTitle("Payload Subsystem")

        self.comboBox_2 = QtWidgets.QComboBox(Widget)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 100, 171, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems("Alexandria, Aswan, Assiut, Beheira, Beni Suef,"
                                 " Cairo, Dakahlia, Damietta, Fayoum, Gharbia, Giza,"
                                 " Ismailia, Kafr el-Sheikh, Matrouh, Minya, Menofia,"
                                 " New Valley, North Sinai, Port Said, Qualyubia, Qena,"
                                 " Red Sea, Al-Sharqia, Soha, South Sinai, Suez, Luxor".split(","))

        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 300, 141, 51))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.comboBox_2.setFont(font)

        # Title
        self.label_8 = QtWidgets.QLabel(Widget)
        self.label_8.setGeometry(QtCore.QRect(40, 13, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        # line
        self.line_4 = QtWidgets.QFrame(Widget)
        self.line_4.setGeometry(QtCore.QRect(0, 45, 1581, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")



        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(100, 200, 121, 51))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label.setFont(font)
        self.label.setObjectName("label")


        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

        # making the button function
        self.pushButton.clicked.connect(lambda:self.action())           # must use lambda here

        # real time showing the coordinates of the city chosen
        self.comboBox_2.activated.connect(self.handleActivated)         # handles the real time showing the city chosen

    def handleActivated(self, index):
        # print(self.comboBox_2.itemText(index))
        # print(self.comboBox_2.itemData(index))
        self.label.setText(self.comboBox_2.currentText())



    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "Save"))
        self.label.setText(_translate("Widget", "Alexandria"))
        self.label_8.setText(_translate("Widget", "Payload Subsystem"))


    # here the coordinates are needed to be put in the variable x to be displayed and sent to the second table
    def action(self):
        x = self.comboBox_2.currentText()
        # self.label.setText(x)

        newPath = os.path.join("\\".join(os.getcwd().split("\\")[:-2]), "txt_files")

        with open(newPath + "\\chosen_city.txt", "w") as f:
            f.writelines(x.strip())
        # with open(newPath + "\\chosen_city.txt", "r") as f:
        #     print(f.readlines())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

# testing commit