from PyQt5 import QtWidgets, QtCore, QtGui, uic
from pathlib import Path
from destination import LIB_ROOT
from Staff.staff_data_classes import StaffData
from Staff.staff_data_manager import StaffDataManager


class StaffManagementController(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(StaffManagementController, self).__init__(*args, **kwargs)
        uic.loadUi(str(Path(LIB_ROOT, 'Staff/staff_management.ui')), self)
        self.changeinfostackedWidget.setCurrentIndex(0)

        # setup buttons
        self.add_staff_btn.clicked.connect(self.add_staff_btn_clicked)
        self.remove_staff_btn.clicked.connect(self.remove_staff_btn_clicked)
        self.get_details_btn.clicked.connect(self.get_details_btn_clicked)
        self.apply_changes_btn.clicked.connect(self.apply_btn_clicked)

    def add_staff_btn_clicked(self):
        staff_data = StaffDataManager()
        staff_data.from_json()
        new_staff = StaffData(self.eid_add_lineEdit.text(),
                              self.uname_lineEdit.text(),
                              self.pwd_lineEdit.text(),
                              self.fname_lineEdit.text(),
                              self.lname_lineEdit.text(),
                              self.mobno_lineEdit.text(),
                              self.email_lineEdit.text())
        if staff_data.add_staff(new_staff):
            staff_data.to_json()
            self.clear_all_add()
            self.add_status_lbl.setText("Staff member added successfully")
        else:
            self.add_status_lbl.setText("Staff member exists. Use different EID")

    def remove_staff_btn_clicked(self):
        staff_data = StaffDataManager()
        staff_data.from_json()
        remove_staff = self.eid_remove_lineEdit.text()
        if staff_data.remove_staff_member(remove_staff):
            self.eid_remove_lineEdit.clear()
            self.remove_status_lbl.setText("Staff member removed successfully")
        else:
            self.remove_status_lbl.setText("Staff member does not exist")

    def get_details_btn_clicked(self):
        staff_data = StaffDataManager()
        staff_data.from_json()
        employee_id = self.eid_change_lineEdit.text()
        get_staff = staff_data.get_staff_details(employee_id)
        if get_staff:
            self.changeinfostackedWidget.setCurrentIndex(1)
            self.fname_change_lineEdit.setText(get_staff.first_name)
            self.lname_changed_lineEdit.setText(get_staff.last_name)
            self.mobno_changed_lineEdit.setText(str(get_staff.mobile_no))
            self.email_changed_lineEdit.setText(get_staff.email)
        else:
            self.get_staff_status_lbl.setText("Staff member does not exist")

    def apply_btn_clicked(self):
        staff_data = StaffDataManager()
        staff_data.from_json()
        staff_update = staff_data.get_staff_details(self.eid_change_lineEdit.text())
        if self.fname_change_lineEdit.isModified():
            staff_update.first_name = self.fname_change_lineEdit.text()
        if self.lname_changed_lineEdit.isModified():
            staff_update.last_name = self.lname_changed_lineEdit.text()
        if self.mobno_changed_lineEdit.isModified():
            staff_update.mobile_no = int(self.mobno_changed_lineEdit.text())
        if self.email_changed_lineEdit.isModified():
            staff_update.email = self.email_changed_lineEdit.text()
        staff_data.update_staff_detail(staff_update)
        staff_data.to_json()
        self.apply_msg_lbl.setText("Staff member information updated successfully")

    def clear_all_add(self):
        self.eid_add_lineEdit.clear()
        self.uname_lineEdit.clear()
        self.pwd_lineEdit.clear()
        self.fname_lineEdit.clear()
        self.lname_lineEdit.clear()
        self.mobno_lineEdit.clear()
        self.email_lineEdit.clear()
