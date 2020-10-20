from datetime import datetime, timedelta
from shift import Shift


class Employee:

    def __init__(self, cpr=None, name=None, min_hours=None, max_hours=None, locations=[], time_constraint=None):
        self.__cpr = cpr
        self.__name = name
        self.__min_hours = min_hours
        self.__max_hours = max_hours
        self.__locations = locations
        self.__time_constraint = time_constraint
        self.__shifts = []
        if time_constraint is None: self.default_time_constraint() else: self.__constraint_to_datetime()

    
    def default_time_constraint(self):
        self.__time_constraint = {  'Monday'    : {'Earliest' : '00:00:00', 'Latest' : '23:59:59'},
                                    'Tuesday'   : {'Earliest' : '00:00:00', 'Latest' : '23:59:59'},
                                    'Wednesday' : {'Earliest' : '00:00:00', 'Latest' : '23:59:59'},
                                    'Thursday'  : {'Earliest' : '00:00:00', 'Latest' : '23:59:59'},
                                    'Friday'    : {'Earliest' : '00:00:00', 'Latest' : '23:59:59'},
                                    'Saturday'  : {'Earliest' : '00:00:00', 'Latest' : '23:59:59'},
                                    'Sunday'    : {'Earliest' : '00:00:00', 'Latest' : '23:59:59'}}

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

    def __constraint_to_datetime(self):
        for day in self.__time_constraint:
            if self.__time_constraint[day]['Earliest'] is not None: 
                self.__time_constraint[day]['Earliest'] = datetime.strptime(self.__time_constraint[day]['Earliest'])
            if self.__time_constraint[day]['Latest'] is not None:
                self.__time_constraint[day]['Latest'] = datetime.strptime(self.__time_constraint[day]['Latest'])
