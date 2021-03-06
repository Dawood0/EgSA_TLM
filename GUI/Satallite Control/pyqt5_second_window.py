# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Widget(QtWidgets.QWidget):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(385, 600+30)
        self.checkBox_6 = QtWidgets.QCheckBox(Widget)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 40, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")


        # radio button
        self.radioButton = QtWidgets.QRadioButton(Widget)
        self.radioButton.setGeometry(QtCore.QRect(50+50, 550+30, 84, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton2 = QtWidgets.QRadioButton(Widget)
        self.radioButton2.setGeometry(QtCore.QRect(170+50, 550+30, 84, 19))
        self.radioButton2.setObjectName("radioButton")

        # choose button
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(64+40, 270+30, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        # clear button
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(62+40, 325+30, 175, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton")

        # send button
        self.pushButton_1 = QtWidgets.QPushButton(Widget)
        self.pushButton_1.setGeometry(QtCore.QRect(70+40, 360+30, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton")

        # Combobox getTLM subsystem
        self.comboBox_2 = QtWidgets.QComboBox(Widget)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(255, 163, 121, 15))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(" ,Communication,ADCS,OBC,Power,Payload,Broadcast".split(","))




        # title
        self.label_8 = QtWidgets.QLabel(Widget)
        self.label_8.setGeometry(QtCore.QRect(97, 3, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        # commands label
        self.label_9 = QtWidgets.QLabel(Widget)
        self.label_9.setGeometry(QtCore.QRect(50+45, 415+30, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_8")

        # line
        self.line_4 = QtWidgets.QFrame(Widget)
        self.line_4.setGeometry(QtCore.QRect(0, 28, 1581, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")





        self.checkBox_7 = QtWidgets.QCheckBox(Widget)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 60, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Widget)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 80, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Widget)
        self.checkBox_9.setGeometry(QtCore.QRect(30, 100, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")

        self.checkBox_1 = QtWidgets.QCheckBox(Widget)
        self.checkBox_1.setGeometry(QtCore.QRect(30, 120, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")

        self.checkBox_2 = QtWidgets.QCheckBox(Widget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 140, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_1")

        self.checkBox_3 = QtWidgets.QCheckBox(Widget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 160, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_1")

        self.checkBox_4 = QtWidgets.QCheckBox(Widget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 180, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_1")

        self.checkBox_5 = QtWidgets.QCheckBox(Widget)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 200, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_1")

        self.checkBox_10 = QtWidgets.QCheckBox(Widget)
        self.checkBox_10.setGeometry(QtCore.QRect(30, 220, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_1")

        self.checkBox_11 = QtWidgets.QCheckBox(Widget)
        self.checkBox_11.setGeometry(QtCore.QRect(30, 240, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_1")

        self.checkBox_18 = QtWidgets.QCheckBox(Widget)
        self.checkBox_18.setGeometry(QtCore.QRect(30, 260, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_18.setFont(font)
        self.checkBox_18.setObjectName("checkBox_18")

        self.text = QtWidgets.QTextBrowser(Widget)
        self.text.setGeometry(QtCore.QRect(50+45, 445+30, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text.setFont(font)
        self.text.setObjectName("label")

        # self.text=QtWidgets.QTextBrowser(Widget)

        self.label = QtWidgets.QLabel("Test", Widget)
        self.label.setGeometry(QtCore.QRect(125, 555, 53, 30))
        self.label.setStyleSheet("background:rgb(255,50,50)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # hidden pushButton
        self.pushButton_0 = QtWidgets.QPushButton(Widget)
        self.pushButton_0.setGeometry(QtCore.QRect(1300, 10, 141, 41))
        self.pushButton_0.setObjectName("pushButton")


        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)






        self.label.hide()


        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)  # update every second
        self.showTime()

        self.pushButton_0.hide()

        self.pushButton.clicked.connect(lambda: self.checked())
        self.pushButton_1.clicked.connect(lambda: self.send())
        self.pushButton_2.clicked.connect(lambda: self.clear())
        self.pushButton_0.clicked.connect(lambda: self.show())

        self.comboBox_2.activated.connect(self.handleActivated)

        self.state=0
        self.s = ""

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Satellite Control"))
        self.checkBox_6.setText(_translate("Widget", "openCom"))
        self.checkBox_7.setText(_translate("Widget", "closeCom"))
        self.checkBox_8.setText(_translate("Widget", "openADCS"))
        self.checkBox_9.setText(_translate("Widget", "closeADCS"))
        self.checkBox_1.setText(_translate("Widget", "openPayload"))
        self.checkBox_2.setText(_translate("Widget", "closePayload"))
        self.checkBox_3.setText(_translate("Widget", "getTLM        ------------->"))
        self.checkBox_4.setText(_translate("Widget", "getStoredTLM"))
        self.checkBox_5.setText(_translate("Widget", "getImage"))
        self.checkBox_10.setText(_translate("Widget", "clearTLM"))
        self.checkBox_11.setText(_translate("Widget", "clearImgs"))
        self.checkBox_18.setText(_translate("Widget", "captureImage"))

        self.pushButton.setText(_translate("Widget", "Choose commands"))
        self.pushButton_1.setText(_translate("Widget", "Send Commands"))
        self.pushButton_2.setText(_translate("Widget", "Clear Commands"))
        self.text.setText(_translate("Widget", ""))
        self.label_8.setText(_translate("Widget", "Satellite Control"))
        self.label_9.setText(_translate("Widget", "Commands:"))
        self.label.setText(_translate("Widget", "ACK"))


        self.radioButton.setText( "SAT1")
        self.radioButton2.setText( "SAT2")

        self.c=0
        self.pushButton_0.setText(_translate("Widget", "Show"))

    def handleActivated(self, index):
        # print(self.comboBox_2.itemText(index))
        # print(self.comboBox_2.itemData(index))
        # self.label.setText(self.comboBox_2.currentText())
        pass

    def checked(self):
        l="openCom,closeCom,openADCS,closeADCS,openPayload,closePayload,getTLM,getStoredTLM,getImage,clearTLM,clearImgs,captureImage".split(",")

        if self.checkBox_6.isChecked():
            self.s+=l[0]+"\n"
        elif self.checkBox_7.isChecked():
            self.s += l[1] + "\n"
        elif self.checkBox_8.isChecked():
            self.s += l[2] + "\n"
        elif self.checkBox_9.isChecked():
            self.s += l[3] + "\n"

        elif self.checkBox_1.isChecked():
            self.s += l[4] + "\n"
        elif self.checkBox_2.isChecked():
            self.s += l[5] + "\n"
        elif self.checkBox_3.isChecked():
            self.s += l[6] + "\n"
        elif self.checkBox_4.isChecked():
            self.s += l[7] + "\n"
        elif self.checkBox_5.isChecked():
            self.s += l[8] + "\n"
        elif self.checkBox_10.isChecked():
            self.s += l[9] + "\n"
        elif self.checkBox_11.isChecked():
            self.s += l[10] + "\n"
        elif self.checkBox_18.isChecked():
            self.s +=l[11]+"\n"
        self.text.setText(self.s)
        # print(self.checkBox_6.())
        for i in range(1,12):
            exec("self.checkBox_{}.setChecked(False)".format(i))

    def clear(self):
        self.s=""
        self.text.setText(self.s)

        for i in range(1,12):
            exec("self.checkBox_{}.setChecked(False)".format(i))

    def show(self):
        import os
        newPath = os.path.join("\\".join(os.getcwd().split("\\")[:-2]), "txt_files")
        # print(newPath+"\chosen_city.txt")
        chosen_city_file=newPath + "\\chosen_city.txt"
        with open(chosen_city_file, "r") as f:
            xx = f.readline()
            l = self.s.split("\n")[:-1]



            #       here change the condition if the packet is sent
            if xx=="ahmed" and ">" not in self.s and self.state==1:
                l = self.s.split("\n")[:-1]

                for i in range(len(l)):
                    if True:  # change this condition to whatever u want
                        l[i] = l[i].ljust(15) + "--> OK"
                self.s_ = "\n".join(l)
                self.text.setText(self.s_+"\n")


    def send(self):
        # put here the sending function                     ###########
        self.state=1
        import os
        newPath = os.path.join("\\".join(os.getcwd().split("\\")[:-2]), "txt_files")
        commands_file="commands.txt"
        with open(commands_file, "w") as f:
            f.write(",".join(self.s.split("\n")[:-1]))

        if self.radioButton2.isChecked():
            sat="01"
        elif self.radioButton.isChecked():
            sat="00"

        sub_file="sub.txt"
        with open(sub_file,"w") as f:
            f.write(self.comboBox_2.currentText())



        os.system("python stalliete_CTRL.py {}".format(sat))
        # os.system("python send.py")
        os.system("python send.py")






    def showTime(self):
        currentTime = QTime.currentTime()

        # displayTxt = currentTime.toString('hh:mm:ss')
        # print(displayTxt)
        self.pushButton_0.click()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
