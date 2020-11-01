import json
from datetime import datetime, timedelta
from models.shift import Shift
from models.employee import Employee

def load():
    with open('smaller_schedule.json') as data:
        data = json.load(data)
        shifts = [Shift(day=s['day'], start=datetime.strptime(s['startTime'], "%H:%M:%S"), end=datetime.strptime(s['endTime'], "%H:%M:%S"), location=s['location']) for s in data['shifts']]
        employees = [Employee(cpr=e['cpr'], name=e['name'], min_hours=timedelta(hours=int(e['min_hours'])), max_hours=timedelta(hours=int(e['max_hours'])), locations=e['locations'], time_constraint=e['time_constraint']) for e in data['employees']]

        return shifts, employees

if __name__ == "__main__":
    print(load())  