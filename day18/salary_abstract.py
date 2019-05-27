# -*- coding:utf8 -*-
from abc import ABCMeta, abstractmethod

"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""

class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self._name=name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
    
    def get_salary(self):
        return 15000
    

class Programmer(Employee):
    def __init__(self, name, work_hour):
        super().__init__(name)
        self._work_hour = work_hour
    
    def get_salary(self):
        return 200 * self._work_hour


class Salesman(Employee):
    def __init__(self, name, sales):
        super().__init__(name)
        self._sales=sales

    def get_salary(self):
        return 1800 + self._sales * 0.05


class EmployeeFactory(object):
    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp


def main():
    emps = [
        EmployeeFactory.create('M', '曹操'), 
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85), 
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print('%s: %.2f元' % (emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()
    