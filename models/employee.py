import datetime


class employee():

    def __init__(self, cpr=None, name=None, min_hours=None, max_hours=None, locations=[], time_constraint=None):
        self.__cpr = cpr
        self.__name = name
        self.__min_hours = min_hours
        self.__max_hours = max_hours
        self.__locations = locations
        self.__time_constraint = time_constraint
        if time_constraint is None: self.default_time_constraint()

    
    def default_time_constraint(self):
        self.__time_constraint = {  'Monday'    : {'Earliest' : None, 'Latest' : None},
                                    'Tuesday'   : {'Earliest' : None, 'Latest' : None},
                                    'Wednesday' : {'Earliest' : None, 'Latest' : None},
                                    'Thursday'  : {'Earliest' : None, 'Latest' : None},
                                    'Friday'    : {'Earliest' : None, 'Latest' : None},
                                    'Saturday'  : {'Earliest' : None, 'Latest' : None},
                                    'Sunday'    : {'Earliest' : None, 'Latest' : None}}