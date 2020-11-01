import datetime

class Shift:
    __id = None
    __start_time = None
    __end_time = None
    __location = None
    __employee = None
    __day = None

    def __init__(self, day, start, end, location, employee=None):
        self.__start_time = start
        self.__end_time = end
        self.__location = location
        self.__employee = employee
        self.__day = day


    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_location(self):
        return self.__location

    def is_covered(self):
        return self.__employee is not None

    def get_duration(self):
        return self.__end_time - self.__start_time

    def get_employee(self):
        return self.__employee

    def assign_employee(self, employee):
        self.__employee = employee
        employee.assign_shift(self)
