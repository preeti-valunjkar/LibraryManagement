# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/97150/PycharmProjects/LibraryManagement/WelcomePage/welcome_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WelcomePage(object):
    def setupUi(self, WelcomePage):
        WelcomePage.setObjectName("WelcomePage")
        WelcomePage.resize(396, 298)
        font = QtGui.QFont()
        font.setPointSize(8)
        WelcomePage.setFont(font)
        WelcomePage.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(WelcomePage)
        self.gridLayout.setObjectName("gridLayout")
        self.welcome_lbl = QtWidgets.QLabel(WelcomePage)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_lbl.setFont(font)
        self.welcome_lbl.setStyleSheet("")
        self.welcome_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_lbl.setObjectName("welcome_lbl")
        self.gridLayout.addWidget(self.welcome_lbl, 0, 0, 1, 1)
        self.user_select_lbl = QtWidgets.QLabel(WelcomePage)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.user_select_lbl.setFont(font)
        self.user_select_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.user_select_lbl.setObjectName("user_select_lbl")
        self.gridLayout.addWidget(self.user_select_lbl, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.staff_btn = QtWidgets.QPushButton(WelcomePage)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.staff_btn.setFont(font)
        self.staff_btn.setObjectName("staff_btn")
        self.horizontalLayout.addWidget(self.staff_btn)
        self.member_btn = QtWidgets.QPushButton(WelcomePage)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.member_btn.setFont(font)
        self.member_btn.setObjectName("member_btn")
        self.horizontalLayout.addWidget(self.member_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(WelcomePage)
        QtCore.QMetaObject.connectSlotsByName(WelcomePage)

    def retranslateUi(self, WelcomePage):
        _translate = QtCore.QCoreApplication.translate
        WelcomePage.setWindowTitle(_translate("WelcomePage", "Welcome Page"))
        self.welcome_lbl.setText(_translate("WelcomePage", "Welcome to Mini Library!"))
        self.user_select_lbl.setText(_translate("WelcomePage", "Please select a user:"))
        self.staff_btn.setText(_translate("WelcomePage", "Staff"))
        self.member_btn.setText(_translate("WelcomePage", "Member"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QWidget()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())
