from PyQt5 import QtWidgets, QtCore, QtGui, uic
from pathlib import Path
from destination import LIB_ROOT
from Staff.staff_data_manager import StaffDataManager


class StaffProfileController(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(StaffProfileController, self).__init__(*args, **kwargs)
        uic.loadUi(str(Path(LIB_ROOT, 'Staff/staff_profile.ui')), self)
        self.current_staff = None

        # setup buttons
        self.apply_btn.hide()
        self.change_info_btn.clicked.connect(self.change_info_btn_clicked)
        self.apply_btn.clicked.connect(self.apply_btn_clicked)

    def change_info_btn_clicked(self):
        self.pwd_lineEdit.setEnabled(True)
        self.fname_lineEdit.setEnabled(True)
        self.lname_lineEdit.setEnabled(True)
        self.mobno_lineEdit.setEnabled(True)
        self.email_lineEdit.setEnabled(True)
        self.apply_btn.show()
        self.change_msg_lbl.setText("Please make required changes in the above boxes itself.")

    def apply_btn_clicked(self):
        staff_data = StaffDataManager()
        staff_data.from_json()
        if self.pwd_lineEdit.isModified():
            self.current_staff.password = staff_data.change_password(self.current_staff.employee_id,
                                                                     self.pwd_lineEdit.text())
        if self.fname_lineEdit.isModified():
            self.current_staff.first_name = self.fname_lineEdit.text()
        if self.lname_lineEdit.isModified():
            self.current_staff.last_name = self.lname_lineEdit.text()
        if self.mobno_lineEdit.isModified():
            self.current_staff.mobile_no = self.mobno_lineEdit.text()
        if self.email_lineEdit.isModified():
            self.current_staff.email = self.email_lineEdit.text()
        if staff_data.update_staff_detail(self.current_staff):
            staff_data.to_json()
            self.apply_msg_lbl.setText("Your profile was updated successfully")
        else:
            self.apply_msg_lbl.setText("Profile not updated.")

    def setup(self, name):
        staff_data = StaffDataManager()
        staff_data.from_json()
        self.current_staff = staff_data.return_staff_details(name)
        self.eid_lineEdit.setText(str(self.current_staff.employee_id))
        self.uname_lineEdit.setText(self.current_staff.username)
        self.fname_lineEdit.setText(self.current_staff.first_name)
        self.lname_lineEdit.setText(self.current_staff.last_name)
        self.mobno_lineEdit.setText(str(self.current_staff.mobile_no))
        self.email_lineEdit.setText(self.current_staff.email)
        self.welcome_msg_lbl.setText("Here's your profile, " + name)
