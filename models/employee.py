from datetime import datetime, timedelta
from models.shift import Shift


class Employee:

    def __init__(self, cpr=None, name=None, min_hours=None, max_hours=None, locations=[], time_constraint=None):
        self.__cpr = cpr
        self.__name = name
        self.__min_hours = min_hours
        self.__max_hours = max_hours
        self.__locations = locations
        self.__time_constraint = time_constraint
        self.__shifts = []
        if time_constraint is None: self.default_time_constraint()

    
    def default_time_constraint(self):
        self.__time_constraint = {  'Monday'    : {'Earliest' : None, 'Latest' : None},
                                    'Tuesday'   : {'Earliest' : None, 'Latest' : None},
                                    'Wednesday' : {'Earliest' : None, 'Latest' : None},
                                    'Thursday'  : {'Earliest' : None, 'Latest' : None},
                                    'Friday'    : {'Earliest' : None, 'Latest' : None},
                                    'Saturday'  : {'Earliest' : None, 'Latest' : None},
                                    'Sunday'    : {'Earliest' : None, 'Latest' : None}}

    def available_for_shift(self, shift):
        if self.get_assigned_hours() > self.__max_hours:
            return False

        if shift.get_location not in self.__locations:
            return False

        if not self.__fits_time_constraint:
            return False


        return True

    def get_assigned_hours(self):
        hours = 0
        for shift in self.__shifts:
            hours += shift.get_duration()

        return hours

    def assign_shift(self, shift):
        self.__shifts.append(shift)

    def assign_shifts(self, shifts):
        self.__shifts.extend(shifts)

    def get_shifts(self):
        return self.__shifts

    def __fits_time_constraint(self, shift):
        early = self.__time_constraint[shift.get_day()]['Earliest']
        late = self.__time_constraint[shift.get_day()]['Latest']
        if early is None and late is None or early > shift.get_start_time() or late < shift.get_end_time():
            return False

        return True