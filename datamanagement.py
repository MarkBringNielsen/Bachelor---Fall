import json
from models.shift import Shift
from models.employee import Employee
from datetime import datetime, timedelta

def load():
    with open('smaller_schedule.json') as data:
        data = json.load(data)


        shifts = []
        employees = []



        shifts = [Shift(day=s['day'], start=s['startTime'],end=s['endTime'], location=s['location']) for s in data['shifts']]
        #for json_employee in data['employees']:




        return shifts, employees

if __name__ == "__main__":
    print(load())