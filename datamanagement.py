import json
from models.shift import Shift
from models.employee import Employee

def load():
    with open('smaller_schedule.json') as data:
        data = json.load(data)
        shifts = [Shift(day=s['day'], start=s['startTime'],end=s['endTime'], location=s['location']) for s in data['shifts']]
        employees = [Employee(cpr=e['cpr'], name=e['name'], min_hours=['min_hours'], max_hours=e['max_hours'], locations=e['locations'], time_constraint=e['time_constraint']) for e in data['employees']]

        return shifts, employees

if __name__ == "__main__":
    print(load())  