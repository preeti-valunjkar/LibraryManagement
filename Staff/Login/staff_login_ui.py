# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/97150/PycharmProjects/pythonProject/Staff/Login/staff_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StaffLogin(object):
    def setupUi(self, StaffLogin):
        StaffLogin.setObjectName("StaffLogin")
        StaffLogin.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(StaffLogin)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 60, 261, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.username_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_lbl.setFont(font)
        self.username_lbl.setObjectName("username_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_lbl)
        self.username_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_lineEdit)
        self.password_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_lbl.setFont(font)
        self.password_lbl.setObjectName("password_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_lbl)
        self.password_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_lineEdit)
        self.message_lbl = QtWidgets.QLabel(StaffLogin)
        self.message_lbl.setGeometry(QtCore.QRect(50, 140, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.message_lbl.setFont(font)
        self.message_lbl.setText("")
        self.message_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.message_lbl.setObjectName("message_lbl")
        self.login_btn = QtWidgets.QPushButton(StaffLogin)
        self.login_btn.setGeometry(QtCore.QRect(120, 170, 161, 31))
        self.login_btn.setObjectName("login_btn")

        self.retranslateUi(StaffLogin)
        QtCore.QMetaObject.connectSlotsByName(StaffLogin)

    def retranslateUi(self, StaffLogin):
        _translate = QtCore.QCoreApplication.translate
        StaffLogin.setWindowTitle(_translate("StaffLogin", "Staff Login"))
        self.username_lbl.setText(_translate("StaffLogin", "Username: "))
        self.password_lbl.setText(_translate("StaffLogin", "Password: "))
        self.login_btn.setText(_translate("StaffLogin", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StaffLogin = QtWidgets.QWidget()
    ui = Ui_StaffLogin()
    ui.setupUi(StaffLogin)
    StaffLogin.show()
    sys.exit(app.exec_())