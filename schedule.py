from random import choice
import time
from itertools import islice
class Schedule():

    def __init__(self, shifts, employees):
        self.__shifts = shifts
        self.__employees = employees
        self.__schedulers = [self.fastest_schedule, self.fulfilling_schedule]

    def fastest_schedule(self):
        for shift in self.__shifts:
            shift.assign_employee(choice(self.__employees))
        return self.__shifts

    def fulfilling_schedule(self, acceptable_percentile=0.85):
        while True:
                
            for shift in self.__shifts:
                shift.assign_employee(choice(self.__employees))

            percentile = 0
            for employee in self.__employees:
                percentile += employee.assess_fitness_of_shifts()['percentile']
            percentile = percentile/len(self.__employees)
            if not percentile < acceptable_percentile:
                print(percentile)
                break
                
            
        return self.__shifts


    def assess_success(self):
        for schedule in self.__schedulers:
            print(schedule)
            
            start_time = time.time()
            schedule()
            print(f'Time spent: {time.time() - start_time}')
            for employee in self.__employees:
                print(employee.assess_fitness_of_shifts())


class Genetic_schedule():

    def __init__(self, shifts, employees):
        self.__shifts = shifts
        self.__employees = employees

    

class CS_schedule():

    def __init__(self, shifts, employees):
        self.__shifts = shifts
        self.__employees = employees


    def schedule(self, shifts, employees):

        if not shifts: #If list is empty something went wrong
            return False

        shift = shifts[0]
        domain = []
        for employee in employees:
            if employee.available_for_shift(shift):
                domain.append(employee)
        if not domain:
            return False
        
        #loop for checking if an employee path will succeed
        for employee in domain:

            shift.assign_employee(employee)

            if len(shifts) <= 1:
                return True
            if self.schedule(shifts[1:],employees):
                return True

            employee.remove_shift(shift)
        return False

    def assess_success(self):
        start_time = time.time()
        success = 'success' if self.schedule(self.__shifts, self.__employees) else 'failure'
        print(f'Time spent: {time.time() - start_time}')
        print(f'Schedule was a {success}')
        for employee in self.__employees:
            print(employee.assess_fitness_of_shifts())
        


from datamanagement import load
data = load()

#Schedule(data[0], data[1]).assess_success()
CS_schedule(data[0], data[1]).assess_success()
