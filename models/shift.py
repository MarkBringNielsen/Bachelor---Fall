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
