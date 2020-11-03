from datetime import datetime, timedelta
from models.shift import Shift


class Employee:
    def __init__(
        self,
        cpr=None,
        name=None,
        min_hours=None,
        max_hours=None,
        locations=[],
        time_constraint=None,
    ):
        self.__cpr = cpr
        self.__name = name
        self.__min_hours = min_hours
        self.__max_hours = max_hours
        self.__locations = locations
        self.__time_constraint = time_constraint
        self.__shifts = []
        if time_constraint is None:
            self.default_time_constraint()
        else:
            self.__constraint_to_datetime()

    def default_time_constraint(self):
        self.__time_constraint = {
            "Monday": {"Earliest": "00:00:00", "Latest": "23:59:59"},
            "Tuesday": {"Earliest": "00:00:00", "Latest": "23:59:59"},
            "Wednesday": {"Earliest": "00:00:00", "Latest": "23:59:59"},
            "Thursday": {"Earliest": "00:00:00", "Latest": "23:59:59"},
            "Friday": {"Earliest": "00:00:00", "Latest": "23:59:59"},
            "Saturday": {"Earliest": "00:00:00", "Latest": "23:59:59"},
            "Sunday": {"Earliest": "00:00:00", "Latest": "23:59:59"},
        }

    def available_for_shift(self, shift):
        if self.get_assigned_hours() > self.__max_hours:
            return False

        if shift.get_location() not in self.__locations:
            return False

        if not self.__fits_time_constraint(shift):
            return False

        if self.__already_working(shift):
            return False

        return True

    def get_name(self):
        return self.__name

    def get_assigned_hours(self):
        hours = timedelta(hours=0)
        for shift in self.__shifts:
            hours = hours + shift.get_duration()

        return hours

    def assign_shift(self, shift):
        self.__shifts.append(shift)

    def assign_shifts(self, shifts):
        self.__shifts.extend(shifts)

    def get_shifts(self):
        return self.__shifts

    def remove_all_shifts(self):
        self.__shifts.clear()

    def remove_shift(self, shift):
        self.__shifts.remove(shift)

    def __fits_time_constraint(self, shift):
        early = self.__time_constraint[shift.get_day()]["Earliest"]
        late = self.__time_constraint[shift.get_day()]["Latest"]
        if (
            (early is None
            and late is None)
            or early > shift.get_start_time()
            or late < shift.get_end_time()
        ):
            return False

        return True

    def __already_working(self, shift):

        for owned_shift in self.__shifts:
            if owned_shift.get_day() != shift.get_day():
                o_day = owned_shift.get_day()
                s_day = shift.get_day()
                same = owned_shift.get_day() == shift.get_day()
                continue

            if (owned_shift.get_start_time() <= shift.get_end_time()) and (owned_shift.get_end_time() >= shift.get_start_time()):
                return True


        return False

    def __constraint_to_datetime(self):
        for day in self.__time_constraint:
            if self.__time_constraint[day]["Earliest"] is not None:
                self.__time_constraint[day]["Earliest"] = datetime.strptime(
                    self.__time_constraint[day]["Earliest"], "%H:%M:%S"
                )
            if self.__time_constraint[day]["Latest"] is not None:
                self.__time_constraint[day]["Latest"] = datetime.strptime(
                    self.__time_constraint[day]["Latest"], "%H:%M:%S"
                )

    def assess_fitness_of_shifts(self):

        constraints = 0
        constraints_met = 0
        hours_assigned = self.get_assigned_hours()

        if self.__min_hours is not None:
            constraints+=1
            if hours_assigned >= self.__min_hours:
                constraints_met+=1

        if self.__max_hours is not None:
            constraints+=1
            if hours_assigned <= self.__max_hours:
                constraints_met+=1



        days_with_shifts = []
        
        for shift in self.__shifts:

            if shift.get_location() in self.__locations:
                constraints+=1
                constraints_met+=1
            else:
                constraints+=1
                

            days_with_shifts.append(shift.get_day())

            early = self.__time_constraint[shift.get_day()]["Earliest"]
            late = self.__time_constraint[shift.get_day()]["Latest"]

            if early is None and late is None: #If employee has a shift when they should have had none
                constraints+=1
            else: 
                if shift.get_start_time() < early: #If shift is too early
                    constraints+=1
                else:
                    constraints+=1
                    constraints_met+=1

                if shift.get_end_time() > late: #If shift is too late
                    constraints+=1
                else:
                    constraints+=1
                    constraints_met+=1

        #days without shifts but has constraints
        for day in self.__time_constraint:
            if day in days_with_shifts:
                continue
            early = self.__time_constraint[day]["Earliest"]
            late = self.__time_constraint[day]["Latest"]
            if early is None and late is None:
                constraints+=1
                constraints_met+=1
                continue
            if early > datetime.strptime('00:00:00', "%H:%M:%S"):
                constraints+=1
                constraints_met+=1
            if late < datetime.strptime('23:59:59', "%H:%M:%S"):
                constraints+=1
                constraints_met+=1

            
        print(f'Days with shifts: {days_with_shifts}')
        times = []
        for td in [self.__min_hours, self.__max_hours, hours_assigned]:
            hours = int(td.total_seconds() // 3600)
            minutes = int((td.total_seconds() // 60) % 60)
            times.append(f'{hours}:{minutes}')

        return {
            "name": self.__name,
            "least": times[0],
            "most": times[1],
            "hours": times[2],
            "constraints_met": f'{constraints_met}/{constraints}',
            "percentile" : constraints_met/constraints
        }
