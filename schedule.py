from random import choice
import time
class Schedule():

    def __init__(self, shifts, employees):
        self.__shifts = shifts
        self.__employees = employees

    def fastest_schedule(self):
        for shift in self.__shifts:
            shift.assign_employee(choice(self.__employees))
        return self.__shifts

    def fulfilling_schedule(self):
        return self.__shifts


    def asses_success(self):
        start_time = time.time()
        self.fastest_schedule()
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
        

        return None


from datamanagement import load
data = load()

Schedule(data[0], data[1]).asses_success()