from Staff.staff_data_classes import StaffLoginCredentials, StaffData
from destination import LIB_STAFF_DB
from pathlib import Path
import json
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import copy


class StaffDataManager:
    def __init__(self):
        self.__JSON_PATH = Path.joinpath(LIB_STAFF_DB, 'staff_data.json')
        self.__staff_data = {}
        self.__ph = PasswordHasher()

    def from_json(self):
        """
        Obtains information from the staff_data.json file if such a file
        exists in the directory. If not, then creates the directory and
        adds an initial staff user to it.
        :return: None
        """
        if Path(self.__JSON_PATH).exists():
            with open(self.__JSON_PATH) as json_file:
                temp_dict = json.load(json_file)
                for eid in temp_dict:
                    new_staff_user = StaffData(temp_dict[eid]['employee_id'],
                                               temp_dict[eid]['username'],
                                               temp_dict[eid]['password'],
                                               temp_dict[eid]['first_name'],
                                               temp_dict[eid]['last_name'],
                                               temp_dict[eid]['mobile_no'],
                                               temp_dict[eid]['email'])
                    self.__staff_data[eid] = new_staff_user
        else:
            self.create_temp_staff()

    def to_json(self):
        """
        The to_json function must be called when the user wishes to write
        the changes made to the local variable staff_data into the json file.
        This function makes changes to the staff_data.json file.
        :return: None
        """
        temp_dict = dict()
        for eid in self.__staff_data:
            temp_dict[eid] = self.__staff_data[eid].__dict__
        with open(self.__JSON_PATH, "w") as json_file:
            json.dump(temp_dict, json_file)

    def add_staff(self, new_staff_member):
        """
        Adds the given staff member to the staff database. Changes are made
        only to the local variable staff_data. Member may not be added if
        the employee id already exists in database.
        :parameter new_staff_member: Object of data type StaffData
        :return: Bool (True if member can be added, False otherwise)
        """
        if not new_staff_member.employee_id in self.__staff_data:
            self.__staff_data[new_staff_member.employee_id] = new_staff_member
            self.__staff_data[new_staff_member.employee_id].password = self.__hash_pass(self.__staff_data[new_staff_member.employee_id].password)
            return True
        else:
            return False

    def get_staff_details(self, employee_id):
        """
        Returns a deep copy of the data of the requested staff member.
        No changes are made to either the local variable or the json
        file. Function must be called only to change personal details
        of the given staff member (not password).
        :parameter employee_id: Str representing staff member's employee ID
        :return: Either an object of data type StaffData or None
        """
        if employee_id in self.__staff_data:
            new_copy = copy.deepcopy(self.__staff_data[employee_id])
            return new_copy
        else:
            return None

    def update_staff_detail(self, staff_member):
        """
        Updates the records of the given staff member. Changes are reflected
        only on the local variable staff_data. Users may call this function
        once they have changed the required information for a staff member
        and wish to store it.
        :parameter staff_member: Object of data type StaffData
        :return: Bool (True if updated successfully, False otherwise)
        """
        if str(staff_member.employee_id) in self.__staff_data:
            self.__staff_data[staff_member.employee_id] = staff_member
            return True
        else:
            return False

    def remove_staff_member(self, employee_id):
        """
        Removes the given staff member from the database. Changes are made
        only to the local variable staff_data.
        :parameter employee_id: Str representing the staff member's employee id
        :return: Bool (True if removed successfully, False otherwise)
        """
        if employee_id in self.__staff_data:
            del self.__staff_data[employee_id]
            return True
        else:
            return False

    def change_password(self, employee_id, password):
        """
        Takes in the employee_id and new password of a staff member and makes
        the required changes on the local variable staff_data.
        :parameter employee_id: Str representing the staff member's employee id
        :parameter password: String containing staff member's new password
        """
        if employee_id in self.__staff_data:
            self.__staff_data[employee_id].password = self.__hash_pass(password)
            return True
        else:
            return False

    def validate_pass(self, staff_cred):
        """
        Validates staff credentials. No changes are made to the local variable
        unless a rehash is needed.
        :parameter staff_cred: Object of data type StaffLoginCredential
        :return: Bool (True is authentic login, False otherwise)
        """
        for eid in self.__staff_data:
            if self.__staff_data[eid].username == staff_cred.username:
                staff_pass = self.__staff_data[eid].password
                try:
                    if self.__ph.verify(staff_pass, staff_cred.password):
                        if self.__ph.check_needs_rehash(staff_pass):
                            self.__staff_data[eid].password = self.__hash_pass(staff_cred.password)
                        return True
                except VerifyMismatchError:
                    return False
        return False

    def get_staff_name(self, uname):
        """
        Returns the full name of the staff member whose username is uname. Function
        is used for presenting information on the staff main window.
        :parameter uname: Str containing username of the staff member
        :return: Str (Full name of the staff member)
        """
        for eid in self.__staff_data:
            if self.__staff_data[eid].username == uname:
                return self.__staff_data[eid].first_name + ' ' + self.__staff_data[eid].last_name

    def __hash_pass(self, password):
        """
        hashPass function takes in a string which must be hashed for
        security and returns a hashed string.
        :parameter password: String containing password
        :return: string of hashed password
        """
        password_hash = self.__ph.hash(password)
        return password_hash

    def create_temp_staff(self):
        """
        Creates a temporary staff user when the file is newly created.
        Details are:
        Employee ID- 0, Username- teststaff, Password- teststaff
        (All other information is blank)
        :return: None
        """
        self.__staff_data[0] = StaffData(0, "teststaff", "teststaff")
        self.__staff_data[0].password = self.__hash_pass(self.__staff_data[0].password)
        temp_dict = dict()
        temp_dict[0] = self.__staff_data[0].__dict__
        if not Path(LIB_STAFF_DB).exists():
            Path.mkdir(LIB_STAFF_DB, exist_ok=True)
        with open(self.__JSON_PATH, "w") as json_file:
            json.dump(temp_dict, json_file)
