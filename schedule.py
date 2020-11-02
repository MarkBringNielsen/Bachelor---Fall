from random import choice
import time
class Schedule():

    def __init__(self, shifts, employees):
        self.__shifts = shifts
        self.__employees = employees
        self.__schedulers = [self.fastest_schedule, self.fulfilling_schedule]

    def fastest_schedule(self):
        for shift in self.__shifts:
            shift.assign_employee(choice(self.__employees))
        return self.__shifts

    def fulfilling_schedule(self, acceptable_percentile=0.9):
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


    def asses_success(self):
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


    def schedule(self):
        
        for shift in self.__shifts:
            fringe = []
            for employee in self.__employees:
                if employee.available_for_shift(shift):
                    fringe.append(employee)


from datamanagement import load
data = load()

Schedule(data[0], data[1]).asses_success()