import datetime

class shift():

    __start_time = None
    __end_time = None
    __location = None
    __employee = None

    def __init__(self, start, end, location, employee=None):
        self.__start_time = start
        self.__end_time = end
        self.__location = location
        self.__employee = employee


    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_location(self):
        return self.__location

    def is_covered(self):
        return self.__employee is not None
