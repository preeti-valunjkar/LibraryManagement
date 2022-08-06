from Member.member_main_window_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from pathlib import Path
from destination import LIB_CSS
from Book.book_data_manager import BookDataManager


class MemberMainWindowController(QtWidgets.QMainWindow):
    redirect_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MemberMainWindowController, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # setup triggers
        self.ui.actionSelect_Diff_User.triggered.connect(self.redirect_action_triggered)

        # setup css
        main_css = str(Path(LIB_CSS, 'main_pages.css'))
        font_css = str(Path(LIB_CSS, 'fonts.css'))
        with open(main_css, "r") as pss, open(font_css, "r") as fss:
            self.ui.centralwidget.setStyleSheet(pss.read() + fss.read())

    def setup_table(self):
        book_data = BookDataManager()
        book_data.from_json()
        book_dict = book_data.return_dict()
        i = 0
        for book in book_dict:
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)
            item = QtWidgets.QLabel()
            item.setText(book_dict[book].title)
            item.setToolTip("Rating: " + str(book_dict[book].rating) + "\n" +
                            "Publish Year: " + str(book_dict[book].publish_year) + "\n" +
                            "Description: " + book_dict[book].description)
            self.ui.tableWidget.setCellWidget(i, 0, item)
            item = QtWidgets.QLabel()
            item.setText(book_dict[book].author)
            self.ui.tableWidget.setCellWidget(i, 1, item)
            item = QtWidgets.QLabel()
            item.setText(book_dict[book].genre.name)
            self.ui.tableWidget.setCellWidget(i, 2, item)
            item = QtWidgets.QLabel()
            if not book_dict[book].borrower.first_name == "":
                item.setText("Yes")
            else:
                item.setText("No")
            self.ui.tableWidget.setCellWidget(i, 3, item)
            item = QtWidgets.QLabel()
            item.setText(book_dict[book].borrower.return_date)
            self.ui.tableWidget.setCellWidget(i, 4, item)
            i += 1

    def redirect_action_triggered(self):
        self.ui.tableWidget.setRowCount(0)
        self.close()
        self.redirect_signal.emit()
