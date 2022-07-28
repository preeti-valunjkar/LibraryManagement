from dataclasses import dataclass


@dataclass
class StaffLoginCredentials:
    username: str = ""
    password: str = ""


@dataclass
class StaffData:
    employee_id: int = 0
    username: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    mobile_no: int = 0
    email: str = ""
