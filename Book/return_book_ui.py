# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/97150/PycharmProjects/LibraryManagement/Book/return_book.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReturnBook(object):
    def setupUi(self, ReturnBook):
        ReturnBook.setObjectName("ReturnBook")
        ReturnBook.resize(724, 552)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ReturnBook)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 90, 521, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.title_lbl.setObjectName("title_lbl")
        self.horizontalLayout.addWidget(self.title_lbl)
        self.title_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.horizontalLayout.addWidget(self.title_lineEdit)
        self.return_btn = QtWidgets.QPushButton(ReturnBook)
        self.return_btn.setGeometry(QtCore.QRect(230, 200, 231, 31))
        self.return_btn.setObjectName("return_btn")
        self.return_msg_lbl = QtWidgets.QLabel(ReturnBook)
        self.return_msg_lbl.setGeometry(QtCore.QRect(110, 260, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.return_msg_lbl.setFont(font)
        self.return_msg_lbl.setText("")
        self.return_msg_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.return_msg_lbl.setObjectName("return_msg_lbl")

        self.retranslateUi(ReturnBook)
        QtCore.QMetaObject.connectSlotsByName(ReturnBook)

    def retranslateUi(self, ReturnBook):
        _translate = QtCore.QCoreApplication.translate
        ReturnBook.setWindowTitle(_translate("ReturnBook", "Return Book"))
        self.title_lbl.setText(_translate("ReturnBook", "Book Title: "))
        self.return_btn.setText(_translate("ReturnBook", "Return Book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReturnBook = QtWidgets.QWidget()
    ui = Ui_ReturnBook()
    ui.setupUi(ReturnBook)
    ReturnBook.show()
    sys.exit(app.exec_())