# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 11/12/2022
# Description: Write a class named Employee that has private
# data members for an employee's name, ID_number, salary, and email_address.

class Employee:
    """Represents employee information"""

    def __init__(self, name, id_number, salary, email):
        """Defines employee information"""
        self.__name = name
        self.__ID_number = id_number
        self.__salary = salary
        self.__email_address = email

    def get_name(self):
        """Returns the name of the employee"""
        return self.__name

    def get_ID_number(self):
        """Returns the ID number of the employee"""
        return self.__ID_number

    def get_salary(self):
        """Returns the salary of the employee"""
        return self.__salary

    def get_email_address(self):
        """Returns the email of the employee"""
        return self.__email_address


def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    """Returns dictionary of employee objects"""
    employee_dict = {}
    for emps in range(0, len(emp_names)):
        """Creates employee as an object and adds it to dictionary"""
        emp = Employee(emp_names[emps], emp_ids[emps], emp_sals[emps], emp_emails[emps])
        employee_dict[emp_ids[emps]] = emp

    return employee_dict


emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result_dictionary = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)

# for key, value in result_dictionary.items():
# print(key, value.get_name(), value.get_salary(), value.get_email_address())
